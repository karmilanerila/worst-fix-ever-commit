"""Worst Fix Ever: Funniest Commit Message.

Writes one commit message line to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt). The line must read like a real commit
message about a fix that backfired: the repair itself broke more than
The joke: the "fix" for a noisy error log was to delete error
handling entirely, so the log goes quiet not because anything was
repaired but because nothing can fail loudly any more. Every error
is still happening; none of them can be reported. The repair broke
more than the bug ever did.
"""

import os

LINE = (
    "fix: silence the error log by deleting error handling; "
    "zero errors reported, all of them fatal"
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = LINE.encode("utf-8")
    assert 1 <= len(LINE) <= 100, "line must be 1-100 characters"
    assert LINE.strip(), "line must not be only whitespace"
    with open(path, "wb") as f:
        f.write(data)
    os.chmod(path, 0o644)
    # No trailing newline: the file holds exactly the commit line.
    print("wrote %d characters to %s" % (len(LINE), path))


if __name__ == "__main__":
    main()
