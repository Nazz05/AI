import random

from m3.environment import GridEnvironment


def run_random_search(episodes=200, max_steps=50, seed=42):
    """
    Chay baseline Random Search tren GridWorld.
    """
    random.seed(seed)
    env = GridEnvironment()

    best_path = None
    best_steps = None
    successful_episodes = 0
    episode_logs = []

    for episode in range(1, episodes + 1):
        state = env.reset()
        path = [state]
        total_reward = 0
        reached_goal = False

        for step in range(1, max_steps + 1):
            action = random.choice(list(env.ACTIONS.keys()))
            next_state, reward, done = env.step(action)
            total_reward += reward

            if next_state != path[-1]:
                path.append(next_state)

            if done:
                successful_episodes += 1
                reached_goal = True
                if best_path is None or len(path) < len(best_path):
                    best_path = list(path)
                    best_steps = step
                break

        episode_logs.append(
            {
                "episode": episode,
                "reward": total_reward,
                "steps": len(path) - 1,
                "success": reached_goal,
            }
        )

    return {
        "best_path": best_path,
        "best_steps": best_steps,
        "successful_episodes": successful_episodes,
        "episodes": episodes,
        "logs": episode_logs,
    }
