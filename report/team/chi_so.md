# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

Số tính bằng `src/lab13.py` (mục E1, A4, B1, B4, D1 trong output), trừ tỉ lệ làm lại ở E2 đếm từ CSV. Mọi con số tính từ cột `_simulated` ghi nhãn **simulated**.

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | 82,83% (994/1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | 27,12% (48/177) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | 4,25% (51/1.200); trong phạm vi noi_dia + hang_nang: 3,97% (39/982) |
| Dùng (nhóm đề xuất) | % yêu cầu của nhóm can thiệp được mở bằng trợ lý | `agent_suggestion_shown` theo `arm`, chia số yêu cầu của nhóm can thiệp | Không cần tính |
| An toàn (nhóm đề xuất) | % đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần | `audit_sample_checked`: `so_tien_da_hoan` khác `so_tien_dung`, chia số đơn được kiểm | Không cần tính |

Viết "chỉ số trong đợt chạy thử là 82,83%", không viết "trợ lý đã nâng chỉ số từ 0,70": đợt chạy thử không có nhóm đối chứng.

Hai chỉ số đề xuất bắt được lỗi mà chỉ số chính không thấy: chỉ số dùng theo nhóm đo mức sử dụng thật của nhóm can thiệp; chỉ số an toàn theo kiểm tra mẫu bắt được đơn sai tiền mà khách không mở lại.

## Danh sách event

Mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm | Chỉ số dùng |
| --- | --- | --- | --- | --- |
| refund_request_created | App khách | request_id, loai, so_tien, arm, trace_id | Khi khách gửi | Mẫu số của mọi chỉ số |
| agent_run_completed | Agent | attempt, tokens_in, tokens_out, tool_calls, status, trace_id | Sau mỗi lần chạy, kể cả lỗi | Chi phí (bảng A2) |
| agent_suggestion_shown | Giao diện nhân viên | staff_id, so_tien_de_xuat, arm, trace_id | Khi gợi ý hiện ra | Dùng (nhóm đề xuất) |
| staff_review_decision | Nhân viên | giu / sua / bo, phut_xem_lai (đo thật), trace_id | Khi bấm gửi, sửa hoặc bỏ | Dùng (tỉ lệ bỏ qua) |
| staff_rework_completed | Nhân viên | phut_lam_lai, ly_do, trace_id | Khi làm lại xong | Chi phí làm lại |
| refund_ledger_write | Dịch vụ sổ cái | idempotency_key, so_tien, ket_qua, trace_id | Khi ghi sổ | An toàn (không trùng, đúng tiền) |
| handoff_to_staff | Agent | reason, tom_tat, trace_id | Khi chuyển nhân viên | Theo dõi ca chuyển nhân viên |
| ticket_closed | Hệ thống ticket | closed_at, trace_id | Khi đóng | Chính |
| ticket_reopened | Khách | reopened_at, reason, trace_id | Khi mở lại | Chính, An toàn |
| audit_sample_checked | Kế toán | so_tien_da_hoan, so_tien_dung, trace_id | Hằng tuần | An toàn (nhóm đề xuất) |

**Kiểm tra chéo:**
- Chính: `ticket_closed` và `ticket_reopened` (7 ngày), mẫu số từ `refund_request_created`.
- Dùng: `staff_review_decision`.
- An toàn: `ticket_reopened`, mẫu số từ `refund_request_created`.
- Dùng và an toàn đề xuất: `agent_suggestion_shown`, `audit_sample_checked`.

Cả ba chỉ số chính và hai chỉ số đề xuất đều tính được từ danh sách event khi các event này được bật trong pilot.

## E2 · Rủi ro kinh tế

Số lấy từ output `lab13.py`, mục B1, B4 và A4 (cùng số với `bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | +51,8%, lên 6.787 đ/việc thành công [simulated] | Tỉ lệ làm lại theo tuần > 7%. Đợt chạy thử trong phạm vi noi_dia + hang_nang: 4,89% (48/982, đếm `ket_qua` = `lam_lai` từ CSV) | Thu hẹp về noi_dia, rà 20 trace làm lại | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | 11.743 đ = 0,98× so với 12.000 đ (9 phút/ca); 12.415 đ = 1,03× nếu dùng 15,3 phút/ca từ dữ liệu [simulated] | % yêu cầu được xem lại còn > 50% sau bước 0,25 | Giảm xem lại theo bậc khi tỉ lệ sửa + bỏ < 15% | Trưởng nhóm CSKH |
| Khối lượng thấp hơn dự kiến | Chi phí cố định 40 triệu/tháng: +1.185 đ/việc ở 45.000 yêu cầu/tháng, tổng 4.599 đ = 0,38× [simulated]; +2.370 đ/việc nếu khối lượng còn một nửa, tổng 5.784 đ = 0,48× [simulated] | Số việc thành công mỗi tuần < 50% kế hoạch | Không mở rộng pilot; xem lại hợp đồng chi phí cố định | PM trợ lý hoàn phí |
