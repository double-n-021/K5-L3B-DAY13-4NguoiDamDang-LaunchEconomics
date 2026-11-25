# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: 4NguoiDamDang
- Lớp: L3B
- Thành viên: xem `TEAM.md`

## 2. Mục tiêu và cách tiếp cận

- Đánh giá tính khả thi kinh tế và lập hồ sơ Launch v0 trình hội đồng Gate 2a cho trợ lý hoàn phí LogiX-VN trên mẫu giả lập 1.200 yêu cầu (1.624 lần chạy).
- Phối hợp 4 thành viên theo mô hình Branch riêng + Pull Request vào `main`, đổi người viết code sau giờ giải lao và kiểm chứng chéo toàn bộ số liệu bằng `src/lab13.py`.

## 3. Giải pháp

- **Nhiệm vụ A–B ([bang_chi_phi.md](bang_chi_phi.md), `src/lab13.py`):** Hoàn thiện mô hình chi phí mỗi việc thành công (Cost-of-Pass), tách theo 4 loại yêu cầu, cộng chi phí cố định 40 triệu đ/tháng và phân tích độ nhạy 9 kịch bản đơn biến, cặp biến, giới hạn chạy lại và xem lại 100%.
- **Nhiệm vụ C ([bang_loi.md](bang_loi.md)):** Hai thành viên gắn nhãn độc lập 20 ca lỗi theo 5 nhóm Google PAIR (nguyên nhân gốc), đối chiếu đồng thuận và lập bảng khắc phục đủ 5 loại có event, ngưỡng và 1 vai trò phụ trách.
- **Nhiệm vụ D ([pilot_plan.yaml](pilot_plan.yaml)):** Tính cỡ mẫu hiệu dụng theo cụm ($\text{ICC} = 0,02$), chọn thiết kế chia theo nhân viên (20 + 20), kiểm tra 5 câu tách tác động và thiết lập 3 luật dừng định lượng 4 vế.
- **Nhiệm vụ E ([chi_so.md](chi_so.md), [ho_so_launch_v0.md](ho_so_launch_v0.md)):** Đặc tả 5 chỉ số, 10 event có `trace_id`, 3 rủi ro kinh tế lấy số từ bảng độ nhạy và tổng hợp hồ sơ 1 trang (7 mục) phục vụ Gate 2a.

## 4. Kết quả

- **Kinh tế & Độ nhạy [simulated]:** Chi phí mỗi việc thành công toàn mẫu là `4.472 đ` (gấp `16,3×` hóa đơn `274,7 đ/yc`; giờ nhân viên chiếm `92,5%`). Trên phạm vi `noi_dia + hang_nang`, chi phí kèm cố định 40 triệu đ/tháng là `4.599 đ = 0,38×` so với `12.000 đ` (ở 45.000 yc/tháng). Ba yếu tố nhạy nhất là làm lại (`+51,8%`), xem lại (`+40,7%`) và lương nhân viên (`+23,1%`); nếu xem lại 100%, chi phí lên `11.743–12.415 đ` (`0,98–1,03×`).
- **Lỗi & Chỉ số chạy thử:** Đồng thuận gắn nhãn đạt `20/20 = 100%`. Chỉ số trong đợt chạy thử (chưa có đối chứng): đóng 24h & không mở lại 7 ngày `82,83%`, bỏ qua gợi ý `27,12%`, mở lại trong 7 ngày `4,25%` (`3,97%` trong phạm vi).
- **Thiết kế Pilot & Đề xuất ([ho_so_launch_v0.md](ho_so_launch_v0.md)):** Chia 20 + 20 nhân viên, MDE `+6 điểm` (`n = 859`, `m >= 299`, `DE = 6,96`; chấp nhận `power = 0,64` ở mức `+5 điểm`). Nhóm đề xuất **Go có điều kiện** kèm 4 điều kiện có ngưỡng, người phụ trách và ngày kiểm tra.
- **Kết quả duyệt chéo Gate 2a:** *(Cập nhật sau phiên chấm chéo 17:00–17:45 cùng [phieu_cham.md](phieu_cham.md)).*

## 5. Khó khăn và cách xử lý

- Phát sinh xung đột nhỏ ở `TEAM.md` và `bang_loi.md` khi nhiều thành viên cập nhật song song; nhóm đã giữ nguyên bảng nhãn 20/20 hoàn chỉnh và hợp nhất đủ thông tin 4 thành viên qua quy trình PR.
- Thiếu thư viện `statsmodels` trên một máy ở đầu giờ chiều; đã cài bổ sung `statsmodels` và chạy kiểm chứng lại toàn bộ `src/lab13.py` trên máy thứ hai.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md` và 4 báo cáo cá nhân trong `report/team/`.

## 7. Hạn chế và hướng cải thiện

- Thời gian xem lại và làm lại hiện là dữ liệu `simulated`; cần thu thập đầy đủ 10 event có `trace_id` ngay từ tuần 1 của pilot để thay thế hoàn toàn số giả lập.
- Giới hạn 40 nhân viên làm `power` ở mức chênh `+5 điểm` chỉ còn `0,64`; cần theo dõi sát chỉ số an toàn theo ngày và chỉ kết luận tại ngày quyết định `2027-01-05`.

## 8. Tài liệu tham khảo

- Tài liệu chính thức Lab 13: `README.md`, `docs/du_lieu_va_cong_thuc.md`, `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`.
- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models* (arXiv:2504.13359); Google PAIR, *People + AI Guidebook* ("Errors + Graceful Failure"); `statsmodels.stats.power.NormalIndPower`.
