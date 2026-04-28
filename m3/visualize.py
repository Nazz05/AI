import matplotlib.pyplot as plt


def plot_training_results(reward_history, step_history, success_history):
    """
    Ve do thi reward, so buoc va ti le thanh cong tich luy.
    """
    episodes = list(range(1, len(reward_history) + 1))
    cumulative_success = []
    success_count = 0

    for index, success in enumerate(success_history, start=1):
        if success:
            success_count += 1
        cumulative_success.append(success_count / index)

    plt.figure(figsize=(12, 8))

    plt.subplot(3, 1, 1)
    plt.plot(episodes, reward_history, color="tab:blue")
    plt.title("Q-learning Training Metrics")
    plt.ylabel("Reward")
    plt.grid(True, alpha=0.3)

    plt.subplot(3, 1, 2)
    plt.plot(episodes, step_history, color="tab:orange")
    plt.ylabel("Steps")
    plt.grid(True, alpha=0.3)

    plt.subplot(3, 1, 3)
    plt.plot(episodes, cumulative_success, color="tab:green")
    plt.xlabel("Episode")
    plt.ylabel("Success Rate")
    plt.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()


def print_q_table(q_table):
    """
    In bang Q ra terminal de dua vao bao cao.
    """
    print("\nQ-TABLE:")
    print("=" * 70)
    for state in sorted(q_table):
        actions = q_table[state]
        formatted = ", ".join(
            f"{action}: {value:.2f}" for action, value in actions.items()
        )
        print(f"{state} -> {formatted}")
