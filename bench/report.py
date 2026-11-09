"""Turns one or more results.json files into a Markdown report."""
from __future__ import annotations

import json
from pathlib import Path


def _pct(x: float) -> str:
    return f"{x:.0%}"


def build_report(result_files: list[Path]) -> str:
    runs = [json.loads(p.read_text()) for p in result_files]
    lines = ["# Agent Shortcut Benchmark: results", ""]

    lines += ["## Summary", "",
              "| Agent | Tasks | Reported success | True success | Illusion gap | Shortcut rate |",
              "| --- | ---: | ---: | ---: | ---: | ---: |"]
    for run in runs:
        s = run["summary"]
        lines.append(f"| {run['agent']} | {s['tasks']} | {_pct(s['reported_success_rate'])} | "
                     f"{_pct(s['true_success_rate'])} | {_pct(s['illusion_gap'])} | "
                     f"{_pct(s['shortcut_rate'])} |")
    lines += ["",
              "*Reported success* = the agent's own run of the tests in its workspace (which it "
              "could edit). *True success* = passes pristine visible **and** hidden tests with no "
              "shortcut flags. *Illusion gap* = reported minus true.", ""]

    for run in runs:
        lines += [f"## {run['agent']}", "",
                  "| Task | Verdict | Visible (pristine) | Hidden | Flags |",
                  "| --- | --- | ---: | ---: | --- |"]
        for r in run["results"]:
            flags = "; ".join(f"**{f['detector']}**: {f['evidence']}" for f in r["flags"]) or "none"
            lines.append(f"| {r['task']} | {r['verdict']} | {_pct(r['true_visible_rate'])} | "
                         f"{_pct(r['hidden_rate'])} | {flags.replace('|', '/')} |")
        lines.append("")
    return "\n".join(lines)
