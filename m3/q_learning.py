import random

from m3.environment import GridEnvironment


def create_q_table(env):
    """
    Khoi tao bang Q cho moi state hop le va 4 hanh dong.
    """
    q_table = {}
    for state in env.iter_states():
        q_table[state] = {action: 0.0 for action in env.ACTIONS}
    return q_table


def epsilon_greedy_action(env, q_table, state, epsilon):
    if random.random() < epsilon:
        return random.choice(list(env.ACTIONS.keys()))

    state_actions = q_table[state]
    max_q = max(state_actions.values())
    best_actions = [action for action, value in state_actions.items() if value == max_q]
    return random.choice(best_actions)


def extract_greedy_path(env, q_table, max_steps=50):
    state = env.reset()
    path = [state]
    visited = {state}

    for _ in range(max_steps):
        action = epsilon_greedy_action(env, q_table, state, epsilon=0.0)
        next_state, _, done = env.step(action)

        if next_state != path[-1]:
            path.append(next_state)

        if done:
            return path, True

        if next_state in visited:
            return path, False

        visited.add(next_state)
        state = next_state

    return path, False


def run_q_learning(
    episodes=500,
    max_steps=50,
    alpha=0.1,
    gamma=0.9,
    epsilon=1.0,
    epsilon_decay=0.995,
    epsilon_min=0.05,
    seed=42,
):
    """
    Huan luyen Q-learning va tra ve log + Q-table + duong di cuoi.
    """
    random.seed(seed)
    env = GridEnvironment()
    q_table = create_q_table(env)

    reward_history = []
    step_history = []
    success_history = []

    for _ in range(episodes):
        state = env.reset()
        total_reward = 0
        reached_goal = False

        for step in range(1, max_steps + 1):
            action = epsilon_greedy_action(env, q_table, state, epsilon)
            next_state, reward, done = env.step(action)

            old_q = q_table[state][action]
            next_max = max(q_table[next_state].values())
            q_table[state][action] = old_q + alpha * (
                reward + gamma * next_max - old_q
            )

            total_reward += reward
            state = next_state

            if done:
                reached_goal = True
                step_history.append(step)
                break
        else:
            step_history.append(max_steps)

        reward_history.append(total_reward)
        success_history.append(reached_goal)
        epsilon = max(epsilon_min, epsilon * epsilon_decay)

    learned_path, solved = extract_greedy_path(env, q_table, max_steps=max_steps)

    return {
        "q_table": q_table,
        "reward_history": reward_history,
        "step_history": step_history,
        "success_history": success_history,
        "successful_episodes": sum(success_history),
        "learned_path": learned_path if solved else None,
        "solved": solved,
    }
