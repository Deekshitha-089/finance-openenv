from env.environment import FinanceEnv

env = FinanceEnv()

def smart_policy(state):
    balance = state["balance"]
    savings = state["savings"]
    expenses = state["expenses"]

    # Priority 1: Build savings safety net
    if savings < 5000:
        return "save"

    # Priority 2: Avoid overspending
    if expenses > 7000:
        return "save"

    # Priority 3: Invest only if stable
    if balance > 10000:
        return "invest"

    # Fallback
    return "save"


def run_task(task_name):
    state = env.reset()
    total_reward = 0

    print(f"\nRunning {task_name}...")

    for step in range(10):
        action = smart_policy(state)
        state, reward, done, _ = env.step(action)

        print(f"Step {step+1}: Action={action}, Reward={reward}, State={state}")

        total_reward += reward

        # Risk control: stop if balance too low
        if state["balance"] < 5000:
            break

    score = min(max(total_reward / 10, 0), 1)
    print(f"{task_name.upper()} TASK SCORE: {score}")
    return score


def main():
    scores = {}
    for task in ["easy", "medium", "hard"]:
        scores[task] = run_task(task)

    print("\nFINAL SCORES:", scores)


if __name__ == "__main__":
    main()