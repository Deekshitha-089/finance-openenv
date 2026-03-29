from env.environment import FinanceEnv

env = FinanceEnv()

def smart_policy(state, last_reward):
    balance = state["balance"]
    savings = state["savings"]
    expenses = state["expenses"]

    # 1. Build safety first
    if savings < 5000:
        return "save"

    # 2. If last action lost money → play safe
    if last_reward < 0:
        return "save"

    # 3. Invest only if stable and safe
    if balance > 10000 and savings >= 5000:
        return "invest"

    # 4. Maintain balance
    return "save"


def run_task(task_name):
    state = env.reset()
    total_reward = 0
    last_reward = 0

    print(f"\nRunning {task_name}...")

    for step in range(10):
        action = smart_policy(state, last_reward)
        state, reward, done, _ = env.step(action)

        print(f"Step {step+1}: Action={action}, Reward={reward}, State={state}")

        total_reward += reward
        last_reward = reward

        # stop if balance too low
        if state["balance"] < 4000:
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
