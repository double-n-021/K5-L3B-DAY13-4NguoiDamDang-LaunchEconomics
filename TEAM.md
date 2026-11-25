# Team

## Thông tin nhóm

- Tên nhóm: `4NguoiDamDang`
- Lớp: `L3B`
- Repo nhóm: `K5-L3B-DAY13-4NguoiDamDang-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: https://github.com/double-n-021/K5-L3B-DAY13-4NguoiDamDang-LaunchEconomics · nhánh `main` · (cập nhật commit chốt khi nộp)

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Đỗ Hoàng Vũ | 2A202603920 | dohoangvu.nt2005@gmail.com | `hoangvu1806` | Người viết code (Developer — CP1, CP2) |
|   2 | Trần Gia Bảo | 2A202603914 | trangiabao433@gmail.com | `Jay-Gabriel` | Người kiểm số (Data Validator — CP1, CP2; đổi vai viết code CP4) |
|   3 | Nguyễn Bảo Duy | 2A202603890 | baoduy2048@gmail.com | `baoduy2048` | Người gắn nhãn 1 (Annotator 1 & Metrics Owner) |
|   4 | Bùi Đặng Nhật Nguyên | 2A202603937 | | `double-n-021` | Người gắn nhãn 2 kiêm Giữ hồ sơ (Annotator 2 & Doc Owner) |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/team/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

### Đỗ Hoàng Vũ - 2A202603920

#### Phần việc phụ trách

- Người viết code (Developer) giai đoạn CP1, CP2; rà soát D2 và kỹ thuật rollback ở CP4; hỗ trợ bảo vệ kỹ thuật tại Gate 2a.

#### Đóng góp cụ thể

- Thiết lập và kiểm tra môi trường Python (`pandas`, `numpy`, `scipy`, `statsmodels`, `yaml`) trong `src/`.
- Hoàn thiện phần code CP1 trong `src/lab13.py`: 3 hàm lý thuyết A1 (`so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`), hàm `mo_hinh` (A2), tách chi phí theo 4 loại yêu cầu và tỉ lệ `ok` theo lần thử (A3), tính chi phí cố định 40 triệu đ/tháng cho phạm vi `noi_dia + hang_nang` (A4).
- Hoàn thiện phần code CP2 trong `src/lab13.py`: chạy 9 kịch bản độ nhạy B1, kịch bản cặp B2, so sánh giới hạn 1/2/3 lần chạy kèm chi phí cả hệ thống (B3), và kịch bản xem lại 100% cho `noi_dia + hang_nang` kèm mức hòa vốn (B4).
- Chuẩn bị phân tích 5 câu hỏi tách tác động (D2) và phương án kỹ thuật rollback trong 30 phút cho CP4.

#### Bằng chứng

- File code `src/lab13.py` chạy qua đủ 3 phép thử A1 (`Ba phép thử đáp án biết trước: ĐẠT`: `1,20 · 1,25 · 1,25`) và xuất đủ bảng số liệu A2–A4, B1–B4.
- Báo cáo cá nhân `report/team/2A202603920_DoHoangVu.md`.

### Trần Gia Bảo - 2A202603914

#### Phần việc phụ trách

- Người kiểm số (Data Validator) ở CP1, CP2; phụ trách `report/team/bang_chi_phi.md`; đổi vai viết code phần D1, E1 trong `src/lab13.py` sau giờ giải lao.

#### Đóng góp cụ thể

- Cài đặt môi trường `src/.venv` trên máy thứ hai và chạy kiểm chứng chéo toàn bộ kết quả CP1–CP2 từ `src/lab13.py` (3 phép thử A1 đạt `1,20 · 1,25 · 1,25`, sai số đối chiếu 0%).
- Hoàn thiện toàn bộ `report/team/bang_chi_phi.md` (bảng A1–A4, B1–B4, tính tuyến tính B1/B2, chi phí cả hệ thống B3, kịch bản xem lại 100% ở B4 kèm mức hòa vốn, đầy đủ nhãn `simulated`).
- Đổi vai viết code phần D1 (`co_mau`, 5 câu cỡ mẫu theo cụm ICC = 0,02, power thực `0,64` bằng `statsmodels`, tỉ lệ `mo_lai_trong_7_ngay` hiện tại `4,25%` / `3,97%`) và phần E1 (3 chỉ số chạy thử `82,83%`, `27,12%`, `4,25%`) trong `src/lab13.py`.

#### Bằng chứng

- Commit `8abb41f` và PR #2 (`feat/bao-cp1-cp4-validation` → `main`): https://github.com/double-n-021/K5-L3B-DAY13-4NguoiDamDang-LaunchEconomics/pull/2
- Các file `report/team/bang_chi_phi.md`, `src/lab13.py` và báo cáo cá nhân `report/team/2A202603914_TranGiaBao.md`.

### Nguyễn Bảo Duy - 2A202603890

#### Phần việc phụ trách

- Người gắn nhãn 1 (Annotator 1) ở CP3 (gắn nhãn độc lập 20 ca lỗi); phụ trách `report/team/chi_so.md` (đặc tả chỉ số, event có `trace_id`, rủi ro kinh tế); theo dõi tiêu chí "Xong khi".

#### Đóng góp cụ thể

- Gắn nhãn độc lập 20/20 ca lỗi theo Google PAIR ở CP3 trên nhánh `baoduy` (đạt 20/20 = 100% đồng thuận khi so chéo với Bùi Đặng Nhật Nguyên).
- Hoàn thiện `report/team/chi_so.md`: 3 chỉ số tính thử (82,83%, 27,12%, 4,25%) và 2 chỉ số tự đề xuất, 10 event có `trace_id` kèm bảng kiểm tra chéo, và 3 dòng rủi ro kinh tế đối chiếu từ CSV và `src/lab13.py` (có nhãn `simulated`).
- Tạo báo cáo cá nhân `report/team/2A202603890_NguyenBaoDuy.md`.

#### Bằng chứng

- Commit `6c52cff` (`bang_loi.md` cột `Nhãn người 1`) và commit `de2fed5` (`report/team/chi_so.md`, `report/team/2A202603890_NguyenBaoDuy.md`) trên nhánh `baoduy`.

### Bùi Đặng Nhật Nguyên - 2A202603937

#### Phần việc phụ trách

- Người gắn nhãn 2 kiêm Giữ hồ sơ (Annotator 2 & Doc Owner): gắn nhãn độc lập 20 ca lỗi ở CP3, tổng hợp `report/team/bang_loi.md`, `report/team/pilot_plan.yaml`, `report/team/ho_so_launch_v0.md`, `report/team/phieu_cham.md`, `report/team/group_report.md` và `TEAM.md`.

#### Đóng góp cụ thể

- Khởi tạo repo nhóm lớp `L3B`, cập nhật `TEAM.md` và biên soạn bảng phân công quy trình Branch/PR tại `PHAN_CONG_NHOM.md`.
- Đồng bộ `origin/main` và chạy kiểm chứng độc lập toàn bộ `src/lab13.py` (A1–E1, gồm `statsmodels`) trên máy thứ 2; cập nhật số liệu Mục 1–3, 5–6 vào `report/team/ho_so_launch_v0.md`.
- Gắn nhãn độc lập 20/20 ca lỗi theo Google PAIR, so chéo với Nguyễn Bảo Duy (đạt 20/20 = 100% đồng thuận) và hoàn thiện `report/team/bang_loi.md` (5 quy tắc phân biệt và bảng khắc phục 5 loại lỗi).
- Hoàn thiện toàn bộ `report/team/pilot_plan.yaml` (D1, D2, công khai đánh đổi MDE +6 điểm / power 0,64, 3 luật dừng định lượng 4 vế, danh sách số `simulated`).

#### Bằng chứng

- Commit khởi tạo `TEAM.md` (`044da17`) và `PHAN_CONG_NHOM.md` (`4996cd8`) trên nhánh `main`.
- Nhánh `feat/nguyen-cp3-cp5-docs`: `report/team/bang_loi.md`, `report/team/pilot_plan.yaml`, `report/team/ho_so_launch_v0.md`, `report/team/group_report.md`, `report/team/2A202603937_BuiDangNhatNguyen.md`.
