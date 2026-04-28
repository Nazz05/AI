# ===================================
# THUẬT TOÁN STRIPS - LẬP KẾ HOẠCH AI
# ===================================
# STRIPS (Stanford Research Institute Problem Solver)
# Lập kế hoạch bằng cách tìm kiếm để biến đổi trạng thái ban đầu thành trạng thái mục tiêu

from typing import List, Set, Optional, Tuple
from dataclasses import dataclass, field
from copy import deepcopy


@dataclass
class Atom:
    """Biểu diễn một atomic formula (vị từ cơ bản)
    Ví dụ: light_on(), at(robot, location_A)
    """
    name: str
    args: List[str] = field(default_factory=list)
    
    def __hash__(self):
        return hash((self.name, tuple(self.args)))
    
    def __eq__(self, other):
        if not isinstance(other, Atom):
            return False
        return self.name == other.name and self.args == other.args
    
    def __repr__(self):
        if self.args:
            return f"{self.name}({', '.join(self.args)})"
        return self.name


@dataclass
class Action:
    """Biểu diễn một hành động STRIPS
    Cấu trúc: name, preconditions, effects
    """
    name: str
    preconditions: List[Atom] = field(default_factory=list)
    effects: List[Tuple[Atom, bool]] = field(default_factory=list)  # (atom, add_or_delete)
    
    def __repr__(self):
        prec_str = ", ".join(str(p) for p in self.preconditions)
        effects_str = ", ".join(
            f"+{e[0]}" if e[1] else f"-{e[0]}" 
            for e in self.effects
        )
        return f"{self.name}: [{prec_str}] → [{effects_str}]"
    
    def is_applicable(self, state: Set[Atom]) -> bool:
        """Kiểm tra hành động có thể áp dụng được trong trạng thái hiện tại"""
        return all(prec in state for prec in self.preconditions)
    
    def apply(self, state: Set[Atom]) -> Set[Atom]:
        """Áp dụng hành động lên trạng thái, trả về trạng thái mới"""
        new_state = deepcopy(state)
        
        for atom, is_add in self.effects:
            if is_add:
                new_state.add(atom)
            else:
                new_state.discard(atom)
        
        return new_state


@dataclass
class PlanStep:
    """Biểu diễn một bước trong kế hoạch"""
    action: Action
    step_number: int
    
    def __repr__(self):
        return f"Step {self.step_number}: {self.action.name}"


class State:
    """Lớp biểu diễn trạng thái của thế giới"""
    
    def __init__(self, atoms: Set[Atom]):
        self.atoms = atoms
    
    def __hash__(self):
        return hash(frozenset(self.atoms))
    
    def __eq__(self, other):
        if not isinstance(other, State):
            return False
        return self.atoms == other.atoms
    
    def copy(self) -> 'State':
        return State(deepcopy(self.atoms))
    
    def __repr__(self):
        return f"State({len(self.atoms)} atoms)"


class STRIPSPlanner:
    """Thuật toán STRIPS - Lập kế hoạch bằng tìm kiếm đầu tiên theo chiều rộng (BFS)"""
    
    def __init__(self, initial_state: Set[Atom], goal: Set[Atom], actions: List[Action]):
        self.initial_state = initial_state
        self.goal = goal
        self.actions = actions
        self.plan: List[Action] = []
        self.explored_states: Set[State] = set()
        self.action_count = 0
    
    def is_goal_reached(self, state: Set[Atom]) -> bool:
        """Kiểm tra trạng thái hiện tại có đạt mục tiêu không"""
        return self.goal.issubset(state)
    
    def get_applicable_actions(self, state: Set[Atom]) -> List[Action]:
        """Lấy danh sách hành động có thể áp dụng trong trạng thái hiện tại"""
        applicable = []
        for action in self.actions:
            if action.is_applicable(state):
                applicable.append(action)
        return applicable
    
    def breadth_first_search(self, max_depth: int = 20) -> Optional[List[Action]]:
        """
        Tìm kế hoạch bằng BFS (Breadth-First Search)
        
        Args:
            max_depth: Độ sâu tối đa của tìm kiếm
        
        Returns:
            Danh sách hành động (kế hoạch) hoặc None nếu không tìm được
        """
        from collections import deque
        
        # Queue: (state, plan_so_far)
        queue = deque([(self.initial_state, [])])
        visited = {frozenset(self.initial_state)}
        
        while queue:
            current_state, current_plan = queue.popleft()
            
            # Kiểm tra mục tiêu
            if self.is_goal_reached(current_state):
                self.plan = current_plan
                self.action_count = len(current_plan)
                return current_plan
            
            # Hạn chế độ sâu
            if len(current_plan) >= max_depth:
                continue
            
            # Thử tất cả hành động có thể áp dụng
            for action in self.get_applicable_actions(current_state):
                new_state = action.apply(current_state)
                new_state_key = frozenset(new_state)
                
                if new_state_key not in visited:
                    visited.add(new_state_key)
                    new_plan = current_plan + [action]
                    queue.append((new_state, new_plan))
        
        return None
    
    def depth_first_search(self, max_depth: int = 20) -> Optional[List[Action]]:
        """
        Tìm kế hoạch bằng DFS (Depth-First Search)
        Nhanh hơn BFS nhưng có thể tìm thấy kế hoạch không tối ưu
        """
        def dfs(state: Set[Atom], plan: List[Action], depth: int) -> Optional[List[Action]]:
            # Kiểm tra mục tiêu
            if self.is_goal_reached(state):
                return plan
            
            # Hạn chế độ sâu
            if depth >= max_depth:
                return None
            
            # Thử tất cả hành động
            for action in self.get_applicable_actions(state):
                new_state = action.apply(state)
                result = dfs(new_state, plan + [action], depth + 1)
                if result is not None:
                    return result
            
            return None
        
        result = dfs(self.initial_state, [], 0)
        if result:
            self.plan = result
            self.action_count = len(result)
        return result
    
    def find_plan(self, method: str = "bfs", max_depth: int = 20) -> Optional[List[Action]]:
        """
        Tìm kế hoạch sử dụng phương pháp được chỉ định
        
        Args:
            method: "bfs" (Breadth-First) hoặc "dfs" (Depth-First)
            max_depth: Độ sâu tối đa
        
        Returns:
            Danh sách hành động hoặc None
        """
        if method == "bfs":
            return self.breadth_first_search(max_depth)
        elif method == "dfs":
            return self.depth_first_search(max_depth)
        else:
            raise ValueError(f"Unknown method: {method}")
    
    def get_plan_steps(self) -> List[PlanStep]:
        """Trả về kế hoạch dưới dạng danh sách các bước có số thứ tự"""
        return [PlanStep(action, i + 1) for i, action in enumerate(self.plan)]


class PlanExecutor:
    """Thực thi kế hoạch và theo dõi trạng thái"""
    
    def __init__(self, plan: List[Action]):
        self.plan = plan
        self.current_step = 0
    
    def execute_step(self, current_state: Set[Atom]) -> Optional[Set[Atom]]:
        """Thực thi bước tiếp theo của kế hoạch"""
        if self.current_step >= len(self.plan):
            print("✓ Kế hoạch đã hoàn thành!")
            return current_state
        
        action = self.plan[self.current_step]
        
        if action.is_applicable(current_state):
            new_state = action.apply(current_state)
            print(f"Step {self.current_step + 1}: Thực thi '{action.name}' ✓")
            self.current_step += 1
            return new_state
        else:
            print(f"✗ Không thể thực thi '{action.name}': điều kiện tiên quyết không thỏa mãn")
            return None
    
    def execute_all(self, initial_state: Set[Atom]) -> Optional[Set[Atom]]:
        """Thực thi toàn bộ kế hoạch"""
        current_state = deepcopy(initial_state)
        
        for step, action in enumerate(self.plan, 1):
            print(f"\nStep {step}: {action.name}")
            if action.is_applicable(current_state):
                current_state = action.apply(current_state)
                print(f"  ✓ Thực thi thành công")
                print(f"  → Trạng thái mới: {len(current_state)} atoms")
            else:
                print(f"  ✗ LỖI: Điều kiện tiên quyết không thỏa mãn")
                return None
        
        return current_state
