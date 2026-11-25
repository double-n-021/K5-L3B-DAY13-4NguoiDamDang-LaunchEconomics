"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    return 1 / p if k is None else (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    return 1.0 if k is None else 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    token = float(tien_token.sum())
    tool = float(tien_tool.sum())
    chay_lai = float((tien_token + tien_tool)[runs['attempt'] > 1].sum())
    xem_lai = float(reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai)
    lam_lai = float(reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai)
    tong = token + tool + xem_lai + lam_lai
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())
    cps = tong / thanh_cong
    hoa_don_moi_yc = (token + tool) / len(reqs)

    return dict(
        token=token,
        tool=tool,
        chay_lai=chay_lai,
        xem_lai=xem_lai,
        lam_lai=lam_lai,
        tong=tong,
        thanh_cong=thanh_cong,
        cps=cps,
        hoa_don_moi_yc=hoa_don_moi_yc,
    )


def in_phan_tich_cp1_cp2(runs, reqs, ket_qua):
    """In bảng số liệu CP1 (A2, A3, A4) và CP2 (B1, B2, B3, B4) để kiểm tra và điền báo cáo."""
    # --- A2: Thông số bổ sung ---
    tong_tool_calls = int(runs['tool_calls'].sum())
    phut_xem_lai = float(reqs['phut_xem_lai_simulated'].sum())
    phut_lam_lai = float(reqs['phut_lam_lai_simulated'].sum())
    khong_tc = len(reqs) - ket_qua['thanh_cong']
    he_thong_moi_yc = (ket_qua['tong'] + khong_tc * BASELINE) / len(reqs)
    print('\n--- A2 · Chi tiết bổ sung ---')
    print(f"So lan goi tool: {tong_tool_calls:,}")
    print(f"Phut xem lai [simulated]: {phut_xem_lai:,.0f} ({ket_qua['xem_lai']/ket_qua['tong']*100:.1f}%)")
    print(f"Phut lam lai [simulated]: {phut_lam_lai:,.0f} ({ket_qua['lam_lai']/ket_qua['tong']*100:.1f}%)")
    print(f"Hoa don token+tool / yc: {ket_qua['hoa_don_moi_yc']:.1f} d")
    print(f"CPS / Hoa don moi yc: {ket_qua['cps'] / ket_qua['hoa_don_moi_yc']:.1f}x")
    print(f"Chi phi ca he thong / yc [simulated]: {he_thong_moi_yc:,.0f} d ({he_thong_moi_yc / BASELINE:.2f}x)")

    # --- A3: Tách theo loại yêu cầu ---
    print('\n--- A3 · Tách theo loại yêu cầu ---')
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        sub = reqs[reqs['loai'] == loai]
        kq_loai = mo_hinh(runs, sub)
        ti_le_tc = (sub['ket_qua'] == 'thanh_cong').mean() * 100
        tb_chay = sub['so_lan_chay'].mean()
        print(
            f"{loai:10s} | n={len(sub):4d} | TC={ti_le_tc:5.1f}% | "
            f"chay/yc={tb_chay:.2f} | cps [sim]={kq_loai['cps']:8,.0f} d | "
            f"vs 12k={kq_loai['cps'] / BASELINE:.2f}x"
        )

    runs_loai = runs.merge(reqs[['request_id', 'loai']], on='request_id')
    runs_loai['is_ok'] = runs_loai['status'] == 'ok'
    ti_le_ok_lan = runs_loai.pivot_table(index='loai', columns='attempt', values='is_ok', aggfunc='mean') * 100
    print('\nTi le status=ok theo lan thu (%):')
    print(ti_le_ok_lan.round(1).to_string())

    # --- A4: Chi phí cố định (phạm vi noi_dia + hang_nang) ---
    CHI_PHI_CO_DINH = 40_000_000
    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    kq_pv = mo_hinh(runs, pham_vi)
    print('\n--- A4 · Chi phí cố định (noi_dia + hang_nang) ---')
    for nhan, khoi_luong in [('45.000 yc/thang', 45_000), ('Mot nua khoi luong', 22_500)]:
        viec_tc_thang = khoi_luong * (kq_pv['thanh_cong'] / len(reqs))
        co_dinh_moi_viec = CHI_PHI_CO_DINH / viec_tc_thang
        cps_co_dinh = kq_pv['cps'] + co_dinh_moi_viec
        print(
            f"{nhan:20s} | TC/thang={viec_tc_thang:7,.0f} | "
            f"co dinh={co_dinh_moi_viec:6,.0f} d | tong cps [sim]={cps_co_dinh:6,.0f} d "
            f"({cps_co_dinh / BASELINE:.2f}x)"
        )

    # --- B1: Bảng độ nhạy ---
    print('\n--- B1 · Bảng độ nhạy ---')
    kich_ban = {
        'Gia token gap doi': dict(gia_vao=52, gia_ra=260),
        'Gia token giam mot nua': dict(gia_vao=13, gia_ra=65),
        'Xem lai gap doi': dict(he_so_xem_lai=2.0),
        'Xem lai giam mot nua': dict(he_so_xem_lai=0.5),
        'Lam lai gap doi': dict(he_so_lam_lai=2.0),
        'Lam lai giam mot nua': dict(he_so_lam_lai=0.5),
        'Luong tang 25%': dict(luong_phut=2500),
        'Toi da 2 lan chay': dict(max_lan_chay=2),
        'Chi 1 lan chay': dict(max_lan_chay=1),
    }
    goc = ket_qua['cps']
    for ten, kw in kich_ban.items():
        cps_kb = mo_hinh(runs, reqs, **kw)['cps']
        pct = (cps_kb / goc - 1) * 100
        print(f"{ten:25s} | cps [sim]={cps_kb:6,.0f} d | {pct:+6.1f}%")

    # --- B2: Đổi một cặp ---
    cps_cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2.0)['cps']
    print(f"\n--- B2 · Doi cap (token x2 + xem lai x2) ---")
    print(f"cps [sim]={cps_cap:,.0f} d ({(cps_cap / goc - 1) * 100:+.1f}%)")

    # --- B3: Giới hạn chạy lại và chi phí cả hệ thống ---
    print('\n--- B3 · Giới hạn chạy lại vs Chi phí cả hệ thống ---')
    for k in [1, 2, 3]:
        kq_k = mo_hinh(runs, reqs, max_lan_chay=k)
        khong_tc_k = len(reqs) - kq_k['thanh_cong']
        ca_he_thong = kq_k['tong'] + khong_tc_k * BASELINE
        print(
            f"{k} lan | tong tro ly [sim]={kq_k['tong']:10,.0f} d | "
            f"khong TC={khong_tc_k:3d} | ca he thong [sim]={ca_he_thong:10,.0f} d | "
            f"cps [sim]={kq_k['cps']:5,.0f} d"
        )

    # --- B4: Xem lại 100% (noi_dia + hang_nang) ---
    print('\n--- B4 · Xem lại 100% (noi_dia + hang_nang) ---')
    runs_pv = runs[runs['request_id'].isin(pham_vi['request_id'])]
    yc_co_ok = runs_pv[runs_pv['status'] == 'ok']['request_id'].nunique()
    so_lam_lai_pv = int((pham_vi['ket_qua'] == 'lam_lai').sum())
    token_tool_pv = kq_pv['token'] + kq_pv['tool']
    tb_phut_lam_lai = float(reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated'].mean())

    for nhan, phut_ll in [('9 phut/ca (theo de)', 9.0), (f'{tb_phut_lam_lai:.1f} phut/ca (TB du lieu)', tb_phut_lam_lai)]:
        tong_b4 = token_tool_pv + yc_co_ok * 5 * LUONG_PHUT + so_lam_lai_pv * phut_ll * LUONG_PHUT
        cps_b4 = tong_b4 / kq_pv['thanh_cong']
        hoa_von_xem_lai = (kq_pv['thanh_cong'] * BASELINE - token_tool_pv - so_lam_lai_pv * phut_ll * LUONG_PHUT) / (yc_co_ok * LUONG_PHUT)
        print(
            f"{nhan:30s} | tong [sim]={tong_b4:10,.0f} d | "
            f"cps [sim]={cps_b4:6,.0f} d ({cps_b4 / BASELINE:.2f}x) | "
            f"hoa von xem lai <= {hoa_von_xem_lai:.1f} phut"
        )


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        fmt = f'{gia_tri:>14,.1f}' if ten == 'hoa_don_moi_yc' else f'{gia_tri:>14,.0f}'
        print(f'{ten:15s} {fmt}')
    in_phan_tich_cp1_cp2(runs, reqs, ket_qua)
    # TODO CP4 · Nhiệm vụ D: cỡ mẫu.
    #   from statsmodels.stats.proportion import proportion_effectsize
    #   from statsmodels.stats.power import NormalIndPower
