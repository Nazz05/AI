# QUICK START GUIDE - M4

## 1️⃣ Cài đặt Python (Nếu chưa có)

Xem: [INSTALL_PYTHON.md](INSTALL_PYTHON.md)

## 2️⃣ Chạy chương trình

### Cách nhanh nhất:
```powershell
cd "e:\CACMONTRENLOP\NAM3\Ki2\2. AI"
python main.py
```
Chọn **2** để chạy M4

### Hoặc chạy demo riêng phần:
```powershell
cd "e:\CACMONTRENLOP\NAM3\Ki2\2. AI\m4"
python demo_m4.py
```
Chọn:
- **1** → Chỉ Logic Inference
- **2** → Chỉ STRIPS Planning
- **3** → Cả hai

## 3️⃣ Hiểu M4

**M4 gồm 2 phần**:

### Part 1: Logic Inference (Tư duy logic)
```
Input:  Sự kiện + Quy tắc
        dark(), person_home(), "Nếu dark + person_home → light_on"
        
Process: Forward Chaining (suy luận tiến)
         Áp dụng quy tắc để suy ra sự kiện mới
         
Output: Tất cả sự kiện (gốc + suy ra)
        dark(), person_home(), light_on() ← Suy ra được!
        
Ứng dụng: Tự động hóa nhà thông minh
          Khi trời tối + có người → tự động bật đèn
```

### Part 2: STRIPS Planning (Lập kế hoạch)
```
Input:  Initial state + Goal state + Hành động có sẵn
        Initial: [person_home, dark, light_off, door_unlocked]
        Goal:    [person_home, light_on, door_locked]
        Actions: turn_on_light, lock_door, ...
        
Process: BFS (tìm kiếm rộng)
         Tìm chuỗi hành động từ initial → goal
         
Output: Kế hoạch (danh sách hành động)
        Step 1: turn_on_light
        Step 2: lock_door
        → Goal achieved ✓
        
Ứng dụng: Lập kế hoạch để đạt mục tiêu
          Từ "nhà tối + cửa mở" → "nhà sáng + cửa khóa"
```

## 4️⃣ File chính

| File | Mục đích |
|------|---------|
| `logic/rules.py` | Định nghĩa Predicate, Rule, KnowledgeBase |
| `logic/inference.py` | Forward Chaining Engine |
| `planning/strips.py` | STRIPS Algorithm |
| `planning/domain.py` | Domain definition (actions, preconditions) |
| `planning/planner.py` | Run planning (BFS/DFS) |
| `main.py` | Chương trình chính (menu) |
| `demo_m4.py` | Demo từng phần |

## 5️⃣ Đọc thêm

- [MEMBER_M4.md](MEMBER_M4.md) - Giải thích chi tiết
- [README.md](README.md) - Thông tin đầy đủ dự án
- [INSTALL_PYTHON.md](INSTALL_PYTHON.md) - Cài đặt Python

## ❓ Lỗi phổ biến

### "python: command not found"
→ Python chưa cài đặt → Xem [INSTALL_PYTHON.md](INSTALL_PYTHON.md)

### "No module named matplotlib"
→ Chạy: `pip install matplotlib`

### "Python t∞m th" (Encoding error)
→ Khởi động lại PowerShell hoặc CMD
→ Thử: `python -c "print('Hello')"`

---

**Bắt đầu nào!** 🚀

```powershell
python main.py
```
