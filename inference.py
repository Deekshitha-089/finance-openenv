from fastapi import FastAPI
from pydantic import BaseModel
from env.environment import FinanceEnv

app = FastAPI()

env = FinanceEnv()


# -------- INPUT FORMAT --------
class InputData(BaseModel):
    task: str   # "easy", "medium", "hard"


# -------- YOUR SMART POLICY --------
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


# -------- CORE RUN FUNCTION --------
def run_task(task_name):
    state = env.reset()
    total_reward = 0
    last_reward = 0

    for step in range(10):
        action = smart_policy(state, last_reward)
        state, reward, done, _ = env.step(action)

        total_reward += reward
        last_reward = reward

        if state["balance"] < 4000:
            break

    score = min(max(total_reward / 10, 0), 1)
    return score


# -------- ROOT CHECK --------
@app.get("/")
def home():
    return {"message": "Finance OpenEnv API running"}


# -------- REQUIRED ENDPOINT --------
@app.post("/predict")
def predict(data: InputData):
    task = data.task.lower()

    if task not in ["easy", "medium", "hard"]:
        return {"error": "Invalid task"}

    score = run_task(task)

    return {
        "task": task,
        "score": score
    }