# Báo cáo cá nhân — Nguyễn Bảo Duy

## 1. Thông tin thành viên

- Họ tên: Nguyễn Bảo Duy
- MSSV: 2A202603890
- Email: baoduy2048@gmail.com
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): người gắn nhãn 1

## 2. Phần việc phụ trách

- Người gắn nhãn 1 (Annotator 1) ở CP3: gắn nhãn độc lập 20 ca lỗi trong 8 phút, không trao đổi với người gắn nhãn 2.
- Phụ trách `report/team/chi_so.md`: đặc tả 3 chỉ số, 2 chỉ số đề xuất, danh sách event có `trace_id`, các dòng rủi ro kinh tế.
- Theo dõi tiêu chí "Xong khi" của từng Checkpoint và rà soát ngưỡng luật dừng trong `pilot_plan.yaml`.

## 3. Đóng góp cụ thể

- Viết `report/team/chi_so.md`:
  - E1: 3 chỉ số tính thử (chính 82,83%, dùng 27,12%, an toàn 4,25%) và 2 chỉ số đề xuất (một dùng, một an toàn).
  - Danh sách 10 event, mỗi event có `trace_id` và chỉ ra chỉ số nào dùng event đó.
  - E2: 3 dòng rủi ro kinh tế, lấy số từ bảng độ nhạy và ghi nhãn [simulated].
- Kiểm tra lại các số trong `chi_so.md` bằng cách tính trực tiếp từ `src/logix_requests.csv` và `src/logix_runs.csv`. Các số chỉ số, tỉ lệ làm lại (4,89%), token + tool (224.513 đ), số phút làm lại trung bình (15,3 phút/ca) đều khớp.
- Kiểm tra `src/lab13.py` trên `main` và nhánh hiện tại: thời điểm kiểm tra, file vẫn là khung chưa viết (4 hàm `NotImplementedError`), nên phép thử A1 chưa chạy được. Nêu vấn đề này để nhóm kịp phân công.
- Gắn nhãn độc lập 20 ca lỗi ở CP3: [điền sau khi làm: số ca trùng với người gắn nhãn 2, tỉ lệ đồng thuận, các ca lệch và quy tắc phân biệt].

## 4. Bằng chứng

- `report/team/chi_so.md`
- Bộ nhãn độc lập của người gắn nhãn 1 trong `report/team/bang_loi.md`, cột "Nhãn người 1"

## 5. Công cụ AI đã dùng

- Claude Code (trợ lý AI): tính lại các chỉ số và số liệu rủi ro từ CSV, soạn nháp `chi_so.md`, kiểm tra việc viết `lab13.py`.
- CP3 (gắn nhãn 20 ca): không dùng AI để tạo nhãn, đúng quy định trong `RULES.md`.

## 6. Tự đánh giá

- Điểm làm tốt: [điền].
- Điểm cần cải thiện: [điền].

