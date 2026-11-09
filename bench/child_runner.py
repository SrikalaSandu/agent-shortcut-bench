"""Runs one test module in an isolated subprocess and reports results.

Usage: python child_runner.py <test_module_name>
The nonce is read from stdin before the solution is imported, so a solution that
prints fake results cannot know which marker the parent will accept.
"""
import importlib
import json
import os
import sys
import traceback


def main():
    sys.path.insert(0, os.getcwd())  # parent runs us with -I, which drops the cwd
    nonce = sys.stdin.readline().strip()
    module_name = sys.argv[1]
    results = {}
    try:
        module = importlib.import_module(module_name)
    except BaseException as exc:  # includes SystemExit raised during import
        results["<import>"] = {"passed": False, "error": f"{type(exc).__name__}: {exc}"}
        print(nonce + json.dumps(results), flush=True)
        return

    for name in sorted(dir(module)):
        if not name.startswith("test_"):
            continue
        fn = getattr(module, name)
        if not callable(fn):
            continue
        try:
            fn()
            results[name] = {"passed": True}
        except BaseException as exc:
            tb = traceback.format_exc(limit=1).strip().splitlines()[-1]
            results[name] = {"passed": False, "error": tb or type(exc).__name__}
    print(nonce + json.dumps(results), flush=True)


if __name__ == "__main__":
    main()
