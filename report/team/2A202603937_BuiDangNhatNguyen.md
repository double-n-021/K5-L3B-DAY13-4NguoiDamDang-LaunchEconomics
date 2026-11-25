# Báo cáo cá nhân — Bùi Đặng Nhật Nguyên - 2A202603937

## 1. Thông tin thành viên

- Họ tên: Bùi Đặng Nhật Nguyên
- MSSV: 2A202603937
- Email: nhatnguyenmtvt@gmail.com
- GitHub: `double-n-021`
- Vai trong nhóm: Người gắn nhãn 2 kiêm Giữ hồ sơ (Annotator 2 & Doc Owner)

## 2. Phần việc phụ trách

- Thiết lập điều phối nhóm (`TEAM.md`, `PHAN_CONG_NHOM.md`) theo quy trình Branch riêng + Pull Request vào `main`.
- Chạy kiểm chứng `src/lab13.py` trên máy thứ 2 sau khi hợp nhất PR #1 của Đỗ Hoàng Vũ.
- Gắn nhãn độc lập 20 ca lỗi theo 5 loại Google PAIR, đối chiếu đồng thuận với Nguyễn Bảo Duy và hoàn thiện `report/team/bang_loi.md`.
- Tổng hợp `report/team/pilot_plan.yaml`, `report/team/ho_so_launch_v0.md`, `report/team/phieu_cham.md` và `report/team/group_report.md`.

## 3. Đóng góp cụ thể

- Tạo và đồng bộ nhánh `feat/nguyen-cp3-cp5-docs`; điền thông tin 4 thành viên vào `TEAM.md` và chuẩn hóa quy trình Branch/PR trong `PHAN_CONG_NHOM.md`.
- Chạy kiểm chứng toàn bộ `src/lab13.py` (A1–E1, gồm `statsmodels`) trên máy thứ 2 và cập nhật số liệu Mục 1–3, 5–6 (kèm nhãn `simulated`) vào `report/team/ho_so_launch_v0.md`.
- Gắn nhãn độc lập 20/20 ca lỗi theo Google PAIR, đối chiếu với Nguyễn Bảo Duy (đồng thuận 20/20 = 100%) và hoàn thiện `report/team/bang_loi.md` với 5 quy tắc phân biệt và bảng khắc phục 5 loại lỗi.
- Hoàn thiện toàn bộ `report/team/pilot_plan.yaml` (kết quả D1, D2, công khai đánh đổi MDE +6 điểm / power 0,64, 3 luật dừng định lượng 4 vế và `simulated_inputs`), vượt kiểm tra `yaml.safe_load`.
- Hợp nhất đóng góp của Trần Gia Bảo và Nguyễn Bảo Duy vào `main`, hoàn thiện trọn vẹn `report/team/ho_so_launch_v0.md` (7/7 mục + đề xuất **Go có điều kiện** kèm 4 điều kiện định lượng) và `report/team/group_report.md` trước mốc 17:00.
- *(Sẽ bổ sung phần duyệt chéo Gate 2a vào `report/team/phieu_cham.md` sau 17:00)*

## 4. Bằng chứng

- Commit `044da17` (`TEAM.md`), `4996cd8` (`PHAN_CONG_NHOM.md`), PR #3 (`178948e`), merge `3dc366b` trên nhánh `main`.
- Nhánh `feat/nguyen-cp3-cp5-docs`: `report/team/bang_loi.md`, `report/team/pilot_plan.yaml`, `report/team/ho_so_launch_v0.md`, `report/team/group_report.md`, `report/team/2A202603937_BuiDangNhatNguyen.md`.
- Kết quả chạy kiểm chứng `src/lab13.py` trên máy cá nhân: 3 phép thử A1 đạt (`1,20 · 1,25 · 1,25`), CPS = `4.472 đ` [simulated], mở lại 7 ngày = `4,25%` (toàn mẫu) / `3,97%` (trong phạm vi), `yaml.safe_load` hợp lệ.

## 5. Công cụ AI đã dùng

- Sử dụng trợ lý AI để rà soát cấu trúc repo, giải thích bản chất các công thức kinh tế/thống kê, đối chiếu kết quả chạy `src/lab13.py` và hỗ trợ giải thích phân loại lỗi Google PAIR theo nguyên nhân gốc.
- Cách tự kiểm tra: đối chiếu trực tiếp với `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`, `docs/Ngay13_Lab13_De_bai_hoc_vien.docx` và chạy kiểm chứng độc lập `python lab13.py` trên máy cá nhân.

## 6. Tự đánh giá

- Đang bám sát tiến độ theo từng Checkpoint, giữ đúng nguyên tắc gắn nhãn độc lập trước khi so chéo với thành viên gắn nhãn 1 và gắn nhãn `simulated` đầy đủ ở các số liệu giả lập.
