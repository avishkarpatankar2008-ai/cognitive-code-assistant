from pydantic import BaseModel
from grader import grade_action
from tasks import TASKS

VALID_ACTIONS = {"hint", "restore_context", "simplify", "explain_error"}

class Observation(BaseModel):
    code_snapshot: str = ""
    errors: str = ""
    progress_score: float = 0.0
    context_lost: bool = False
    task_id: str = ""
    task_description: str = ""
    attempts: int = 0
    done: bool = False

class Action(BaseModel):
    action_type: str
    message: str = ""

class CognitiveDevAssistantEnv:

    def __init__(self, task_id="easy"):
        self.task_id = task_id
        self.reset()

    def reset(self):
        self.data = dict(TASKS[self.task_id]["initial_state"])
        self.attempts = 0
        self.done = False
        return self._obs()

    def step(self, action: Action):
        self.attempts += 1

        score, breakdown = grade_action(
            self.task_id, self.data, action, self.attempts
        )

        reward = max(0, min(1, score))

        if reward > 0.3:
            self.data["progress_score"] += 0.3

        if self.data["progress_score"] >= 1:
            self.data["solved"] = True
            self.done = True

        return self._obs(), reward, self.done, {"breakdown": breakdown}

    def state(self):
        return self.data

    def _obs(self):
        return Observation(
            code_snapshot=self.data.get("code_snapshot", ""),
            errors=self.data.get("errors", ""),
            progress_score=self.data.get("progress_score", 0),
            context_lost=self.data.get("context_lost", False),
            task_id=self.task_id,
            task_description=TASKS[self.task_id]["description"],
            attempts=self.attempts,
            done=self.done
        )