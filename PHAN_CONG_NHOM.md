# Phân công công việc nhóm 4NguoiDamDang — Lab 13 (Gate 2a)

Tài liệu điều phối nội bộ cho 4 thành viên thực hiện **Lab 13: Định giá Agent và lập kế hoạch Pilot (LogiX-VN, Gate 2a)** trong 4 giờ tại lớp (14:00–18:00) và hoàn thiện nộp bài trước **23h59 GMT+7**.

## 1. Thông tin chung và thiết lập môi trường

- **Nhóm:** `4NguoiDamDang` · **Lớp:** `L3B`
- **Repository nhóm:** `https://github.com/double-n-021/K5-L3B-DAY13-4NguoiDamDang-LaunchEconomics`
- **Nhánh làm việc & nộp bài:** `main`

### Lệnh clone và cài đặt môi trường (chạy trong `src/`)

Yêu cầu Python 3.10 trở lên. Lab chạy offline, không dùng API key.

**Windows PowerShell:**

```powershell
git clone https://github.com/double-n-021/K5-L3B-DAY13-4NguoiDamDang-LaunchEconomics.git
cd K5-L3B-DAY13-4NguoiDamDang-LaunchEconomics\src
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -c "import pandas, numpy, scipy, statsmodels, yaml; print('san sang')"
```

**macOS / Linux:**

```bash
git clone https://github.com/double-n-021/K5-L3B-DAY13-4NguoiDamDang-LaunchEconomics.git
cd K5-L3B-DAY13-4NguoiDamDang-LaunchEconomics/src
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -c "import pandas, numpy, scipy, statsmodels, yaml; print('san sang')"
```

Lưu ý: Từng thành viên nhớ tự điền bổ sung **MSSV, Email, tài khoản GitHub** của mình vào bảng thành viên trong [TEAM.md](TEAM.md).

---

## 2. Phân công vai trò và file sở hữu chính

Nguyên tắc: mỗi file tại một thời điểm chỉ có **một người chỉnh sửa chính** để cả 4 người chạy song song mà không bị xung đột Git.

| Thành viên | Vai trò chính | File sở hữu chính | Hỗ trợ chéo |
|---|---|---|---|
| **Đỗ Hoàng Vũ** | Người viết code (Developer — CP1, CP2) | `src/lab13.py` (giai đoạn CP1, CP2) | Kiểm tra D2 & kỹ thuật rollback (CP4); trả lời kỹ thuật khi bảo vệ Gate 2a |
| **Trần Gia Bảo** | Người kiểm số (Data Validator) & Code CP4 | `report/team/bang_chi_phi.md`, `src/lab13.py` (sau giải lao: D1, E1) | Tính tay đối chiếu A2/A3/B1; kiểm soát tính nhất quán số liệu trên toàn bộ hồ sơ |
| **Nguyễn Bảo Duy** | Người gắn nhãn 1 (Annotator 1 & Metrics Owner) | Bộ nhãn 1 trong `report/team/bang_loi.md`, `report/team/chi_so.md` | Theo dõi tiêu chí "Xong khi" từng Checkpoint; rà soát ngưỡng Stop Rules |
| **Bùi Đặng Nhật Nguyên** | Người gắn nhãn 2 kiêm Giữ hồ sơ (Annotator 2 & Doc Owner) | Bộ nhãn 2 trong `report/team/bang_loi.md`, `report/team/pilot_plan.yaml`, `report/team/ho_so_launch_v0.md`, `report/team/phieu_cham.md`, `report/team/group_report.md` | Tổng hợp hồ sơ Launch v0 dần từ CP1; chốt commit & kiểm tra checklist nộp bài |

---

## 3. Lịch trình thực hiện theo Checkpoint (14:00 – 18:00)

| Giờ | Checkpoint | Đỗ Hoàng Vũ (Dev -> Hỗ trợ CP4) | Trần Gia Bảo (Kiểm số -> Dev CP4) | Nguyễn Bảo Duy (Nhãn 1 & Metrics) | Bùi Đặng Nhật Nguyên (Nhãn 2 & Hồ sơ) |
|---|---|---|---|---|---|
| **14:00 – 14:10** | **Chuẩn bị** | Clone repo, cài `src/.venv`, chạy thử `lab13.py` | Cài môi trường trên máy thứ 2 để sẵn sàng chạy kiểm chéo | Mở `CHECKPOINTS.md` và `RUBRIC.md`, nắm điều kiện "Xong khi" | Mở sẵn khung `ho_so_launch_v0.md`, nhắc mọi người điền `TEAM.md` |
| **14:10 – 14:53** | **CP1 · A: Mô hình chi phí** | Code A1 (3 test `1,20 · 1,25 · 1,25`), `mo_hinh` (A2), A3 (4 loại), A4 (chi phí cố định) | Tính tay 1 ca để đối chiếu; nhận output từ Vũ để điền bảng A1–A4 vào `bang_chi_phi.md` | Kiểm tra sai số <= 2% và xác nhận mọi số từ cột `_simulated` đều có nhãn `simulated` | Điền ngay **Mục 1** (Chi phí mỗi việc thành công) và **Mục 3** (So với 12.000 đ) vào `ho_so_launch_v0.md` |
| **14:53 – 15:20** | **CP2 · B: Bảng độ nhạy** | Code B1 (9 kịch bản), B2 (cặp), B3 (chi phí cả hệ thống 1/2/3 lần), B4 (xem lại 100%) | Kiểm tra tính tuyến tính B1/B2; hoàn thiện bảng B1–B4 và câu trả lời (<= 3 dòng, có số) trong `bang_chi_phi.md` | Đọc trước định nghĩa 5 loại lỗi Google PAIR trong `docs/` để chuẩn bị CP3 | Điền **Mục 2** (Top 3 yếu tố nhạy nhất) vào `ho_so_launch_v0.md`; đọc trước khung 5 loại lỗi |
| **15:20 – 15:35** | **Giải lao** | Push nhánh `feat/vu-cp1-cp2-cost`, tạo PR vào `main` và merge để bàn giao cho Gia Bảo | Kéo `origin/main` về nhánh `feat/bao-cp1-cp4-validation`, sẵn sàng tiếp quản `src/lab13.py` | Nghỉ giải lao | Nghỉ giải lao |
| **15:35 – 16:08** | **CP3 · C: 20 ca lỗi** | Hỗ trợ chốt định dạng `bang_chi_phi.md`; cùng nhóm làm bảng khắc phục 5 loại sau khi so nhãn | Hỗ trợ kiểm tra số B3/B4 và chuẩn bị công thức D1; cùng nhóm viết quy tắc phân biệt | **8 phút đầu:** Ngồi tách riêng, gắn nhãn độc lập 20 ca lỗi (không trao đổi). Sau đó so nhãn với Nguyên, thống nhất và phụ trách phần phát hiện đo được | **8 phút đầu:** Ngồi tách riêng, gắn nhãn độc lập 20 ca lỗi (không trao đổi). Sau đó so nhãn với Duy, ghi quy tắc ca lệch, điền `bang_loi.md` và **Mục 5** của `ho_so_launch_v0.md` |
| **16:08 – 16:36** | **CP4 · D: Pilot Plan** | Trả lời 5 câu D2 (tách được tác động) và kiểm tra phương án rollback kỹ thuật | **Đổi vai viết code:** Code 5 câu D1 (cỡ mẫu, DE, mẫu hiệu dụng) và tính tỉ lệ `mo_lai_trong_7_ngay` hiện tại trong `src/lab13.py` | Kiểm tra chéo 3 luật dừng (An toàn, Chi phí, Sử dụng) đủ 4 vế `NẾU – TRONG – THÌ – KHÔNG THÌ` | Điền hoàn chỉnh `pilot_plan.yaml` (comment D1/D2, 0 dấu `?`), test `yaml.safe_load`; điền **Mục 6** của `ho_so_launch_v0.md` |
| **16:36 – 17:00** | **CP5 · E: Chỉ số & Hồ sơ v0** | Chạy toàn bộ `src/lab13.py` từ đầu đến cuối kiểm tra không lỗi | Tính 3 chỉ số E1 trong `src/lab13.py`; rà soát đối chiếu số liệu toàn hồ sơ | Hoàn thiện `chi_so.md`: 3 chỉ số tính thử + 2 chỉ số đề xuất + >= 6 event có `trace_id` + >= 2 dòng rủi ro kinh tế | Hoàn thiện **Mục 4**, **Mục 7** và **Đề xuất cuối (Go / Go có điều kiện / No-go)** trong `ho_so_launch_v0.md` trước **17:00** |
| **17:00 – 17:45** | **Gate 2a: Duyệt chéo** | Trả lời câu hỏi kỹ thuật và mô hình chi phí từ hội đồng | Kiểm tra tính nhất quán số liệu trên hồ sơ nhóm bạn (nhóm n + 1) | Kiểm tra event, chỉ số, luật dừng trên hồ sơ nhóm bạn | Trình bày hồ sơ nhóm (1 phút); tổng hợp điểm và lý do có số vào `phieu_cham.md` |
| **17:45 – 18:00** | **Đóng gói & Nộp** | Tạo file `report/team/MSSV_HoTen.md`, commit & push, nộp link lên LMS | Tạo file `report/team/MSSV_HoTen.md`, chạy test lại `lab13.py` trên máy mình, nộp link lên LMS | Tạo file `report/team/MSSV_HoTen.md`, rà checklist `SUBMISSION.md`, nộp link lên LMS | Hoàn thiện `group_report.md`, `TEAM.md`, tạo file `report/team/MSSV_HoTen.md`, chốt commit cuối và xác nhận 4/4 người nộp LMS |

---

## 4. Hướng dẫn chi tiết cho từng thành viên

### 4.1. Đỗ Hoàng Vũ — Người viết code (CP1, CP2)

1. Setup môi trường trong `src/`, xác nhận `python -c "import pandas, numpy, scipy, statsmodels, yaml; print('san sang')"`.
2. **CP1:** Viết 3 hàm A1 trong `src/lab13.py` (`so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`) cho tới khi `kiem_tra_dap_an_biet_truoc()` in `ĐẠT` (`1,20 · 1,25 · 1,25`). Sau đó viết `mo_hinh()` (A2), tách theo `loai` (A3) và cộng chi phí cố định 40 triệu đ/tháng (A4).
3. **CP2:** Gọi lại `mo_hinh()` để chạy 9 kịch bản B1, kịch bản cặp B2, so sánh giới hạn 1/2/3 lần chạy kèm chi phí cả hệ thống (B3) và kịch bản xem lại 100% cho `noi_dia + hang_nang` (B4).
4. **15:20 (Giải lao):** Push nhánh `feat/vu-cp1-cp2-cost`, mở Pull Request vào `main` và merge để Trần Gia Bảo kéo về tiếp quản phần code CP4.
5. **CP4–CP5:** Hỗ trợ phân tích 5 câu hỏi tách tác động (D2), kiểm tra tính khả thi kỹ thuật của cơ chế rollback 30 phút và chạy kiểm tra cuối toàn bộ `src/lab13.py`.

### 4.2. Trần Gia Bảo — Người kiểm số & Code CP4

1. Cài môi trường Python trên máy thứ hai ngay đầu buổi để đảm bảo yêu cầu chạy tái lập trên ít nhất 2 máy.
2. **CP1–CP2:** Tính tay kiểm chứng một trường hợp nhỏ và đối chiếu từng dòng kết quả Vũ xuất ra (sai số <= 2%). Điền đầy đủ bảng A1–A4, B1–B4 và câu trả lời (<= 3 dòng, có số) vào `report/team/bang_chi_phi.md`. Kiểm tra kỹ tính tuyến tính ở B1/B2 và nhắc gắn nhãn `simulated`.
3. **15:35 (Sau giải lao — đổi vai viết code):** Đồng bộ `main` mới nhất (`git fetch origin && git merge origin/main`) vào nhánh `feat/bao-cp1-cp4-validation`, tiếp quản `src/lab13.py` để viết code tính 5 câu D1 (cỡ mẫu, Design Effect, Effective Sample Size, mức chênh 6 điểm), tỉ lệ `mo_lai_trong_7_ngay` hiện tại, và 3 chỉ số E1.
4. **CP5 & Gate 2a:** Đối chiếu mọi con số giữa `bang_chi_phi.md`, `pilot_plan.yaml`, `chi_so.md` và `ho_so_launch_v0.md`. Khi chấm chéo, chịu trách nhiệm kiểm tra tính khớp số liệu của nhóm được chấm.

### 4.3. Nguyễn Bảo Duy — Người gắn nhãn 1 & Metrics Owner

1. **CP1–CP2:** Theo dõi điều kiện "Xong khi" trong `CHECKPOINTS.md` để đảm bảo nhóm không sót dòng hay thiếu nhãn `simulated`. Đọc trước định nghĩa 5 loại lỗi Google PAIR trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx` (mục "Hai mươi ca lỗi").
2. **CP3 (15:35):** Trong **8 phút đầu**, ngồi tách riêng khỏi Nguyên và gắn nhãn độc lập 20 ca lỗi theo nguyên nhân gốc (không trao đổi, không xem đáp án trước). Sau khi so nhãn với Nguyên:
   - Nếu đồng thuận >= 16/20 (80%): thống nhất các ca lệch và ghi quy tắc phân biệt.
   - Nếu dưới 80%: cùng viết lại định nghĩa trước khi đi tiếp (tuyệt đối không sửa nhãn ban đầu).
   - Cùng hoàn thiện bảng khắc phục 5 ca (đủ 5 loại), đảm bảo cách phát hiện đo được (event, ngưỡng, tần suất) và chỉ định 1 vai trò phụ trách.
3. **CP4:** Soát lại 3 luật dừng trong `pilot_plan.yaml` (An toàn, Chi phí, Sử dụng) xem đã đủ 4 vế `NẾU – TRONG – THÌ – KHÔNG THÌ` và có ngưỡng định lượng chưa.
4. **CP5:** Chủ trì `report/team/chi_so.md`: 3 chỉ số tính thử + 2 chỉ số đề xuất (1 dùng, 1 an toàn) + ít nhất 6 event có `trace_id` + kiểm tra chéo event-chỉ số + ít nhất 2 rủi ro kinh tế lấy số trực tiếp từ bảng độ nhạy.

### 4.4. Bùi Đặng Nhật Nguyên — Người gắn nhãn 2 kiêm Giữ hồ sơ

1. **Đầu buổi:** Cập nhật thông tin nhóm trong `TEAM.md`; mở sẵn `report/team/ho_so_launch_v0.md` để cập nhật cuốn chiếu ngay sau mỗi Checkpoint (không đợi đến 16:36 mới viết).
2. **CP1–CP2:** Cập nhật Mục 1, Mục 2, Mục 3 vào `ho_so_launch_v0.md` ngay khi Gia Bảo chốt số. Đọc trước định nghĩa 5 loại lỗi Google PAIR.
3. **CP3 (15:35):** Trong **8 phút đầu**, ngồi tách riêng khỏi Duy và gắn nhãn độc lập 20 ca lỗi theo nguyên nhân gốc. Sau đó so nhãn với Duy, giữ nguyên nhãn gốc ở 2 cột độc lập, ghi tỉ lệ đồng thuận, quy tắc phân biệt ca lệch và hoàn thiện `report/team/bang_loi.md` + Mục 5 của `ho_so_launch_v0.md`.
4. **CP4:** Hoàn thiện `report/team/pilot_plan.yaml` (điền kết quả D1, D2 vào phần comment; xóa hết dấu `?` ở các trường; kiểm tra chạy `yaml.safe_load` không lỗi) và cập nhật Mục 6 của `ho_so_launch_v0.md`.
5. **CP5 & Gate 2a:** Hoàn thiện Mục 4, Mục 7 và Đề xuất cuối (`Go` / `Go có điều kiện` / `No-go` kèm số liệu bất lợi và điều kiện) trước **17:00**. Đại diện trình bày 1 phút ở Gate 2a, tổng hợp `report/team/phieu_cham.md`, `report/team/group_report.md` và kiểm tra checklist cuối trước khi nộp.

---

## 5. Năm quy tắc bắt buộc của Lab 13

1. **Qua đủ 3 phép thử A1 (`1,20 · 1,25 · 1,25`)** trong `src/lab13.py` rồi mới tính tiếp trên CSV.
2. **Mọi con số tính từ cột `_simulated`** (`phut_xem_lai_simulated`, `phut_lam_lai_simulated`) phải ghi nhãn `simulated`.
3. **Đọc file yêu cầu bắt buộc dùng `keep_default_na=False`** (`pd.read_csv('logix_requests.csv', keep_default_na=False)`) để không làm hỏng cột `quyet_dinh_xem_lai`.
4. **Mỗi câu trả lời trong hồ sơ không quá 3 dòng và có ít nhất 1 con số.** Người phụ trách ghi đúng **1 vai trò** (không ghi "cả đội").
5. **Không dùng từ chỉ vận hành chính thức (xem quy tắc 5 trong `README.md`)** trong bất kỳ file hồ sơ nào (Gate 2a chỉ duyệt kế hoạch pilot). Không kết luận trợ lý "đã nâng chỉ số" từ dữ liệu chạy thử chưa có đối chứng.

---

## 6. Quy trình Git và Checklist nộp bài (Trước 23h59 GMT+7)

### Quy trình Git phối hợp (Branch riêng + Pull Request vào `main`)

Không push trực tiếp vào `main`. Mỗi thành viên làm việc trên **1 nhánh riêng** để tránh conflict, bảo vệ tính độc lập ở CP3 và giữ link Pull Request làm bằng chứng đóng góp trong `TEAM.md` / `MSSV_HoTen.md`.

| Thành viên | Tên nhánh làm việc |
|---|---|
| **Đỗ Hoàng Vũ** | `feat/vu-cp1-cp2-cost` |
| **Trần Gia Bảo** | `feat/bao-cp1-cp4-validation` |
| **Nguyễn Bảo Duy** | `feat/duy-cp3-cp5-metrics` |
| **Bùi Đặng Nhật Nguyên** | `feat/nguyen-cp3-cp5-docs` |

**Bước 1 — Tạo nhánh riêng từ `main` (làm 1 lần đầu buổi):**

```bash
git checkout main
git pull origin main
git checkout -b <ten-nhanh-cua-ban>
```

**Bước 2 — Commit và đẩy nhánh lên GitHub sau mỗi Checkpoint:**

```bash
git add <chi_cac_file_minh_phu_trach>
git commit -m "cpX: mo ta ngan gon phan viec"
git push -u origin <ten-nhanh-cua-ban>
```

**Bước 3 — Tạo Pull Request (PR) và merge vào `main`:**

1. Mở GitHub repo -> chọn **Compare & pull request** từ nhánh của bạn vào `main`.
2. Nhờ 1 thành viên khác soát nhanh trong 1 phút (đúng file, không sửa CSV, đủ nhãn `simulated`).
3. Bấm **Create a merge commit** (không dùng squash để giữ nguyên tên tác giả từng commit trên `main`).

**Bước 4 — Đồng bộ `main` mới nhất về nhánh cá nhân trước khi làm CP tiếp theo:**

```bash
git fetch origin
git merge origin/main
```

**Quy tắc riêng cho CP3 (gắn nhãn độc lập):** Duy (`feat/duy-cp3-cp5-metrics`) và Nguyên (`feat/nguyen-cp3-cp5-docs`) **không mở hoặc merge PR chứa bộ nhãn 20 ca** trước khi cả hai hoàn thành 8 phút gắn nhãn độc lập.

**Tuyệt đối không:** push thẳng vào `main`; sửa `src/logix_runs.csv`, `src/logix_requests.csv`, `src/lab13_starter.py`, `report/team/MSSV_HoTen.md` gốc; không commit `.venv/` hay `.env`; không force-push hay xóa lịch sử commit.

### Checklist chốt trước khi nộp

- [ ] `TEAM.md` điền đủ Họ tên, MSSV, Email, GitHub, Vai trò và đóng góp của cả 4 thành viên.
- [ ] Mỗi thành viên đã **copy** `report/team/MSSV_HoTen.md` thành file riêng (`report/team/<MSSV>_<HoTenKhongDau>.md`) và điền đủ 6 mục (có mục Công cụ AI đã dùng).
- [ ] Chạy kiểm tra code trên 2 máy khác nhau: `cd src && python lab13.py` in `Ba phép thử đáp án biết trước: ĐẠT`.
- [ ] Đủ 6 file hồ sơ trong `report/team/` đúng tên: `bang_chi_phi.md`, `bang_loi.md`, `pilot_plan.yaml`, `chi_so.md`, `ho_so_launch_v0.md`, `phieu_cham.md`, cùng `group_report.md`.
- [ ] Kiểm tra YAML hợp lệ và không còn dấu `?` ngoài dòng chú thích:
  `python -c "import yaml; yaml.safe_load(open('report/team/pilot_plan.yaml'))"`
- [ ] Kiểm tra không có từ bị cấm trong `report/team/` (theo quy tắc 5 trong `README.md` và `CHECKPOINTS.md`).
- [ ] Đã push commit cuối lên `origin main` (repo public hoặc đã mở quyền cho giảng viên).
- [ ] **Cả 4 thành viên tự nộp cùng link repo nhóm lên LMS bằng tài khoản cá nhân trước 23h59 GMT+7** (ai không nộp link cá nhân sẽ không có điểm).
