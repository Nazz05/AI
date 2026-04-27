# A* PATHFINDING ALGORITHM

## GIOI THIEU

Đây là ứng dụng triển khai **Thuật toán A*** để tìm đường đi ngắn nhất trong một lưới (grid).
Ứng dụng sẽ:
- Khởi tạo một lưới 5x5 có chứa tường
- Tìm đường đi từ vị trí START đến vị trị GOAL
- Hiển thị đường đi bằng biểu đồ

---

## CẤU TRÚC DỰ ÁN

```
AI/
├── config.py           # Cấu hình: grid, điểm bắt đầu, điểm đích
├── main.py             # Chương trình chính
├── core/
│   ├── __init__.py
│   ├── grid.py         # Lớp GridWorld: Đại diện thế giới dạng lưới
│   └── utils.py        # Hàm hỗ trợ: heuristic, reconstruct_path
├── search/
│   ├── __init__.py
│   └── astar.py        # Thuật toán A*
├── visualization/
│   ├── __init__.py
│   └── plot.py         # Vẽ lưới và đường đi
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
cd 'd:\Visual studio code\AI'
python main.py
```

### Cách 2: Dùng Code Runner

- Bấm **Ctrl+Alt+N** (nếu đã cấu hình Code Runner)
- Hoặc Click phải > "Run Code"

### Cách 3: Dùng Task Runner

Bấm **Ctrl+Shift+B** để chạy task mặc định

---

## KẾT QUẢ CHẠY

Khi chạy xong, bạn sẽ thấy:

```
Path found!
Path: [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 3), (2, 4), (3, 4), (4, 4)]
Length: 9
```

Đồng thời một cửa sổ matplotlib sẽ hiển thị:
- Lưới 5x5 (màu trắng = đi được, màu đen = tường)
- Đường đi được vẽ bằng đường trắng

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
