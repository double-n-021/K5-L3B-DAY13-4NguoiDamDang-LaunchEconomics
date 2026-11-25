# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Nguyễn Bảo Duy (gắn độc lập trên nhánh `baoduy`) · Người gắn nhãn 2: Bùi Đặng Nhật Nguyên (gắn độc lập trên nhánh `feat/nguyen-cp3-cp5-docs`, trong 8 phút, không trao đổi trước khi so)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 20 / 20 = 100%

## Quy tắc phân biệt cho các ca không trùng

Không có ca bất đồng (0/20 ca lệch sau hai lượt gắn độc lập). Nhóm chốt 5 quy tắc phân biệt theo nguyên nhân gốc cho các ca dễ nhầm:

- **Ca 6, 9 là Do người dùng, không phải Hệ thống:** Gốc lỗi do khách chọn sai mục hoặc nhập sai mã; việc trợ lý chưa tự đối chiếu/gợi ý nằm ở cột khắc phục.
- **Ca 13 là Giới hạn hệ thống, không phải Hệ thống:** Yêu cầu ngoài phạm vi sản phẩm (bảo hiểm đối tác) là giới hạn; việc trợ lý trả lời chưa rõ được xử lý ở bước khắc phục.
- **Ca 8, 15 là Hệ thống, không phải Ngầm:** Lỗi sai so với chính sách đã lộ ra rõ trong trích dẫn gửi khách (Ca 8) hoặc bị nhân viên kiểm tra phát hiện trước khi gửi (Ca 15).
- **Ca 18 là Ngữ cảnh, không phải Hệ thống:** Số tiền hoàn (15.000 đ = 50% của 30.000 đ) đúng chính sách; xung đột phát sinh do giả định thiết kế thiếu dòng diễn giải cách tính cho khách.
- **Ca 12 là Ngầm, không phải Hệ thống:** Kết quả trả cho khách vẫn đúng nhưng chi phí token bị đội gấp 3 lần suốt 3 tuần không ai phát hiện; lỗi ngầm bao gồm cả sai lệch âm thầm về chi phí.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed` gắn `trace_id`; cảnh báo khi tỉ lệ lỗi định dạng mã > 2% tổng yêu cầu/ngày (đo theo ngày) | *Prevention:* Nhận diện tự động mã sàn TMĐT và gợi ý đối chiếu sang mã vận đơn trên giao diện nhập. *Mitigation:* Khi không tra được, trả hướng dẫn tìm mã kèm ảnh minh họa thay vì chỉ báo không hợp lệ | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát theo giờ giữa sự kiện tin nhắn "đã hoàn tiền" và event `refund_ledger_write` có cùng `trace_id`; ngưỡng kích cảnh báo > 0 ca lệch/giờ | *Prevention:* Chặn cứng trạng thái báo "đã hoàn", chỉ gửi thông báo khi sổ cái trả `ok`. *Mitigation:* Khi API 503 quá 3 lần thử, báo "đang xử lý" và phát `handoff_to_staff` kèm `trace_id` để nhân viên xử lý ngay | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Tỉ lệ `ticket_reopened` có lý do thắc mắc số tiền nhưng kiểm tra đối chiếu thấy đúng chính sách; cảnh báo khi vượt 1,5%/tuần | *Prevention:* Cập nhật mẫu phản hồi bắt buộc hiển thị công thức tính rõ ràng (ví dụ `30.000 đ × 50% = 15.000 đ`). *Mitigation:* Khi khách mở lại với lý do này, hiển thị ngay chi tiết phép tính và dẫn link điều khoản để giảm thời gian giải thích | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Event `handoff_to_staff` với `reason = thieu_du_lieu_hang_ngoai`, theo dõi theo `loai` mỗi tuần; cảnh báo nếu > 5% trong phạm vi pilot | *Prevention:* Đưa loại `quoc_te` ra khỏi phạm vi pilot và định tuyến thẳng sang nhân viên ngay từ đầu. *Mitigation:* Nếu phát sinh ca thiếu dữ liệu chặng ngoài, thông báo rõ giới hạn dữ liệu cho khách và chuyển nhân viên kèm bản tóm tắt đầy đủ | PM trợ lý hoàn phí |
| 17 | Ngầm | Kiểm tra mẫu kiểm toán định kỳ (`audit_sample_checked`) 100 đơn ngẫu nhiên/tuần đối chiếu với bảng giá hiện hành; ngưỡng cảnh báo > 1% đơn lệch số tiền | *Prevention:* Tự động xóa bộ nhớ đệm (cache invalidation) mỗi khi cập nhật bảng giá mới và ghi bắt buộc `pricing_version` vào mọi `trace_id`. *Mitigation:* Truy vết danh sách đơn dùng phiên bản bảng giá cũ để hoàn bổ sung phần chênh lệch và thông báo cho khách bị ảnh hưởng | Kế toán trưởng |
