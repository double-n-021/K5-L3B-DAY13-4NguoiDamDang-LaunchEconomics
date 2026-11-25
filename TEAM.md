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
|   2 | Trần Gia Bảo | | | | Người kiểm số (Data Validator — CP1, CP2; đổi vai viết code CP4) |
|   3 | Nguyễn Bảo Duy | 2A202603890 | baoduy2048@gmail.com | baoduy2048 | Người gắn nhãn 1 (Annotator 1 & Metrics Owner) |
|   4 | Bùi Đặng Nhật Nguyên | | | `double-n-021` | Người gắn nhãn 2 kiêm Giữ hồ sơ (Annotator 2 & Doc Owner) |

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

### Trần Gia Bảo - MSSV

#### Phần việc phụ trách

- Người kiểm số (Data Validator) ở CP1, CP2; phụ trách `report/team/bang_chi_phi.md`; đổi vai viết code phần D1, E1 trong `src/lab13.py` sau giờ giải lao.

#### Đóng góp cụ thể

- (Cập nhật sau khi hoàn thành từng Checkpoint)

#### Bằng chứng

- (Link commit `bang_chi_phi.md`, phép tính tay đối chiếu, commit D1/E1 trong `src/lab13.py`, file báo cáo cá nhân)

### Nguyễn Bảo Duy - MSSV

#### Phần việc phụ trách

- Người gắn nhãn 1 (Annotator 1) ở CP3 (gắn nhãn độc lập 20 ca lỗi); phụ trách `report/team/chi_so.md` (đặc tả chỉ số, event có `trace_id`, rủi ro kinh tế); theo dõi tiêu chí "Xong khi".

#### Đóng góp cụ thể

- (Cập nhật sau khi hoàn thành từng Checkpoint)

#### Bằng chứng

- (Bộ nhãn độc lập trong `bang_loi.md`, link commit `chi_so.md`, file báo cáo cá nhân)

### Bùi Đặng Nhật Nguyên - MSSV

#### Phần việc phụ trách

- Người gắn nhãn 2 kiêm Giữ hồ sơ (Annotator 2 & Doc Owner): gắn nhãn độc lập 20 ca lỗi ở CP3, tổng hợp `report/team/bang_loi.md`, `report/team/pilot_plan.yaml`, `report/team/ho_so_launch_v0.md`, `report/team/phieu_cham.md`, `report/team/group_report.md` và `TEAM.md`.

#### Đóng góp cụ thể

- (Cập nhật sau khi hoàn thành từng Checkpoint)

#### Bằng chứng

- (Bộ nhãn độc lập trong `bang_loi.md`, link commit các file hồ sơ nhóm, file báo cáo cá nhân)
