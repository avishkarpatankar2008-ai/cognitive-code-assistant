# Cognitive Developer Assistant (OpenEnv)

## Overview
Simulates real-world developer workflows:
- Detects when developer is stuck
- Restores lost context
- Simplifies overengineered code

## Tasks
- Easy: Stuck detection
- Medium: Context recovery
- Hard: Code simplification

## Action Space
- hint
- restore_context
- simplify
- explain_error

## Observation Space
- code_snapshot
- errors
- progress_score
- context_lost

## Reward
- Correct action: +0.5
- Helpful message: +0.3
- Wrong action: -0.2
- Range: 0.0 – 1.0

## Setup
```bash
pip install -r requirements.txt
python inference.py