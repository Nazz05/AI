# 🚀 START HERE - BẮTDẦU TỪ ĐÂY

## Xin chào! 👋

Bạn vừa được giao Member **M4: Logic + AI Planning (STRIPS/PDDL)**.

Dự án này bao gồm:
- **M1**: A* Pathfinding (do người khác làm)
- **M4**: Logic + Planning (của bạn) ← **BẮT ĐẦU TỪ ĐÂY**

---

## ⏱️ 5 PHÚT ĐỂ CHẠY

### Bước 1: Cài đặt Python (Nếu chưa có)
```powershell
# Tải từ https://www.python.org/downloads/
# Chọn Python 3.10 hoặc 3.11
# ⚠️ QUAN TRỌNG: Đánh dấu "Add Python to PATH"
```

### Bước 2: Mở PowerShell
```powershell
cd "e:\CACMONTRENLOP\NAM3\Ki2\2. AI"
```

### Bước 3: Chạy
```powershell
python main.py
```

### Bước 4: Chọn **2** (Logic + Planning)
```
CHOOSE PROGRAM:
  1. M1: A* Pathfinding Algorithm
  2. M4: Logic + AI Planning (STRIPS/PDDL)  ← CHỌN CÁI NÀY
  3. Chạy tất cả
  0. Thoát
```

### Bước 5: Xem kết quả
```
[1] SỰ KIỆN BAN ĐẦU (Facts):
  • dark(living_room)
  • motion_detected(living_room)
  • person_home()
  ...

[2] SỐ QUY TẮC: 5
  • Auto_Light_On: [dark(living_room) ∧ person_home()] → [light_on(living_room)]
  ...

[3] KẾT QUẢ SAU SỰ LUẬN: light_on() được suy ra ✓
```

✅ **Bạn vừa chạy M4 thành công!**

---

## 📚 20 PHÚT ĐỂ HIỂU

### M4 là cái gì?

**M4 gồm 2 phần**:

#### Part 1: Logic Inference (Suy luận logic)
```
Ý tưởng: Nếu trời tối + có người ở nhà → tự động bật đèn

Input:
  Facts: [dark(), person_home()]
  Rules: "dark() + person_home() → light_on()"

Processing:
  Kiểm tra: dark() ✓, person_home() ✓
  → Quy tắc được áp dụng!

Output:
  Suy ra được: light_on() ← Đèn sáng tự động!

Ứng dụng: Tự động hóa nhà thông minh
```

#### Part 2: STRIPS Planning (Lập kế hoạch)
```
Ý tưởng: Từ "nhà tối, cửa mở" → "nhà sáng, cửa khóa"

Input:
  Initial: [person_home, dark, light_off, door_unlocked]
  Goal:    [person_home, light_on, door_locked]
  Actions: turn_on_light(), lock_door(), ...

Processing:
  Bước 1: turn_on_light → light_on() ✓
  Bước 2: lock_door → door_locked() ✓

Output:
  Kế hoạch: [turn_on_light, lock_door]
  Trạng thái: ĐẠT MỤC TIÊU ✓

Ứng dụng: Lập kế hoạch để đạt mục tiêu
```

---

## 🎓 30 PHÚT ĐỂ HIỂU SÂU

**Đọc file này**: [MEMBER_M4.md](MEMBER_M4.md)

Nó bao gồm:
- ✓ Khái niệm chi tiết (Predicate, Rule, Forward Chaining, ...)
- ✓ Ví dụ cụ thể cho từng phần
- ✓ Cách dùng code
- ✓ So sánh Part 1 vs Part 2

---

## 💻 XEM CODE

### File chính

| Part | File | Dòng code |
|------|------|-----------|
| Logic | `logic/rules.py` | 180 |
| Inference | `logic/inference.py` | 150 |
| Planning | `planning/strips.py` | 250 |
| Domain | `planning/domain.py` | 200 |
| Runner | `planning/planner.py` | 150 |
| **Total** | - | **930 dòng** |

### Đọc theo thứ tự này:

1. **logic/rules.py** - Bắt đầu với concepts cơ bản
   ```python
   class Predicate: # Sự kiện
   class Rule:      # Quy tắc
   class KnowledgeBase: # Lưu trữ
   ```

2. **logic/inference.py** - Cách suy luận
   ```python
   class LogicInferenceEngine:
       def forward_chain(): # Suy luận tiến
   ```

3. **planning/strips.py** - STRIPS algorithm
   ```python
   class Atom:        # Vị từ
   class Action:      # Hành động
   class STRIPSPlanner: # Tìm kế hoạch
   ```

4. **planning/domain.py** - Domain cho nhà thông minh
   ```python
   def create_smart_home_domain(): # Actions
   ```

5. **planning/planner.py** - Runner
   ```python
   def run_smart_home_planning(): # Chạy
   ```

---

## ❓ CÂU HỎI THƯỜNG GẶP

### Q: Tôi chạy bị lỗi "python: command not found"
**A**: Python chưa được cài đặt hoặc chưa thêm vào PATH
→ Xem: [INSTALL_PYTHON.md](INSTALL_PYTHON.md)

### Q: Chạy xong không thấy gì
**A**: Có thể lỗi encoding hoặc PowerShell. Thử:
```powershell
# Khóa PowerShell hiện tại
# Mở PowerShell mới (Ctrl+Shift+Esc)
# Thử lại: python main.py
```

### Q: Tôi muốn chạy chỉ Part 1 hoặc Part 2?
**A**: Chạy file demo:
```powershell
python demo_m4.py
# Chọn 1 → Logic only
# Chọn 2 → Planning only
# Chọn 3 → Cả hai
```

### Q: Tôi muốn mở rộng M4?
**A**: Sửa file `planning/domain.py`:
1. Thêm actions mới vào `create_smart_home_domain()`
2. Chạy: `python main.py` → Chọn 2

### Q: M4 có thể dùng cho bài toán khác không?
**A**: Có! Ví dụ logistics đã có sẵn. Xem `planning/domain.py`.

---

## 📁 FILE STRUCTURE

```
2. AI/
├── 🎯 START HERE (Đầu tiên)
│   ├── THIS_FILE (index.md) ← Bạn đang đọc
│   ├── QUICKSTART.md (5 min)
│   ├── MEMBER_M4.md (30 min - PHẢI ĐỌC)
│   └── INSTALL_PYTHON.md (nếu cần)
│
├── 📚 DOCUMENTATION
│   ├── README.md (tổng quan)
│   ├── M4_SUMMARY.md (tóm tắt kỹ thuật)
│   └── FILE_GUIDE.md (hướng dẫn tìm file)
│
├── 🧠 M4 CODE (Logic + Planning)
│   ├── logic/
│   │   ├── rules.py (Predicate, Rule, KB)
│   │   └── inference.py (Forward Chaining)
│   └── planning/
│       ├── strips.py (STRIPS Algorithm)
│       ├── domain.py (Actions)
│       └── planner.py (Runner)
│
├── ⚙️ M1 CODE (A* - người khác làm)
│   ├── core/ (grid, utils)
│   ├── search/ (astar)
│   └── visualization/ (plot)
│
├── 🎮 RUNNER
│   ├── main.py (Menu)
│   ├── demo_m4.py (Demo)
│   └── test_import.py (Test)
```

---

## ✅ TODO

Để hoàn thành M4:

- [ ] Cài Python 3.7+
- [ ] Đọc [QUICKSTART.md](QUICKSTART.md)
- [ ] Chạy: `python main.py` → Chọn 2
- [ ] Xem kết quả Logic Inference
- [ ] Xem kết quả STRIPS Planning
- [ ] Đọc [MEMBER_M4.md](MEMBER_M4.md)
- [ ] Hiểu Forward Chaining
- [ ] Hiểu STRIPS Planning
- [ ] Đọc code: `logic/rules.py`
- [ ] Đọc code: `logic/inference.py`
- [ ] Đọc code: `planning/strips.py`
- [ ] Đọc code: `planning/domain.py`
- [ ] Đọc code: `planning/planner.py`
- [ ] Chạy: `python demo_m4.py` (test từng phần)
- [ ] ✅ HOÀN THÀNH M4

---

## 🎉 LỜI CUỐI

Bạn được giao một dự án **hoàn toàn hoàn chỉnh** với:
- ✓ Code đầy đủ (930 dòng)
- ✓ Hướng dẫn chi tiết (3000+ dòng doc)
- ✓ Demo có sẵn
- ✓ Sẵn sàng chạy

Chỉ cần:
1. Cài Python
2. Chạy: `python main.py`
3. Chọn 2
4. Enjoy! 🚀

---

## 🔗 CÁC LINK QUAN TRỌNG

| Link | Mục đích |
|------|---------|
| [QUICKSTART.md](QUICKSTART.md) | Hướng dẫn 5 phút |
| [MEMBER_M4.md](MEMBER_M4.md) | **PHẢI ĐỌC** - 30 phút |
| [FILE_GUIDE.md](FILE_GUIDE.md) | Tìm file |
| [M4_SUMMARY.md](M4_SUMMARY.md) | Tóm tắt kỹ thuật |
| [INSTALL_PYTHON.md](INSTALL_PYTHON.md) | Cài Python |
| [README.md](README.md) | Toàn bộ dự án |

---

## 💬 FEEDBACK

- Lỗi? → Xem [INSTALL_PYTHON.md](INSTALL_PYTHON.md)
- Không hiểu? → Đọc [MEMBER_M4.md](MEMBER_M4.md)
- Muốn biết thêm? → Xem [FILE_GUIDE.md](FILE_GUIDE.md)

---

**BẮT ĐẦU:**

```powershell
python main.py
```

Chọn **2** → ENJOY! 🎉
