from __future__ import annotations

from pathlib import Path


class Agent:
    """An agent gets a workspace containing prompt.md, solution.py and tests_visible.py.

    It may read and write any file in the workspace. Only solution.py is graded,
    but every change is recorded, which is how test tampering is detected.
    """

    name = "base"

    def solve(self, workspace: Path, task) -> dict:
        """Work on the task in-place. Return any metadata worth logging (e.g. turns used)."""
        raise NotImplementedError
