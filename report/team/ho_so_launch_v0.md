# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: 4NguoiDamDang · Lớp: L3B

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | `4.472 đ` [simulated] (16,3× hóa đơn 274,7 đ/yc). Phạm vi `noi_dia + hang_nang`: `3.414 đ` + cố định 40 tr/tháng = `4.599 đ` [simulated] (45.000 yc) / `5.784 đ` (nửa khối lượng) | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | 1. Làm lại (+51,8%, lên `6.787 đ`) · 2. Xem lại (+40,7%, lên `6.292 đ`) · 3. Lương +25% (+23,1%, lên `5.506 đ`) [simulated]; xem lại 100% lên `11.743 đ` (hoặc `12.415 đ` với 15,3 phút TB) | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Cả hệ thống `5.865 đ/yc` (0,49× của `12.000 đ`); phạm vi `noi_dia + hang_nang` + cố định = `4.599 đ` (0,38×) [simulated]. Loại `quoc_te` (`22.515 đ`, 1,88×) và `doi_tac` (`10.215 đ`, 0,85×) | Giả lập | Giám đốc tài chính |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Chạy thử (chưa đối chứng): chính `82,83%` (994/1.200), bỏ qua `27,12%` (48/177), mở lại 7 ngày `4,25%` (`3,97%` phạm vi); 2 chỉ số đề xuất và 10 event có `trace_id` (`chi_so.md`) | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 5 · Bảng lỗi và cách khắc phục | 20/20 ca đồng thuận (100%); đủ 5 loại PAIR kèm event, ngưỡng và 1 vai trò phụ trách (`bang_loi.md`) | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 6 · Pilot plan | 20 + 20 nhân viên (DE=6,96, n=859, MDE +6 điểm; power 0,64 ở +5 điểm); 3 luật dừng định lượng (`pilot_plan.yaml`) | Xong, có bằng chứng | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | Làm lại ×2 lên `6.787 đ` (+51,8%); xem lại 100% lên `11.743 đ` (0,98×) hoặc `12.415 đ` (1,03× với 15,3 phút TB); cố định 40 tr/tháng lên `+2.370 đ/việc` ở nửa khối lượng [simulated] (`chi_so.md`) | Giả lập | PM trợ lý hoàn phí |

**Đề xuất: Go có điều kiện** (áp dụng cho pilot phạm vi `noi_dia + hang_nang`; loại `quoc_te` vì `22.515 đ = 1,88×` và `doi_tac` vì `10.215 đ = 0,85×` kèm điều khoản riêng):

1. Khóa lỗi hoàn trùng và lỗi báo nhầm sổ cái (Ca 20, Ca 7): bổ sung `idempotency_key`, chặn gửi tin "đã hoàn" khi sổ cái chưa trả `ok` và bật đối soát theo giờ (ngưỡng `> 0 ca lệch/giờ`) — **Kỹ sư trưởng agent** — kiểm tra trước **2026-12-01**.
2. Ký chấp nhận đánh đổi cỡ mẫu: chia 20 + 20 nhân viên, MDE `+6 điểm` (`n = 859`, `m >= 299`), chấp nhận `power` còn `0,64` nếu tác động thật là `+5 điểm` — **Giám đốc vận hành LogiX-VN** — kiểm tra trước **2026-12-01**.
3. Bật đủ 10 event có `trace_id`, thay toàn bộ phút `simulated` bằng thời gian đo thật sau tuần 1 (bước 10%), và bật kiểm toán mẫu 100 đơn/tuần (ngưỡng `> 1%`) bắt lỗi ngầm (Ca 17) — **Kỹ sư trưởng agent** (event) & **Kế toán trưởng** (kiểm toán) — kiểm tra **2026-12-08**.
4. Áp dụng lộ trình giảm xem lại theo bậc từ bước 25% (đưa tỉ lệ xem lại `< 50%` khi tỉ lệ `sua + bo < 15%`), vì xem lại 100% không tiết kiệm (`11.743–12.415 đ = 0,98–1,03×` [simulated]) — **Trưởng nhóm CSKH** — kiểm tra **2026-12-15**.
