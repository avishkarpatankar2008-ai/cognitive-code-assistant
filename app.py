import os
import json
from openai import OpenAI
from env import Action, CognitiveDevAssistantEnv

client = OpenAI(
    base_url=os.getenv("API_BASE_URL"),
    api_key=os.getenv("HF_TOKEN")
)

POLICY = {
    "easy": Action(action_type="hint", message="Check loop condition and break logic."),
    "medium": Action(action_type="restore_context", message="Resume from checkpoint and continue jwt + logout."),
    "hard": Action(action_type="simplify", message="Use sorted() instead of complex code.")
}

def log(tag, data):
    print(json.dumps({"tag": tag, **data}), flush=True)

def run(task):
    env = CognitiveDevAssistantEnv(task)
    obs = env.reset()

    log("START", {"task": task})

    for i in range(5):
        action = POLICY[task]
        obs, reward, done, info = env.step(action)

        log("STEP", {
            "step": i,
            "reward": reward,
            "done": done
        })

        if done:
            break

    log("END", {"task": task})

def main():
    for t in ["easy", "medium", "hard"]:
        run(t)

if __name__ == "__main__":
    main()