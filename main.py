"""Dad Joke Showdown entry.

Writes a single dad joke (at most 200 characters) to entry.txt in the
output directory the grader provides, and prints it for the log.

Output directory order, as the make.fun preflight requires:
1. $MAKEFUN_OUTPUT_DIR when it is set,
2. /output when it exists (or can be created),
3. a local "output" directory next to this file, only as a last resort.
"""

import os
import sys
from pathlib import Path

JOKE = (
    "My dad planted a money tree in the garden. "
    "He says it's the only investment that really grows on him."
)


def resolve_output_dir() -> Path:
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip()
    if env_dir:
        return Path(env_dir)
    if os.path.isdir("/output"):
        return Path("/output")
    try:
        os.makedirs("/output", exist_ok=True)
        return Path("/output")
    except OSError:
        return Path(__file__).resolve().parent / "output"


def main() -> int:
    joke = JOKE.strip()
    if not 1 <= len(joke) <= 200:
        print(f"joke is {len(joke)} characters, must be 1-200", file=sys.stderr)
        return 1
    out_dir = resolve_output_dir()
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(joke, encoding="utf-8")
    if target.read_text(encoding="utf-8") != joke:
        print("written entry does not match the joke", file=sys.stderr)
        return 1
    print(joke)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
