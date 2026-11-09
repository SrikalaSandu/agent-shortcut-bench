"""Command-line entry point.

Examples:
  python run.py --agent reference
  python run.py --agent shortcut
  python run.py --agent llm --provider anthropic --model <model-id> --pressure high
  python run.py --report results/*/results.json
"""
import argparse
from pathlib import Path

from bench.agents import make_agent
from bench.report import build_report
from bench.runner import run, save


def main():
    parser = argparse.ArgumentParser(description="Agent Shortcut Benchmark")
    parser.add_argument("--agent", choices=["reference", "shortcut", "llm"])
    parser.add_argument("--provider", default="anthropic", choices=["anthropic", "openai"])
    parser.add_argument("--model", help="model id for --agent llm (or set BENCH_MODEL)")
    parser.add_argument("--pressure", default="low", choices=["low", "high"])
    parser.add_argument("--max-turns", type=int, default=12)
    parser.add_argument("--tasks", nargs="*", help="subset of task names")
    parser.add_argument("--keep-workspaces", action="store_true")
    parser.add_argument("--report", nargs="*", type=Path,
                        help="build a Markdown report from results.json files")
    args = parser.parse_args()

    if args.report:
        out = Path("results/REPORT.md")
        out.parent.mkdir(exist_ok=True)
        out.write_text(build_report(args.report))
        print(f"Report written to {out}")
        return

    if not args.agent:
        parser.error("--agent is required unless --report is given")
    kwargs = {}
    if args.agent == "llm":
        kwargs = dict(provider=args.provider, model=args.model,
                      max_turns=args.max_turns, pressure=args.pressure)
    agent = make_agent(args.agent, **kwargs)
    print(f"Running {agent.name}")
    result = run(agent, args.tasks, args.keep_workspaces)
    out_dir = save(result)
    s = result["summary"]
    print(f"\nTrue success {s['true_success_rate']:.0%} | reported {s['reported_success_rate']:.0%} "
          f"| illusion gap {s['illusion_gap']:.0%} | shortcut rate {s['shortcut_rate']:.0%}")
    print(f"Saved to {out_dir / 'results.json'}")


if __name__ == "__main__":
    main()
