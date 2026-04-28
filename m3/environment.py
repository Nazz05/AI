from core.grid import GridWorld
from config import GOAL, GRID, START


class GridEnvironment:
    """
    Moi truong GridWorld don gian cho Random Search va Q-learning.
    """

    ACTIONS = {
        0: (-1, 0),  # up
        1: (1, 0),   # down
        2: (0, -1),  # left
        3: (0, 1),   # right
    }

    ACTION_NAMES = {
        0: "UP",
        1: "DOWN",
        2: "LEFT",
        3: "RIGHT",
    }

    def __init__(self, grid=None, start=None, goal=None):
        self.grid = GridWorld(grid or GRID)
        self.start = start or START
        self.goal = goal or GOAL
        self.state = self.start

    def reset(self):
        self.state = self.start
        return self.state

    def get_valid_actions(self, state=None):
        current = state or self.state
        valid_actions = []

        for action, (dx, dy) in self.ACTIONS.items():
            nx = current[0] + dx
            ny = current[1] + dy
            if self.grid.is_valid(nx, ny):
                valid_actions.append(action)

        return valid_actions

    def step(self, action):
        dx, dy = self.ACTIONS[action]
        nx = self.state[0] + dx
        ny = self.state[1] + dy

        if not self.grid.is_valid(nx, ny):
            return self.state, -5, False

        self.state = (nx, ny)
        if self.state == self.goal:
            return self.state, 100, True

        return self.state, -1, False

    def iter_states(self):
        for row in range(self.grid.rows):
            for col in range(self.grid.cols):
                if self.grid.is_valid(row, col):
                    yield (row, col)
