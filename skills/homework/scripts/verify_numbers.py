r"""Cross-check every number in the document prose against the console output.

Two things make a naive check pass when it should not, and both are handled here.

Echoed source is not output. A transcript captured with echo on contains the code as
well as its results, so a number that only ever appears in a line of source -- a literal
in an unused assignment, a tolerance, a seed -- would otherwise satisfy a claim about a
result. Lines carrying an interpreter prompt are excluded.

A number belongs to a sub-part. Checking against the whole transcript lets a value from
Problem 1 satisfy a sentence about Problem 8. When a chunk directory is given, each
number is checked against the chunks included in its own section first; a hit somewhere
else is reported separately, because prose does sometimes quote an earlier result, and
that is for a human to confirm.

A prose value with d decimals counts as found when some printed number is within half a
unit of its last shown digit, which covers rounding and scientific notation on the
transcript side. Signs are compared: a minus in front makes the prose number negative,
unless a second dash precedes it, which reads as a range.

Known blind spot: a value typeset as 1.2345\times10^{-7} is compared as 1.2345, because
the exponent is markup rather than digits. Check those by hand.

    python3 verify_numbers.py solutions.tex chunk            # per-section, preferred
    python3 verify_numbers.py solutions.tex transcript.txt   # flat fallback
    python3 verify_numbers.py solutions.tex book.xlsx        # values come from a workbook

A workbook source is read for its CACHED values, which is what the grader opens the file
to. Volatile formulas are reported: any figure resting on one is a single draw and the
document must say so, or the next recalculation contradicts it.
"""
import os
import re
import sys

VOLATILE = re.compile(r"\b(RAND|RANDBETWEEN|RANDARRAY|NOW|TODAY|OFFSET|INDIRECT|CELL|INFO)\s*\(", re.I)

PROMPT = re.compile(r"^(?:>>>|\.\.\.|>|\+|In \[\d+\]:|julia>|octave:\d+>)(?:\s|$)")
NUM = re.compile(r"[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?")
PROSE_NUM = re.compile(r"(?<![\w.])(\d+\.\d{3,})")
INCLUDE = re.compile(r"\\(?:Rin|VerbatimInput|lstinputlisting)\s*(?:\[[^\]]*\])?\{([^}]*)\}")
SECTION = re.compile(r"\\(?:sub)*section\*?\{")


def output_numbers(text):
    vals = []
    for line in text.splitlines():
        if PROMPT.match(line):
            continue
        for m in NUM.finditer(line):
            try:
                vals.append(float(m.group(0)))
            except ValueError:
                pass
    return vals


def signed(text, start, digits):
    if start > 0 and text[start - 1] == "-":
        if start < 2 or text[start - 2] not in "-0123456789":
            return -float(digits)
    return float(digits)


def load_workbook_values(path):
    """Cached cell values, plus a count of the volatile formulas behind them."""
    try:
        import openpyxl
    except ImportError:
        sys.exit("reading a workbook needs openpyxl: python3 -m pip install openpyxl")
    keep = path.lower().endswith(".xlsm")
    vals, volatile = [], []
    wbv = openpyxl.load_workbook(path, data_only=True, keep_vba=keep)
    for ws in wbv:
        for row in ws.iter_rows():
            for c in row:
                if isinstance(c.value, (int, float)) and not isinstance(c.value, bool):
                    vals.append(float(c.value))
    wbf = openpyxl.load_workbook(path, data_only=False, keep_vba=keep)
    for ws in wbf:
        for row in ws.iter_rows():
            for c in row:
                if isinstance(c.value, str) and VOLATILE.search(c.value):
                    volatile.append(f"{ws.title}!{c.coordinate}")
    return vals, volatile


def load(source):
    """-> {name: [numbers printed under that name]}; one bucket named '' for a flat file."""
    if source.lower().endswith((".xlsx", ".xlsm")):
        vals, volatile = load_workbook_values(source)
        if volatile:
            print(f"volatile formulas in {os.path.basename(source)}: {len(volatile)} "
                  f"(e.g. {', '.join(volatile[:3])}). Any quoted value resting on one is a "
                  f"single draw; say so in the document or it will not survive a recalculation.")
        return {"": vals}
    if os.path.isdir(source):
        out = {}
        for f in sorted(os.listdir(source)):
            if f.endswith(".txt"):
                out[os.path.splitext(f)[0]] = output_numbers(
                    open(os.path.join(source, f), encoding="utf-8").read())
        return out
    return {"": output_numbers(open(source, encoding="utf-8").read())}


def main(tex_path, sources, min_decimals=3):
    tex = open(tex_path, encoding="utf-8").read()
    if isinstance(sources, str):
        sources = [sources]
    buckets = {}
    for src in sources:
        for k, v in load(src).items():
            buckets.setdefault(k, []).extend(v)
    everywhere = [v for vs in buckets.values() for v in vs]

    body = re.sub(INCLUDE, lambda m: f"\x00{os.path.splitext(os.path.basename(m.group(1)))[0]}\x00", tex)
    blocks = [(0, body)] if len(buckets) == 1 and "" in buckets else None
    if blocks is None:
        cuts = [m.start() for m in SECTION.finditer(body)] or [0]
        if cuts[0] != 0:
            cuts.insert(0, 0)
        blocks = [(a, body[a:b]) for a, b in zip(cuts, cuts[1:] + [len(body)])]

    ok = wrong_section = 0
    misses, strays = [], []
    for _, block in blocks:
        local = [n for n in re.findall(r"\x00([^\x00]*)\x00", block) if n in buckets]
        if not local and list(buckets) == [""]:
            local, pool = ["(whole source)"], buckets[""]
        else:
            pool = [v for n in local for v in buckets[n]]
        clean = block.replace("\x00", " ")
        for m in PROSE_NUM.finditer(clean):
            digits = m.group(1)
            if len(digits.split(".")[1]) < min_decimals:
                continue
            value = signed(clean, m.start(1), digits)
            shown = ("-" if value < 0 else "") + digits
            tol = 0.5 * 10 ** (-len(digits.split(".")[1]))
            if any(abs(x - value) <= tol for x in pool):
                ok += 1
            elif any(abs(x - value) <= tol for x in everywhere):
                wrong_section += 1
                where = [n for n, vs in buckets.items() if any(abs(x - value) <= tol for x in vs)]
                strays.append((shown, local or ["(none)"], where))
            else:
                misses.append(shown)

    print(f"checked: {ok + wrong_section + len(misses)} prose numbers with >={min_decimals} decimals")
    print(f"matched in their own section: {ok}")
    if strays:
        print(f"MATCHED ONLY ELSEWHERE: {len(strays)} -- confirm each by hand")
        for shown, local, where in strays:
            print(f"  {shown}: section includes {local}, value printed in {where}")
    if misses:
        print(f"NOT FOUND: {sorted(set(misses))}")
        print("  Each must be a constant you typed, a value derived by hand in the document,")
        print("  or a value from a source not passed on the command line. Anything else is a defect.")
    else:
        print("NOT FOUND: none")
    return 1 if misses else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "solutions.tex",
                  sys.argv[2:] if len(sys.argv) > 2 else ["chunk"]))
