# AI PROJECT - PATHFINDING & PLANNING

## GIỚI THIỆU

Dự án này triển khai các thuật toán AI:

### M1: A\* Pathfinding Algorithm

Đây là ứng dụng triển khai **Thuật toán A\*** để tìm đường đi ngắn nhất trong một lưới (grid).

- Khởi tạo một lưới 5x5 có chứa tường
- Tìm đường đi từ vị trí START đến vị trị GOAL
- Hiển thị đường đi bằng biểu đồ

### M2: So Sánh Dijkstra + Greedy vs A*

Triển khai và so sánh hai thuật toán tìm đường khác:

- **Dijkstra**: Thuật toán tìm đường tối ưu (optimal), nhưng kham phá nhiều node hơn
- **Greedy**: Chỉ dùng heuristic để đánh giá, nhanh hơn nhưng có thể không tối ưu
- **So sánh**: 
  - Hiển thị đường đi tìm được
  - Bảng so sánh: Path Length, Nodes Expanded
  - Phân tích kết quả và nhận xét hiệu suất

### M3: Random Search + Q-Learning

Thuật toán học tăng cường (Reinforcement Learning) trên GridWorld:

- **Random Search**: Tìm đường ngẫu nhiên trong N episodes
- **Q-Learning**: Agent học chính sách tối ưu qua các episode
- So sánh hiệu suất giữa Random Search, Q-Learning và A*

### Member 4: Logic + STRIPS

Hệ thống logic và lập kế hoạch AI cho tự động hóa nhà thông minh

- **Bài 5 (Rule-based)**: Logic inference engine
  - Biểu diễn quy tắc IF-THEN với predicate và điều kiện
  - Ví dụ: "Nếu trời tối và có người ở phòng khách → bật đèn"
  - Sử dụng Forward Chaining để suy ra hành động tự động
- **Bài 6 (STRIPS/PDDL)**: Planning
  - Biểu diễn hành động với tiền điều kiện (preconditions) và hiệu ứng (effects)
  - Tìm chuỗi hành động từ trạng thái ban đầu đến mục tiêu
  - Sử dụng BFS để tìm kế hoạch hành động tối ưu

---

## CẤU TRÚC DỰ ÁN

```
AI/
├── config.py           # Cấu hình chung: grid, điểm bắt đầu, điểm đích
├── main.py             # Chương trình chính - Menu chọn M1 hoặc M4
├── core/               # Core utilities (M1 - A* Pathfinding)
│   ├── __init__.py
│   ├── grid.py         # Lớp GridWorld: Đại diện thế giới dạng lưới
│   └── utils.py        # Hàm hỗ trợ: heuristic, reconstruct_path
├── search/             # Search algorithms (M1 - A*, M2 - Dijkstra, Greedy)
│   ├── __init__.py
│   ├── astar.py        # Thuật toán A*
│   ├── dijkstra.py     # Thuật toán Dijkstra (M2)
│   └── greedy.py       # Thuật toán Greedy (M2)
├── visualization/      # Visualization (M1 - biểu đồ)
│   ├── __init__.py
│   └── plot.py         # Vẽ lưới và đường đi
├── logic/              # M4 logic + planning
│   ├── __init__.py
│   ├── rules.py        # Định nghĩa rules, predicates, knowledge base
│   ├── inference.py    # Forward Chaining inference engine
│   ├── strips.py       # STRIPS planning core
│   ├── domain.py       # Domain definitions (atoms, actions)
│   └── planner.py      # Planner driver
├── m3/                 # Member 3: learning module
│   ├── __init__.py
│   ├── environment.py
│   ├── q_learning.py
│   ├── random_search.py
│   └── visualize.py
└── .vscode/            # VS Code configuration (optional)
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

- **1** để chạy M1 (A\* Pathfinding)
- **2** để chạy M2 (Dijkstra + Greedy Comparison)
- **3** để chạy M3 (Random Search + Q-Learning)
- **4** để chạy M4 (Logic + STRIPS)
- **5** để chạy tất cả
- **0** để thoát

### Cách 2: Chạy trực tiếp module

#### M1 - A\* Pathfinding:

```powershell
python -c "from main import run_m1_astar; run_m1_astar()"
```

#### Logic + STRIPS:

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

### M1 - A\* Pathfinding:

Khi chạy M1, bạn sẽ thấy:

```
Path found!
Path: [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 3), (2, 4), (3, 4), (4, 4)]
Length: 9
```

Đồng thời một cửa sổ matplotlib sẽ hiển thị:

- Lưới 5x5 (màu trắng = đi được, màu đen = tường)
- Đường đi được vẽ bằng đường trắng

### M2 - Dijkstra + Greedy Comparison:

Khi chạy M2, bạn sẽ thấy:

**[1] Chạy các thuật toán:**
```
  - Chay A*...
  - Chay Dijkstra...
  - Chay Greedy...
```

**[2] Bảng so sánh kết quả:**
--- A* ---
Path length     : 9
Nodes expanded  : 9
Path            : [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 3), (2, 4), (3, 4), (4, 4)]

--- Dijkstra ---
Path length     : 9
Nodes expanded  : 14
Path            : [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 3), (2, 4), (3, 4), (4, 4)]

--- Greedy ---
Path length     : 9
Nodes expanded  : 8
Path            : [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 3), (2, 4), (3, 4), (4, 4)]

**[3] Phân tích chi tiết:**
```
[3] PHAN TICH:
  - Dijkstra va Greedy tim duoc duong di co cung do dai: 9 buoc
  - Greedy kham pham it node hon: 8 < 14 (6 node it hon)
  - A* tim duoc duong di toi uu: 9 buoc (bang Dijkstra)
  - A* co hieu suat hon Dijkstra: 5 node it hon
```

**[4] So sánh thuật toán:**
```
  - Dijkstra: Tim duong di toi uu (optimal), kham pham da so node
  - Greedy: Tim duong di nhanh, nhung co the khong toi uu
  - A*: Toi uu + nhanh, su dung heuristic de huong tim kiem
```

**[5] Hiển thị biểu đồ:**
- Vẽ đường đi của Dijkstra trên grid
- Vẽ đường đi của Greedy trên grid

### Logic + STRIPS:

#### Phần 1 - Logic Inference Output:

```
============================================================
ENGINE SUY LUAN LOGIC - FORWARD CHAINING
============================================================

[1] SU KIEN BAN DAU (Facts):
  - dark(living_room)
  - light_off(living_room)
  - motion_detected(living_room)
  - person_home(living_room)
  - room(living_room)
  - room(bedroom)
  - room(kitchen)
  - temperature(20)

[2] SO QUY TAC: 5
  - Auto_Light_On: [dark(X) and person_home(X)] -> [light_on(X)]
  - Motion_Activated_Light: [motion_detected(X)] -> [light_on(X)]
  - Auto_AC_On: [high_temperature] -> [ac_on]
  - Away_Mode_Activated: [no_person_home] -> [door_locked and energy_saving_mode]
  - Auto_Light_Off: [light_on(X) and no_motion(X)] -> [light_off(X)]

[Lan lap 1] Ap dung quy tac: Auto_Light_On
  -> Ket luan: ['light_on(X)']

[3] KET QUA SAU SUY LUAN:
  - Tong su kien: 9
  - Quy tac ap dung: 1

[4] DANH SACH TAT CA SU KIEN:
  GOC | dark(living_room)
  GOC | light_off(living_room)
  SUY RA | light_on(living_room)
  GOC | motion_detected(living_room)
  ...

[5] HANH DONG TU DONG HOA:
  HANH DONG: light_on(living_room)
```

#### Phần 2 - STRIPS Planning Output:

```
======================================================================
LAP KE HOACH AI - TU DONG HOA NHA THONG MINH (STRIPS/PDDL)
======================================================================

[1] TRANG THAI BAN DAU:
  - ac_off
  - dark(living_room)
  - door_unlocked
  - light_off(living_room)
  - low_temperature
  - person_home(living_room)
  - security_disarmed

[2] TRANG THAI MUC TIEU:
  - ac_off
  - door_locked
  - light_on(living_room)
  - person_home(living_room)
  - security_disarmed

[3] HANH DONG CO SAN: 8
  1. turn_on_light: [dark(living_room), person_home(living_room)] -> [+light_on(living_room), -light_off(living_room)]
  2. turn_off_light: [light_on(living_room)] -> [+light_off(living_room), -light_on(living_room)]
  ...

[4] DANG TIM KE HOACH (BFS)...

[5] KE HOACH TIM THAY: 2 buoc
  Step 1: turn_on_light
  Step 2: lock_door

[6] THUC THI KE HOACH:

Step 1: turn_on_light
  EXECUTED SUCCESSFULLY
  -> New state: 7 atoms

Step 2: lock_door
  EXECUTED SUCCESSFULLY
  -> New state: 7 atoms

[7] TRANG THAI CUOI CUNG: 7 atoms
DAT DUOC MUC TIEU!
```
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

## GIẢI THÍCH LOGIC + STRIPS

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

### 2. Thuật toán A\* chạy

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

- Python 3.7+ nên được cài đặt.
- Sử dụng `pip install matplotlib` nếu muốn chạy phần hiển thị.

---

## THÔNG TIN CHI TIẾT VỀ LOGIC + STRIPS

M4 giờ chỉ còn nằm trong code tại `logic/`.
Các tài liệu hướng dẫn bên ngoài đã được loại bỏ để giữ cấu trúc gọn và đúng theo ảnh.

- `logic/rules.py` - rule definitions + knowledge base
- `logic/inference.py` - forward chaining engine
- `logic/strips.py` - STRIPS planning core
- `logic/domain.py` - domain definitions
- `logic/planner.py` - planner driver

- Ví dụ cụ thể cho mỗi phần
- Cách sử dụng từng module

---

## GIẢI THÍCH THUẬT TOÁN A\*

### A\* là gì?

A\* là thuật toán tìm đường đi ngắn nhất kết hợp:

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

### Tại sao A\* nhanh?

Vì A\* **ưu tiên** kiểm tra những vị trí có khả năng dẫn đến GOAL cao nhất (dựa trên F-score).
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
2. Chạy A\*
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

**Thuật toán A\***:

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
3. So sánh A\* với Dijkstra, BFS
4. Thêm test cases
5. Xuất kết quả ra file
6. Tạo giao diện GUI

---

## LƯU Ý

- Heuristic Manhattan distance chỉ hoạt động tốt khi chỉ có 4 hướng di chuyển
- Nếu thêm hướng chéo, cần đổi heuristic (Euclidean hoặc Chebyshev)
- A\* **luôn tìm đường đi tối ưu** nếu heuristic **không vượt quá** khoảng cách thực tế

---

## LIÊN HỆ & HỖ TRỢ

Nếu có câu hỏi, vui lòng kiểm tra comments chi tiết trong từng file code.
