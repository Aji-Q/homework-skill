r"""Split an echoed console transcript into one file per assignment sub-part.

The analysis script carries section markers that survive echo, one per sub-part:

    ## ------------------------------------------------------------------ 1(a)

Everything between two markers becomes <out_dir>/<slug>.txt, ready for \VerbatimInput.
The slug lowercases the label, drops parentheses and turns every other run of
non-alphanumerics into "_", so "1(a)" -> 1a.txt and "5 (picture)" -> 5_picture.txt.
An interpreter prompt in front of the marker ("> ", ">>> ", "In [3]: ", "julia> ") is
tolerated.

Text is passed through unchanged by default. XeTeX and LuaTeX -- and therefore tectonic --
typeset UTF-8 inside verbatim correctly, including a Unicode minus and Greek letters; only
CJK needs a font that has the glyphs (xeCJK, or fontspec with a CJK family). Under pdfLaTeX,
non-ASCII in verbatim fails to compile: pass --ascii to fold it, which reports every
substitution rather than silently mangling a number.

    python3 split_transcript.py transcript.txt chunk
    python3 split_transcript.py transcript.txt chunk --ascii --clean
"""
import argparse
import os
import re
import sys
import unicodedata

PROMPT = r"(?:>\s|>>>\s|\.\.\.\s|In \[\d+\]:\s|julia>\s|octave:\d+>\s)?"
MARKER = re.compile(r"^" + PROMPT + r"##\s*-{3,}\s*(.+?)\s*$")
FOLD = {"‘": "'", "’": "'", "“": '"', "”": '"', "–": "-",
        "—": "--", "…": "...", " ": " ", "µ": "mu", "±": "+/-",
        "×": "x", "−": "-", "≤": "<=", "≥": ">=", "≠": "!=",
        "∞": "Inf"}


def slugify(label):
    return re.sub(r"[^a-z0-9]+", "_", label.lower().replace("(", "").replace(")", "")).strip("_")


def fold_line(line, lineno, report):
    out = []
    for col, ch in enumerate(line, 1):
        if ord(ch) < 128:
            out.append(ch)
        elif ch in FOLD:
            out.append(FOLD[ch])
        else:
            folded = unicodedata.normalize("NFKD", ch).encode("ascii", "ignore").decode()
            out.append(folded if folded else "?")
            if not folded:
                report.append((lineno, col, ch))
    return "".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("transcript")
    ap.add_argument("out_dir", nargs="?", default="chunk")
    ap.add_argument("--ascii", action="store_true",
                    help="fold non-ASCII to ASCII (needed only for pdfLaTeX)")
    ap.add_argument("--clean", action="store_true",
                    help="delete .txt files in out_dir that this run does not write")
    a = ap.parse_args()

    raw = open(a.transcript, encoding="utf-8", errors="replace").read().splitlines()

    if a.ascii:
        report = []
        lines = [fold_line(l, i, report) for i, l in enumerate(raw, 1)]
        for lineno, col, ch in report:
            print(f"warning: {a.transcript}:{lineno}:{col} U+{ord(ch):04X} {ch!r} "
                  f"has no ASCII form, replaced with '?'", file=sys.stderr)
    else:
        lines = raw
        exotic = sorted({c for l in lines for c in l if ord(c) > 127})
        if exotic:
            print(f"note: transcript contains non-ASCII ({''.join(exotic)}). XeTeX/LuaTeX "
                  f"(tectonic) handle this; CJK additionally needs a CJK font. Under pdfLaTeX, "
                  f"re-run with --ascii.", file=sys.stderr)

    chunks, order, cur, name, preamble = {}, [], [], None, []
    for l in lines:
        m = MARKER.match(l)
        if m:
            if name is not None:
                chunks[name] = cur
                order.append(name)
            name, cur = m.group(1), []
        elif name is None:
            preamble.append(l)
        else:
            cur.append(l)
    if name is not None:
        chunks[name] = cur
        order.append(name)

    if not order:
        sys.exit(f"error: no section markers found in {a.transcript}.\n"
                 f"       Expected lines matching '## ---- <label>', optionally behind an\n"
                 f"       interpreter prompt. Check that the script ran with echo on.")

    slugs = {}
    for label in order:
        s = slugify(label)
        slugs.setdefault(s, []).append(label)
    clashes = {s: v for s, v in slugs.items() if len(v) > 1}
    if clashes:
        detail = "; ".join(f"{s}.txt <- {v}" for s, v in clashes.items())
        sys.exit(f"error: two or more markers map to the same file, so one would silently\n"
                 f"       overwrite the other: {detail}\n"
                 f"       Give each sub-part a distinct label.")

    if preamble and any(l.strip() for l in preamble):
        print(f"warning: {len(preamble)} line(s) before the first marker were discarded "
              f"(imports, data loading, inspection output). Put a marker above them if the "
              f"document should show them.", file=sys.stderr)

    os.makedirs(a.out_dir, exist_ok=True)
    written = set()
    for label in order:
        slug = slugify(label)
        written.add(slug + ".txt")
        body = "\n".join(chunks[label]).strip("\n")
        open(os.path.join(a.out_dir, slug + ".txt"), "w", encoding="utf-8").write(body + "\n")
        print(f"{slug:16s} {len(chunks[label]):4d} lines")

    stale = sorted(f for f in os.listdir(a.out_dir) if f.endswith(".txt") and f not in written)
    for f in stale:
        if a.clean:
            os.remove(os.path.join(a.out_dir, f))
            print(f"removed stale {f}", file=sys.stderr)
        else:
            print(f"warning: {f} is left over from an earlier run and was not rewritten; "
                  f"\\VerbatimInput would show stale output. Re-run with --clean.",
                  file=sys.stderr)


if __name__ == "__main__":
    main()
