r"""Flag transcript lines too wide for the page.

Over-wide verbatim lines do NOT raise "Overfull \hbox": each line is set in a box that
simply runs into the margin, silently. Console output is exactly the kind of content that
produces such lines, so the compiler's overfull count can be zero while text runs off the
sheet. This measures the lines instead.

A monospace character in the default LaTeX typewriter face is 0.525 em wide, so

    columns = floor(linewidth_pt / (0.525 x fontsize_pt))

For an 11pt article with 1in margins, linewidth is 469.755pt and \footnotesize is 9pt,
giving 99 columns -- measured: a 99-character line clears the margin, a 100-character
line crosses it.

    python3 check_width.py chunk                 # defaults: footnotesize, 11pt, 1in margins
    python3 check_width.py chunk --size 8        # \scriptsize
    python3 check_width.py chunk --linewidth 345 # a4paper with 2.5cm margins, say
"""
import argparse
import glob
import math
import os
import sys

SIZES = {11: {"normalsize": 11, "small": 10, "footnotesize": 9, "scriptsize": 8, "tiny": 6},
         12: {"normalsize": 12, "small": 11, "footnotesize": 10, "scriptsize": 8, "tiny": 6},
         10: {"normalsize": 10, "small": 9, "footnotesize": 8, "scriptsize": 7, "tiny": 5}}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("chunk_dir")
    ap.add_argument("--size", type=float, default=9.0,
                    help="type size in pt of the verbatim text (default 9 = footnotesize in an 11pt class)")
    ap.add_argument("--linewidth", type=float, default=469.755,
                    help="\\linewidth in pt; print it with \\showthe\\linewidth (default: 11pt article, 1in margins)")
    a = ap.parse_args()

    columns = math.floor(a.linewidth / (0.525 * a.size))
    print(f"budget: {columns} columns ({a.linewidth}pt at {a.size}pt monospace)")

    bad = 0
    for path in sorted(glob.glob(os.path.join(a.chunk_dir, "*.txt"))):
        for i, line in enumerate(open(path, encoding="utf-8"), 1):
            n = len(line.rstrip("\n"))
            if n > columns:
                bad += 1
                print(f"{os.path.basename(path)}:{i}  {n} columns (+{n - columns})")
    print("no over-wide lines" if not bad else f"{bad} line(s) over budget")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
