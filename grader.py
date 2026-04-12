from tasks import TASKS

def grade_action(task_id, task_data, action, attempts):
    task = TASKS.get(task_id, {})
    correct_action = task.get("correct_action", "")
    keywords = task.get("expected_keywords", [])

    at = action.action_type
    msg = action.message.lower()

    score = 0.0
    breakdown = {}

    # Correct action
    if at == correct_action:
        score += 0.5
        breakdown["correct"] = 0.5
    else:
        score -= 0.2
        breakdown["wrong"] = -0.2

    # Message quality
    if msg:
        hits = sum(1 for k in keywords if k in msg)
        ratio = hits / len(keywords) if keywords else 0

        if ratio > 0.3:
            score += 0.3
            breakdown["message"] = 0.3
        else:
            score += 0.05
            breakdown["weak_msg"] = 0.05
    else:
        score -= 0.1
        breakdown["no_msg"] = -0.1

    return score, breakdown