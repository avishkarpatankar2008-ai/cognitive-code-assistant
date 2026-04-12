from fastapi import FastAPI
from env import CognitiveDevAssistantEnv
from pydantic import BaseModel

app = FastAPI()

env = None

# Define action model (important for POST /step)
class Action(BaseModel):
    action_type: str
    content: str = ""

@app.post("/reset")
def reset():
    global env
    env = CognitiveDevAssistantEnv("easy")
    obs = env.reset()
    return obs.dict()

@app.post("/step")
def step(action: Action):
    global env
    obs, reward, done, info = env.step(action)
    return {
        "observation": obs.dict(),
        "reward": reward,
        "done": done,
        "info": info
    }

@app.get("/state")
def state():
    return env.state().dict()
