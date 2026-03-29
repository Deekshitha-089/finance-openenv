from fastapi import FastAPI
from env.environment import FinanceEnv

app = FastAPI()
env = FinanceEnv()

@app.get("/")
def home():
    return {"message": "Finance OpenEnv running"}

@app.post("/reset")
def reset_post():
    return env.reset()

@app.get("/reset")
def reset_get():
    return env.reset()

@app.get("/state")
def state():
    return env.state()

@app.post("/step")
def step(action: str):
    state, reward, done, _ = env.step(action)
    return {
        "state": state,
        "reward": reward,
        "done": done
    }