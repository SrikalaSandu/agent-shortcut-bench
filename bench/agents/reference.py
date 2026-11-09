"""Honest baseline: writes a correct, general solution. Should never be flagged."""
from pathlib import Path

from .base import Agent

SOLUTIONS = Path(__file__).resolve().parent / "reference_solutions"


class ReferenceAgent(Agent):
    name = "reference"

    def solve(self, workspace: Path, task) -> dict:
        (workspace / "solution.py").write_text((SOLUTIONS / f"{task.name}.py").read_text())
        return {"strategy": "correct general solution"}
