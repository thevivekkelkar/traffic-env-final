import os
import random
from fastapi import FastAPI
from traffic_env import TrafficEnvironment

app = FastAPI()
env = TrafficEnvironment()

@app.post("/reset")
def reset():
    state = env.reset()
    return {"observation": state}

@app.post("/step")
def step(body: dict):
    action = body.get("action", 0)
    next_state, reward, done = env.step(action)
    return {
        "observation": next_state,
        "reward": reward,
        "done": done,
        "info": {}
    }

@app.get("/state")
def state():
    return {"state": env.state()}

@app.get("/health")
def health():
    return {"status": "ok"}
