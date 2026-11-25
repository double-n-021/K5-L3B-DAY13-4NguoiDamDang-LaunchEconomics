# Báo cáo cá nhân — TranGiaBao-2A202603914

## 1. Thông tin thành viên

- Họ tên: Trần Gia Bảo
- MSSV: 2A202603914
- Email: trangiabao433@gmail.com
- GitHub: `Jay-Gabriel`
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): Người kiểm số (Data Validator — CP1, CP2) và Người viết code (Developer — CP4, E1)

## 2. Phần việc phụ trách

- Thiết lập môi trường Python (`src/.venv`) trên máy thứ hai để kiểm chứng khả năng chạy tái lập của `src/lab13.py`.
- Giai đoạn CP1–CP2: Kiểm chứng số liệu đầu ra từ code của Đỗ Hoàng Vũ (đối chiếu phép tính tay, sai số ≤ 2%, kiểm tra tính tuyến tính B1/B2, đảm bảo nhãn `simulated`), hoàn thiện toàn bộ file `report/team/bang_chi_phi.md`.
- Giai đoạn CP4–CP5 (đổi vai viết code sau giải lao): Tiếp quản `src/lab13.py` trên nhánh riêng `feat/bao-cp1-cp4-validation`, viết code tính 5 câu cỡ mẫu pilot D1 (kèm power thực tế khi đánh đổi MDE và tỉ lệ `mo_lai_trong_7_ngay` hiện tại) và 3 chỉ số chạy thử E1 để bàn giao số liệu cho `pilot_plan.yaml` và `chi_so.md`.
- Hỗ trợ kiểm tra tính nhất quán số liệu trên toàn bộ hồ sơ nhóm và hồ sơ duyệt chéo tại Gate 2a.

## 3. Đóng góp cụ thể

- **Thiết lập & kiểm chứng chéo CP1–CP2:** Cài đặt `src/.venv` (`pandas`, `numpy`, `scipy`, `statsmodels`, `pyyaml`) và chạy kiểm chứng `src/lab13.py` trên máy thứ hai, xác nhận qua đủ 3 phép thử A1 (`1,20 · 1,25 · 1,25`) và khớp 100% số đối chiếu A2–A4, B1–B4.
- **Hoàn thiện `report/team/bang_chi_phi.md`:**
  - Điền bảng A1–A2 (`4.472 đ/việc thành công` `[simulated]`, gấp `16,3×` hoá đơn `274,7 đ/yc`; giờ nhân viên chiếm `92,5%`; chi phí cả hệ thống `5.865 đ/yc = 0,49×` `[simulated]`).
  - Điền bảng A3 theo 4 loại (`noi_dia` `0,22×`, `hang_nang` `0,69×`, `quoc_te` `1,88×`, `doi_tac` `0,85×`) và bảng A4 cộng chi phí cố định 40 triệu đ/tháng (`4.599 đ = 0,38×` ở 45.000 yc/tháng; `5.784 đ = 0,48×` ở nửa khối lượng `[simulated]`).
  - Điền bảng độ nhạy B1 (9 kịch bản), kiểm tra tính tuyến tính B2 (`6.543 đ`, `+46,3%` `[simulated]`), xếp hạng top 3 yếu tố (làm lại · xem lại · lương nhân viên), phân tích giới hạn chạy lại B3 (tối ưu cả hệ thống là 2 lần chạy: `6.901.220 đ` `[simulated]`) và kịch bản xem lại 100% ở B4 (`11.743 đ = 0,98×` với 9 phút làm lại và `12.415 đ = 1,03×` với 15,3 phút trung bình dữ liệu; hòa vốn xem lại `<= 5,1` / `<= 4,8` phút `[simulated]`).
- **Viết code phần D1 và E1 trong `src/lab13.py`:**
  - Viết hàm `co_mau()` và `in_phan_tich_cp4_cp5(reqs)` tính đủ 5 câu cỡ mẫu D1: chia theo yêu cầu (`1.251`/nhóm), theo nhân viên `m = 75` (`DE = 2,48`, cần `84 > 40` người), giới hạn tối đa 20 nhân viên/nhóm (`1.000 < 1.251`), giới hạn tối đa 6 depot/nhóm (`300 < 1.251`), và phương án đánh đổi MDE `+6 điểm` (`n = 859`/nhóm, `m >= 299`, `DE = 6,96`).
  - Dùng `statsmodels` (`proportion_effectsize`, `NormalIndPower`) lượng hóa rủi ro đánh đổi: nếu tác động thật chỉ `+5 điểm` tại `n = 859` thì power giảm còn `0,64`.
  - Tính tỉ lệ `mo_lai_trong_7_ngay` hiện tại (`4,25%` toàn mẫu, `51/1.200`; `3,97%` trong phạm vi `noi_dia + hang_nang`, `39/982`) để nhóm đặt ngưỡng luật dừng an toàn thực tế.
  - Tính 3 chỉ số chạy thử E1 trên 1.200 yêu cầu: Chỉ số chính `82,83%` (`994/1.200`), Chỉ số dùng — tỉ lệ bỏ qua gợi ý `27,12%` (`48/177`), Chỉ số an toàn `4,25%` (`51/1.200`).

## 4. Bằng chứng

- Commit code và bảng chi phí: `8abb41f` trên nhánh `feat/bao-cp1-cp4-validation`.
- Pull Request #2 vào `main`: https://github.com/double-n-021/K5-L3B-DAY13-4NguoiDamDang-LaunchEconomics/pull/2
- Các file đóng góp trực tiếp: `report/team/bang_chi_phi.md`, `src/lab13.py` (hàm `co_mau` và `in_phan_tich_cp4_cp5`), `TEAM.md` và báo cáo cá nhân này.
- Kiểm chứng chạy thực tế: `cd src && ./.venv/bin/python lab13.py` thoát mã `0`, in `Ba phép thử đáp án biết trước: ĐẠT` và xuất đầy đủ kết quả A1–E1; rà soát từ bị cấm (theo quy tắc 5 trong `README.md`) trên `report/team/bang_chi_phi.md` trả về 0 kết quả.

## 5. Công cụ AI đã dùng

- Công cụ: Antigravity (Gemini).
- Việc đã dùng: Hỗ trợ giải thích bản chất bài học Lab 13 (Cost-of-Pass, độ nhạy, cỡ mẫu phân cụm ICC), viết hàm `co_mau()` và `in_phan_tich_cp4_cp5()` trong `src/lab13.py`, trình bày bảng `report/team/bang_chi_phi.md` và hoàn thiện báo cáo cá nhân.
- Cách tự kiểm tra kết quả: Tự chạy lệnh `cd src && ./.venv/bin/python lab13.py` trong `src/.venv` để đối chiếu từng con số đầu ra của A1–A4, B1–B4, D1 và E1 với tài liệu hướng dẫn (`docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`); kiểm tra tính tuyến tính (kịch bản giảm một nửa = nửa mức tăng kịch bản gấp đôi), rà soát đủ nhãn `simulated` và chạy `grep` xác nhận không có từ bị cấm trong báo cáo.

## 6. Tự đánh giá

- Hoàn thành đúng vai trò kiểm số (CP1–CP2) và đổi vai viết code (CP4–E1), giữ luồng làm việc sạch sẽ trên nhánh riêng `feat/bao-cp1-cp4-validation` và mở PR đầy đủ để nhóm trưởng merge mà không gây xung đột Git.
- Đảm bảo tính trung thực số liệu cho hội đồng Gate 2a: ghi rõ mọi con số `simulated`, nêu đủ các điểm bất lợi (chi phí xem lại 100% có thể vượt 12.000 đ ở B4, power tụt về 0,64 nếu đánh đổi MDE 6 điểm ở D1, và không kết luận trợ lý "đã nâng" chỉ số từ dữ liệu chạy thử chưa có đối chứng).
