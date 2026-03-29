import os
from env.environment import FinanceEnv
from env.grader import FinanceGrader

def run_task(task_name):
    env = FinanceEnv()
    state = env.reset()

    print(f"\nRunning {task_name}...")

    for step in range(10):
        # simple logic (no AI needed)
        if state["savings"] < 5000:
            action = "save"
        elif state["balance"] < 20000:
            action = "invest"
        else:
            action = "save"

        state, reward, done, _ = env.step(action)

        print(f"Step {step+1}: Action={action}, Reward={reward}, State={state}")

        if done:
            break

    # grading
    if task_name == "easy":
        score = FinanceGrader.grade_easy(env)
    elif task_name == "medium":
        score = FinanceGrader.grade_medium(env)
    else:
        score = FinanceGrader.grade_hard(env)

    print(f"{task_name.upper()} TASK SCORE: {score}\n")
    return score


if __name__ == "__main__":
    scores = {}

    scores["easy"] = run_task("easy")
    scores["medium"] = run_task("medium")
    scores["hard"] = run_task("hard")

    print("FINAL SCORES:", scores)