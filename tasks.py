TASKS = {
    "easy": {
        "description": (
            "Developer stuck in loop for long time. Detect and hint."
        ),
        "initial_state": {
            "code_snapshot": (
                "for i in range(10):\n"
                "    result = process(i)\n"
                "    if result == expected:\n"
                "        break\n"
                "# This never terminates correctly"
            ),
            "errors": "AssertionError",
            "progress_score": 0.1,
            "context_lost": False,
            "attempts_before": 7,
            "solved": False,
        },
        "correct_action": "hint",
        "expected_keywords": ["loop", "break", "condition", "result"]
    },

    "medium": {
        "description": "Restore lost developer context",
        "initial_state": {
            "code_snapshot": "def login(): pass",
            "errors": "",
            "progress_score": 0.25,
            "context_lost": True,
            "last_checkpoint": "validate_credentials() extracted",
            "pending_tasks": ["update logout", "add jwt", "tests"],
            "solved": False,
        },
        "correct_action": "restore_context",
        "expected_keywords": ["context", "resume", "checkpoint", "jwt"]
    },

    "hard": {
        "description": "Simplify overengineered sorting code",
        "initial_state": {
            "code_snapshot": "VERY COMPLEX SORTING CODE...",
            "errors": "",
            "progress_score": 0.2,
            "context_lost": False,
            "line_count": 80,
            "solved": False,
        },
        "correct_action": "simplify",
        "expected_keywords": ["sorted", "simple", "overengineered"]
    },
}
