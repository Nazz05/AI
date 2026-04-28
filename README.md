# AI PROJECT - PATHFINDING & PLANNING

## GIỚI THIỆU

Dự án này triển khai các thuật toán AI:

### M1: A* Pathfinding Algorithm
Đây là ứng dụng triển khai **Thuật toán A*** để tìm đường đi ngắn nhất trong một lưới (grid).
- Khởi tạo một lưới 5x5 có chứa tường
- Tìm đường đi từ vị trí START đến vị trị GOAL
- Hiển thị đường đi bằng biểu đồ

### M4: Logic + AI Planning (STRIPS/PDDL)
Hệ thống logic và lập kế hoạch AI cho tự động hóa nhà thông minh
- **Phần 1 (Logic)**: Forward Chaining Inference Engine
  - Biểu diễn các quy tắc logic (FOL - First Order Logic)
  - Ví dụ: "Nếu trời tối và có người ở nhà → bật đèn"
  - Sử dụng suy luận tiến (Forward Chaining) để suy ra các sự kiện mới
  
- **Phần 2 (Planning)**: STRIPS/PDDL Planner
  - Lập kế hoạch hành động từ trạng thái ban đầu đến trạng thái mục tiêu
  - Biểu diễn hành động với điều kiện tiên quyết (preconditions) và kết quả (effects)
  - Sử dụng BFS/DFS để tìm chuỗi hành động tối ưu

---

## CẤU TRÚC DỰ ÁN

```
AI/
├── config.py           # Cấu hình: grid, điểm bắt đầu, điểm đích (M1)
├── main.py             # Chương trình chính - Menu chọn M1 hoặc M4
├── core/               # Core utilities (M1 - A* Pathfinding)
│   ├── __init__.py
│   ├── grid.py         # Lớp GridWorld: Đại diện thế giới dạng lưới
│   └── utils.py        # Hàm hỗ trợ: heuristic, reconstruct_path
├── search/             # Search algorithms (M1 - A*)
│   ├── __init__.py
│   └── astar.py        # Thuật toán A*
├── visualization/      # Visualization (M1 - biểu đồ)
│   ├── __init__.py
│   └── plot.py         # Vẽ lưới và đường đi
├── m4/                 # Member 4: Logic + AI Planning (STRIPS/PDDL)
│   ├── logic/          # Logic inference (Part 1)
│   │   ├── __init__.py
│   │   ├── rules.py    # Định nghĩa rules, predicates, knowledge base
│   │   └── inference.py # Forward Chaining inference engine
│   ├── planning/       # AI Planning (Part 2)
│   │   ├── __init__.py
│   │   ├── strips.py   # STRIPS algorithm - lập kế hoạch
│   │   ├── domain.py   # Định nghĩa domain (actions, preconditions, effects)
│   │   └── planner.py  # Planner - chạy STRIPS
│   ├── demo_m4.py      # Demo riêng từng phần
│   ├── test_import.py  # Test import modules
│   ├── INSTALL_PYTHON.md # Hướng dẫn cài đặt Python
│   ├── MEMBER_M4.md    # Chi tiết M4 (khái niệm + code)
│   ├── QUICKSTART.md   # Hướng dẫn nhanh
│   ├── FILE_GUIDE.md   # Hướng dẫn tìm file
│   ├── M4_SUMMARY.md   # Tóm tắt M4
│   └── INDEX.md        # Điểm bắt đầu
└── .vscode/
    ├── settings.json   # Cấu hình Code Runner
    └── tasks.json      # Cấu hình Task Runner
```

---

## CÀI ĐẶT

### Yêu cầu:
- Python 3.7+
- matplotlib (để vẽ biểu đồ)

### Bước 1: Cài đặt thư viện cần thiết

```powershell
pip install matplotlib
```

---

## CHẠY CHƯƠNG TRÌNH

### Cách 1: Chạy từ Terminal (Khuyến nghị)

Mở PowerShell, chuyển vào thư mục dự án:

```powershell
cd 'e:\CACMONTRENLOP\NAM3\Ki2\2. AI'
python main.py
```

Sau đó chọn:
- **1** để chạy M1 (A* Pathfinding)
- **2** để chạy M4 (Logic + Planning)
- **3** để chạy cả hai
- **0** để thoát

### Cách 2: Chạy trực tiếp module

#### M1 - A* Pathfinding:
```powershell
python -c "from main import run_m1_astar; run_m1_astar()"
```

#### M4 - Logic + Planning:
```powershell
python -c "from main import run_m4_logic_planning; run_m4_logic_planning()"
```

### Cách 3: Dùng Code Runner

- Bấm **Ctrl+Alt+N** (nếu đã cấu hình Code Runner)
- Hoặc Click phải > "Run Code"

### Cách 4: Dùng Task Runner

Bấm **Ctrl+Shift+B** để chạy task mặc định

---

## KẾT QUẢ CHẠY

### M1 - A* Pathfinding:

Khi chạy M1, bạn sẽ thấy:

```
Path found!
Path: [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 3), (2, 4), (3, 4), (4, 4)]
Length: 9
```

Đồng thời một cửa sổ matplotlib sẽ hiển thị:
- Lưới 5x5 (màu trắng = đi được, màu đen = tường)
- Đường đi được vẽ bằng đường trắng

### M4 - Logic + Planning:

#### Phần 1 - Logic Inference Output:

```
============================================================
LOGIC INFERENCE ENGINE - FORWARD CHAINING
============================================================

[1] SỰ KIỆN BAN ĐẦU (Facts):
  • dark(living_room)
  • motion_detected(living_room)
  • person_home()
  • room(living_room)
  • room(bedroom)
  • room(kitchen)
  • temperature(20)

[2] SỐ QUY TẮC: 5
  • Auto_Light_On: [dark(living_room) ∧ person_home()] → [light_on(living_room)]
  • Motion_Activated_Light: [motion_detected(living_room)] → [light_on(living_room)]
  • Auto_Light_Off: [light_on(living_room) ∧ no_motion(living_room)] → [light_off(living_room)]
  • Auto_AC_On: [high_temperature()] → [ac_on()]
  • Away_Mode_Activated: [no_person_home()] → [door_locked() ∧ energy_saving_mode()]

[3] KẾT QUẢ SAU SỰ LUẬN:
  • Tổng sự kiện: 8
  • Quy tắc áp dụng: 2

[4] DANH SÁCH TẤT CẢ SỰ KIỆN:
  🟢 Suy ra | light_on(living_room)
  ⚫ Gốc | person_home()
  ...

[5] HÀNH ĐỘNG TỰ ĐỘNG HÓA:
  ⚡ light_on(living_room)
```

#### Phần 2 - STRIPS Planning Output:

```
======================================================================
AI PLANNING - SMART HOME AUTOMATION (STRIPS/PDDL)
======================================================================

[1] TRẠNG THÁI BAN ĐẦU (Initial State):
  • person_home()
  • dark()
  • light_off()
  • ac_off()
  ...

[2] TRẠNG THÁI MỤC TIÊU (Goal State):
  • person_home()
  • light_on()
  • ac_off()
  • door_locked()
  ...

[3] DANH SÁCH CÁC HÀNH ĐỘNG KHẢ DỤNG: 8
  1. turn_on_light: [dark() ∧ person_home()] → [+light_on() -light_off()]
  2. turn_off_light: [light_on()] → [+light_off() -light_on()]
  ...

[4] TÌM KIẾM KẾ HOẠCH (BFS)...

[5] KẾ HOẠCH TÌM ĐƯỢC: 3 bước
  Step 1: turn_on_light
  Step 2: lock_door
  Step 3: arm_security

[6] THỰC THI KẾ HOẠCH:
  Step 1: turn_on_light
    ✓ Thực thi thành công
  Step 2: lock_door
    ✓ Thực thi thành công
  Step 3: arm_security
    ✓ Thực thi thành công

[7] TRẠNG THÁI CUỐI CÙNG: 6 atoms
  ✓ ĐẠT MỤC TIÊU!
```

---

## GIẢI THÍCH M4: LOGIC + PLANNING

### Phần 1: LOGIC INFERENCE (Forward Chaining)

#### Khái niệm:

- **Predicate (Vị từ)**: Biểu diễn sự kiện trong logic
  - Ví dụ: `light_on(living_room)`, `person_home()`, `dark()`
  
- **Rule (Quy tắc)**: Biểu diễn mối quan hệ logic
  - Dạng: **Nếu {conditions} thì {conclusions}**
  - Ví dụ: `Nếu dark(X) ∧ person_at(X) → turn_light_on(X)`
  
- **Forward Chaining**: Suy luận từ sự kiện → kết luận
  - Bắt đầu từ các sự kiện gốc (facts)
  - Liên tục áp dụng các quy tắc
  - Suy ra các sự kiện mới cho đến khi không còn quy tắc nào có thể áp dụng

#### Ứng dụng: Smart Home Automation

**Bài toán**: Tự động hóa nhà thông minh

**Sự kiện ban đầu**:
- `person_home()` - Có người ở nhà
- `dark()` - Trời tối
- `motion_detected()` - Phát hiện chuyển động

**Quy tắc**:
1. Nếu tối + có người → bật đèn
2. Nếu phát hiện chuyển động → bật đèn
3. Nếu nhiệt độ cao → bật điều hòa
4. Nếu vắng nhà → khóa cửa + chế độ tiết kiệm

**Kết luận**:
- `light_on()` - Đèn được bật tự động
- `ac_on()` - Điều hòa được bật (nếu nhiệt độ cao)
- `door_locked()` - Cửa khóa tự động (nếu vắng nhà)

### Phần 2: STRIPS PLANNING (Goal-Based Planning)

#### Khái niệm:

- **State (Trạng thái)**: Tập hợp các atoms (sự kiện) tại một thời điểm
  
- **Action (Hành động)**: Biểu diễn hành động trong STRIPS
  - **Preconditions**: Điều kiện tiên quyết (phải thoả mãn để thực thi)
  - **Effects**: Kết quả của hành động (atoms được thêm/xóa)
  
- **Goal**: Trạng thái mục tiêu cần đạt đến
  
- **Planning**: Tìm chuỗi hành động từ initial state → goal state

#### Ví dụ:

**Bài toán**: Nhà thông minh vào buổi tối

**Trạng thái ban đầu**:
```
- person_home()
- dark()
- light_off()
- ac_off()
- door_unlocked()
```

**Mục tiêu**:
```
- person_home()
- light_on()        ← Cần bật đèn
- ac_off()
- door_locked()     ← Cần khóa cửa
```

**Hành động có sẵn**:
```
1. turn_on_light
   Preconditions: [dark(), person_home()]
   Effects: [+light_on(), -light_off()]

2. lock_door
   Preconditions: [person_home()]
   Effects: [+door_locked(), -door_unlocked()]
```

**Kế hoạch tìm được**:
```
Step 1: turn_on_light
  - Kiểm tra: dark() ✓, person_home() ✓ → có thể thực thi
  - Kết quả: light_on() được thêm, light_off() được xóa

Step 2: lock_door
  - Kiểm tra: person_home() ✓ → có thể thực thi
  - Kết quả: door_locked() được thêm
```

**Trạng thái cuối cùng**: ✓ ĐẠT MỤC TIÊU

---

## GIẢI THÍCH LUỒNG CHẠY

### 1. Khởi động chương trình

**File:** main.py - Hàm main()

```
main() bắt đầu
    |
    v
Khởi tạo GridWorld(GRID)
    |
    v
Gọi hàm astar(grid, START, GOAL)
```

### 2. Thuật toán A* chạy

**File:** search/astar.py - Hàm astar()

```
astar(grid, START, GOAL)
    |
    v
Khởi tạo: open_set = [(0, START)]
          g_score = {START: 0}
          came_from = {}
    |
    v
LẶP CHÍNH:
  - Lay diem co F_score nho nhat tu open_set
  - Kiem tra neu la GOAL?
    - CO: Return duong di
    - KHONG: Kiem tra hang xom
  
  Voi moi hang xom:
    - Tinh chi phi moi: temp_g = g_score[current] + 1
    - Chi phi nay co ngan hon khong?
      - CO: Cap nhat g_score
              Tinh F = g + heuristic
              Them vao open_set
              Luu duong truoc trong came_from
    - KHONG: Boqed hang xom nay
    
  Lap lai cho den khi:
    - Tim duoc GOAL (return path)
    - open_set rong (return None - khong co duong)
```

### 3. Tái tạo đường đi

**File:** core/utils.py - Hàm reconstruct_path()

```
came_from = {
    (0,1): (0,0),
    (0,2): (0,1),
    (1,2): (0,2),
    ...,
    (4,4): (3,4)
}

reconstruct_path(came_from, (4,4)):
  - Bat dau tu (4,4)
  - Lui ve (3,4)
  - Lui ve (2,4)
  - ...
  - Lui ve (0,0)
  - Dao nguoc: [(0,0), (0,1), ..., (4,4)]
```

### 4. Hiển thị kết quả

**File:** main.py & visualization/plot.py

```
if path:
    In ra duong di
    Goi draw(grid, path)
        - Vẽ lưới bằng matplotlib
        - Vẽ đường đi lên trên lưới
        - Hiển thị cửa sổ
else:
    In "No path found!"
```

---

## HƯỚNG DẪN CÀI ĐẶT PYTHON

**Chú ý**: Python chưa được cài đặt trên hệ thống? Xem file [INSTALL_PYTHON.md](INSTALL_PYTHON.md)

---

## THÔNG TIN CHI TIẾT VỀ M4

Xem file [MEMBER_M4.md](MEMBER_M4.md) để có hướng dẫn chi tiết:
- Khái niệm Logic Inference + Forward Chaining
- Khái niệm STRIPS Planning + BFS
- Ví dụ cụ thể cho mỗi phần
- Cách sử dụng từng module

---

## GIẢI THÍCH THUẬT TOÁN A*

### A* là gì?

A* là thuật toán tìm đường đi ngắn nhất kết hợp:
- **Dijkstra:** Biết chi phí thực tế từ START đến hiện tại (g-score)
- **Greedy:** Ước tính chi phí còn lại đến GOAL (h-score)

### F-score = G-score + H-score

- **G-score:** Số bước đã đi từ START
- **H-score:** Ước tính (Manhattan distance) từ vị trí hiện tại đến GOAL
- **F-score:** Tổng chi phí dự kiến để đến GOAL qua vị trí này

### Heuristic (Manhattan Distance)

```
heuristic((0,0), (4,4)) = |0-4| + |0-4| = 8

Giải thích:
- Khoảng cách theo hàng: |0-4| = 4
- Khoảng cách theo cột: |0-4| = 4
- Tổng cộng = 8 bước
```

### Tại sao A* nhanh?

Vì A* **ưu tiên** kiểm tra những vị trí có khả năng dẫn đến GOAL cao nhất (dựa trên F-score).
Không kiểm tra mọi vị trí (như Dijkstra) nên nhanh hơn.

---

## CẤU TRÚC DỮ LIỆU CHÍNH

### GridWorld (core/grid.py)

```python
grid = GridWorld(GRID)
- grid.grid: Ma tran 2D
- grid.rows: So hang
- grid.cols: So cot
```

**Phương thức:**
- `is_valid(x, y)`: Kiểm tra vị trí có hợp lệ không
- `get_neighbors(node)`: Lấy danh sách vị trí hàng xóm

### Config (config.py)

```python
GRID = [
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]
- 0 = Ô trống (đi được)
- 1 = Tường (đi không được)

START = (0, 0)  # Điểm bắt đầu
GOAL = (4, 4)   # Điểm đích
```

---

## VÍ DỤ CHẠY CHI TIẾT

### Input:

```
GRID: 
0 0 0 1 0
1 1 0 1 0
0 0 0 0 0
0 1 1 1 0
0 0 0 0 0

START = (0, 0)
GOAL = (4, 4)
```

### Quá trình:

Bước 1: Từ (0,0), kiểm tra hàng xóm: (0,1), (1,0)
- (0,1): g=1, h=7, f=8
- (1,0): không hợp lệ (là tường)

Bước 2: Chọn (0,1) (f nhỏ nhất), kiểm tra hàng xóm
- (0,2): g=2, h=6, f=8
- ...

... (tiếp tục cho đến khi đạt GOAL)

### Output:

```
Path found!
Path: [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 3), (2, 4), (3, 4), (4, 4)]
Length: 9
```

---

## GIẢI THÍCH CÁC FILE

### config.py

Chứa các tham số cấu hình chính:
- `GRID`: Lưới 5x5 mô tả thế giới
- `START`: Vị trí bắt đầu
- `GOAL`: Vị trí đích

### main.py

Chương trình chính:
1. Khởi tạo GridWorld
2. Chạy A*
3. Hiển thị kết quả
4. Xử lý lỗi

### core/grid.py

Lớp **GridWorld**:
- Lưu trữ lưới
- Kiểm tra vị trí hợp lệ
- Lấy danh sách hàng xóm

### core/utils.py

Hàm hỗ trợ:
- `heuristic(a, b)`: Tính Manhattan distance
- `reconstruct_path(came_from, current)`: Tái tạo đường đi từ came_from

### search/astar.py

**Thuật toán A***:
- Khởi tạo open_set, g_score, came_from
- Lặp chính: Chọn vị trí có F nhỏ nhất
- Cập nhật chi phí và hàng xóm
- Trả về đường đi hoặc None

### visualization/plot.py

Hiển thị:
- Vẽ lưới (matplotlib heatmap)
- Vẽ đường đi (đường kẻ)
- Hiển thị cửa sổ

---

## KHẮC PHỤC LỖI

### Lỗi: "No path found!"
- Kiểm tra START và GOAL có hợp lệ không
- Kiểm tra có đường nào kết nối START và GOAL không

### Lỗi: "Visualization error"
- Cài đặt matplotlib: `pip install matplotlib`
- Hoặc không có display server (khi chạy remote)

### Lỗi: "Module not found"
- Đảm bảo bạn `cd` vào thư mục chính trước khi chạy
- Kiểm tra tất cả file `__init__.py` có tồn tại không

### Code Runner không chạy
- Kiểm tra cấu hình settings.json trong .vscode/
- Dùng PowerShell thay vì Command Prompt

---

## MỞ RỘNG TƯƠNG LAI

Có thể cải thiện dự án:
1. Thêm hỗ trợ 8 hướng (bao gồm đường chéo)
2. Thêm visualize quá trình tìm kiếm (step-by-step)
3. So sánh A* với Dijkstra, BFS
4. Thêm test cases
5. Xuất kết quả ra file
6. Tạo giao diện GUI

---

## LƯU Ý

- Heuristic Manhattan distance chỉ hoạt động tốt khi chỉ có 4 hướng di chuyển
- Nếu thêm hướng chéo, cần đổi heuristic (Euclidean hoặc Chebyshev)
- A* **luôn tìm đường đi tối ưu** nếu heuristic **không vượt quá** khoảng cách thực tế

---

## LIÊN HỆ & HỖ TRỢ

Nếu có câu hỏi, vui lòng kiểm tra comments chi tiết trong từng file code.
