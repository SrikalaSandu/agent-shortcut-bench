from .base import Agent
from .reference import ReferenceAgent
from .shortcut import ShortcutAgent


def make_agent(name: str, **kwargs) -> Agent:
    if name == "reference":
        return ReferenceAgent()
    if name == "shortcut":
        return ShortcutAgent()
    if name == "llm":
        from .llm import LLMAgent  # imported lazily so the SDKs are optional
        return LLMAgent(**kwargs)
    raise SystemExit(f"Unknown agent: {name}")
