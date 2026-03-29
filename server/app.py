from fastapi import FastAPI
from env.environment import FinanceEnv

app = FastAPI()
env = FinanceEnv()

@app.get("/")
def home():
    return {"message": "Finance OpenEnv running"}

@app.api_route("/reset", methods=["GET", "POST"])
def reset():
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

def main():
    return app

if __name__ == "__main__":
    main()