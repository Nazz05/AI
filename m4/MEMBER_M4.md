# MEMBER M4: LOGIC + AI PLANNING (STRIPS/PDDL)

## Tổng quan

Member M4 gồm 2 phần:
1. **PART 1: Logic Inference Engine** - Suy luận logic tự động hóa nhà thông minh
2. **PART 2: STRIPS Planning** - Lập kế hoạch hành động từ initial state → goal state

---

## PART 1: LOGIC INFERENCE ENGINE

### Khái niệm

#### 1. Predicate (Vị từ)
Biểu diễn một sự kiện trong logic.

```python
# Ví dụ:
light_on(living_room)  # Đèn phòng khách đang bật
person_home()          # Có người ở nhà
temperature(23)        # Nhiệt độ 23°C
```

**Cấu trúc**:
- `name`: Tên vị từ (ví dụ: "light_on", "person_home")
- `args`: Đối số (danh sách chuỗi hoặc rỗng)

#### 2. Rule (Quy tắc)
Biểu diễn một mối quan hệ logic dưới dạng IF-THEN.

```
Rule: "Auto_Light_On"
  Conditions: [dark(living_room), person_home()]
  Conclusions: [light_on(living_room)]
  
Ý nghĩa: Nếu (phòng khách tối) VÀ (có người ở nhà) 
         THÌ (bật đèn phòng khách)
```

**Cấu trúc**:
- `name`: Tên quy tắc
- `conditions`: Danh sách điều kiện (Predicates)
- `conclusions`: Danh sách kết luận (Predicates)
- `priority`: Độ ưu tiên (cao → thực thi trước)

#### 3. Knowledge Base (Cơ sở kiến thức)
Lưu trữ tất cả facts và rules.

```python
kb = KnowledgeBase()
kb.add_fact(Predicate("person_home", ()))
kb.add_fact(Predicate("dark", ("living_room",)))
kb.add_rule(rule1)
kb.add_rule(rule2)
```

#### 4. Forward Chaining (Suy luận tiến)
Quy trình suy luận logic từ facts ban đầu.

```
Bước 1: Bắt đầu với sự kiện gốc
        facts = {person_home(), dark(living_room), motion_detected()}

Bước 2: Áp dụng quy tắc
        - Kiểm tra điều kiện: dark() ✓, person_home() ✓
        - Kết luận: light_on(living_room) ← Suy ra được!

Bước 3: Cập nhật facts
        facts = {..., light_on(living_room)}

Bước 4: Lặp lại cho đến khi không suy ra được gì mới
```

### Ứng dụng: Smart Home Automation

**Bài toán**: Tự động hóa nhà thông minh

**Sự kiện ban đầu** (Initial Facts):
```
• person_home()         - Có người ở nhà
• dark(living_room)     - Phòng khách tối
• motion_detected()     - Phát hiện chuyển động
• temperature(20)       - Nhiệt độ 20°C
```

**Quy tắc** (Rules):

1. **Auto_Light_On**
   ```
   IF: dark(living_room) ∧ person_home()
   THEN: light_on(living_room)
   ```
   Nếu tối và có người → bật đèn

2. **Motion_Activated_Light**
   ```
   IF: motion_detected(living_room)
   THEN: light_on(living_room)
   ```
   Nếu phát hiện chuyển động → bật đèn

3. **Auto_AC_On**
   ```
   IF: high_temperature()
   THEN: ac_on()
   ```
   Nếu nhiệt độ cao → bật điều hòa

4. **Away_Mode_Activated**
   ```
   IF: no_person_home()
   THEN: door_locked() ∧ energy_saving_mode()
   ```
   Nếu vắng nhà → khóa cửa và chế độ tiết kiệm

**Kết luận** (Inferred Facts):
```
⚫ Original: person_home(), dark(), temperature(20)
🟢 Inferred: light_on() ← từ quy tắc 1
🟢 Inferred: light_on() ← từ quy tắc 2 (cũng kết luận này)
```

### File code

- **logic/rules.py**: Định nghĩa Predicate, Rule, KnowledgeBase
- **logic/inference.py**: Implement LogicInferenceEngine + Forward Chaining

### Cách sử dụng

```python
from logic.rules import create_smart_home_kb
from logic.inference import run_inference

# Tạo knowledge base
kb = create_smart_home_kb()

# Chạy inference
run_inference(kb)
```

---

## PART 2: STRIPS PLANNING

### Khái niệm

#### 1. Atom (Vị từ cơ bản)
Giống Predicate nhưng dùng cho STRIPS planning.

```python
Atom("light_on", [])
Atom("person_home", [])
```

#### 2. Action (Hành động)
Biểu diễn một hành động STRIPS.

```python
action = Action(
    name="turn_on_light",
    preconditions=[Atom("dark", []), Atom("person_home", [])],
    effects=[
        (Atom("light_on", []), True),   # Thêm light_on
        (Atom("light_off", []), False)  # Xóa light_off
    ]
)
```

**Cấu trúc**:
- `name`: Tên hành động
- `preconditions`: Điều kiện tiên quyết (phải có để thực thi)
- `effects`: Kết quả (tuples của (atom, True/False))
  - `True` = Thêm atom vào state
  - `False` = Xóa atom khỏi state

#### 3. State (Trạng thái)
Tập hợp các atoms biểu diễn trạng thái của thế giới.

```
Initial State: {person_home, dark, light_off, ac_off, door_unlocked}
Goal State:    {person_home, light_on, ac_off, door_locked}
```

#### 4. STRIPSPlanner (Bộ lập kế hoạch)
Tìm chuỗi hành động từ initial state → goal state.

```
Thuật toán: BFS (Breadth-First Search)

1. Khởi tạo: queue = [(initial_state, [])]

2. Lặp:
   - Lấy (state, plan) từ queue
   - Nếu state == goal: return plan ✓
   - Nếu depth > max_depth: skip
   - Với mỗi hành động có thể áp dụng:
       - Tính state mới = apply_action(state)
       - Nếu chưa explore: thêm vào queue

3. Nếu queue rỗng: return None (không có kế hoạch)
```

### Ứng dụng: Smart Home Planning

**Bài toán**: Lập kế hoạch hành động để từ trạng thái ban đầu đạt mục tiêu

**Trạng thái ban đầu**:
```
- person_home()
- dark()
- light_off()
- ac_off()
- door_unlocked()
- security_disarmed()
- low_temperature()
```

**Mục tiêu**:
```
- person_home()      ← phải giữ
- light_on()         ← cần bật đèn
- ac_off()           ← phải giữ
- door_locked()      ← cần khóa cửa
```

**Hành động có sẵn**:
```
1. turn_on_light
   Preconditions: [dark(), person_home()]
   Effects: [+light_on(), -light_off()]

2. lock_door
   Preconditions: [person_home()]
   Effects: [+door_locked(), -door_unlocked()]

3. arm_security
   Preconditions: [person_away(), door_locked()]
   Effects: [+security_armed(), -security_disarmed()]

... (8 hành động tổng cộng)
```

**Kế hoạch tìm được** (3 bước):
```
Step 1: turn_on_light
  ✓ Precondition: dark() ✓, person_home() ✓
  → New state: light_on() added

Step 2: lock_door
  ✓ Precondition: person_home() ✓
  → New state: door_locked() added

Step 3: (Mục tiêu đã đạt, không cần bước thêm)
```

**Trạng thái cuối cùng**:
```
✓ person_home()  ✓ light_on()  ✓ door_locked()  ✓ security_disarmed()
✓ GOAL REACHED!
```

### File code

- **planning/strips.py**: Implement Atom, Action, STRIPSPlanner
- **planning/domain.py**: Định nghĩa domain (actions) cho bài toán
- **planning/planner.py**: Chạy planning với BFS/DFS

### Cách sử dụng

```python
from planning.domain import create_smart_home_domain
from planning.strips import STRIPSPlanner

# Lấy domain
domain = create_smart_home_domain()
actions = domain["actions"]

# Tạo planner
planner = STRIPSPlanner(initial_state, goal_state, actions)

# Tìm kế hoạch
plan = planner.find_plan(method="bfs", max_depth=10)

# Thực thi
if plan:
    executor = PlanExecutor(plan)
    final_state = executor.execute_all(initial_state)
```

---

## Sự khác biệt giữa Part 1 và Part 2

### Part 1: Logic Inference
- **Input**: Cơ sở kiến thức (facts + rules)
- **Process**: Áp dụng quy tắc → suy ra sự kiện mới
- **Output**: Tất cả sự kiện (original + inferred)
- **Ứng dụng**: Tự động hóa dựa trên quy tắc logic

### Part 2: STRIPS Planning
- **Input**: Trạng thái ban đầu + mục tiêu + hành động
- **Process**: Tìm chuỗi hành động từ initial → goal
- **Output**: Kế hoạch (danh sách hành động)
- **Ứng dụng**: Lập kế hoạch để đạt mục tiêu

---

## Chạy M4

### Cách 1: Menu chính
```powershell
python main.py
```
Chọn **2** hoặc **3**

### Cách 2: Demo riêng
```powershell
python demo_m4.py
```

### Cách 3: Chạy riêng phần
```python
# Chỉ logic
python -c "from logic.rules import create_smart_home_kb; from logic.inference import run_inference; run_inference(create_smart_home_kb())"

# Chỉ planning
python -c "from planning.planner import run_smart_home_planning; run_smart_home_planning()"
```

---

## Cấu trúc thư mục M4

```
AI/
├── logic/
│   ├── __init__.py
│   ├── rules.py          ← Predicate, Rule, KnowledgeBase
│   └── inference.py      ← LogicInferenceEngine, Forward Chaining
├── planning/
│   ├── __init__.py
│   ├── strips.py         ← Atom, Action, STRIPSPlanner
│   ├── domain.py         ← Định nghĩa domain & actions
│   └── planner.py        ← Chạy planning
├── demo_m4.py            ← Demo riêng từng phần
└── MEMBER_M4.md          ← File này
```

---

## Kết luận

- **M4 Part 1**: Mô phỏng tự động hóa nhà thông minh dùng logic + suy luận
- **M4 Part 2**: Lập kế hoạch AI để đạt mục tiêu từ một trạng thái ban đầu
- Cả hai phần đều sử dụng biểu diễn logic (FOL - First Order Logic)
- Có thể mở rộng cho nhiều bài toán khác (logistics, robot planning, v.v.)
