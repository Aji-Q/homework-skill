r"""Measure the shape of the prose: how much the sentences and paragraphs vary, and how
often the balanced-construction moves appear.

The stance and banned-string checks are per-sentence. A document can pass every one of them
and still read as generated, because the tell is a whole-document frequency: every third
sentence a balanced pair, every paragraph the same weight, no sentence that goes nowhere.
This script measures that layer. references/voice.md carries the thresholds and where they
came from.

    python3 count_shape.py solutions.tex
    python3 count_shape.py --plain some_prose.txt     # already-plain text, skip the LaTeX strip
"""
import re
import statistics
import sys

# the "short sentence that negates, then expand" move: a pivot sentence short enough to land
# as a beat. Length cap is what separates it from an ordinary negative statement.
PIVOT_MAX_WORDS = 12
NEGATION = r"\b(not|no|never|nor|cannot|isn't|does not|did not|is not|are not|was not)\b"
# two-part antithesis, the "X rather than Y" family
ANTITHESIS = r"\b(rather than|instead of|as opposed to|not .{1,40} but|less .{1,30} than it is)\b"
# only the rhetorical colon counts. A colon that introduces a display, and the one inside a
# spreadsheet range, are punctuation this genre needs; counting them measured 35 per 100 on a
# document whose prose carries none of the move at all.
CELL_RANGE = r"\b[A-Z]{1,2}\$?\d+:\$?[A-Z]{1,2}\$?\d+\b"
COLON_LEAD_MAX_WORDS = 12

# Thresholds measured, not guessed. Baseline: two Journal of Financial Economics papers
# (S0304405X19301655; Moskowitz-Ooi-Pedersen 2012), body prose only, 1208 sentences in all.
# They gave sentence CV 0.62/0.57, paragraph CV 1.04/0.90, pivots 0.8/1.1, antithesis 1.6/1.9
# per 100 sentences. The floors sit below the lower human value and the caps above the higher
# one, so a real document passes and uniform prose does not. subtle: this baseline is academic
# finance, the longest-paragraph register there is; a short-form essay will run a lower
# paragraph CV honestly, so treat that row as the weakest of the five.
SENT_CV_MIN = 0.50
PARA_CV_MIN = 0.55
PIVOT_MAX = 3.0
ANTI_MAX = 4.0
COLON_MAX = 4.0


def strip_latex(text):
    """LaTeX source -> the prose a reader actually reads, paragraphs kept as blank-line splits."""
    text = text.split(r"\begin{document}", 1)[-1]
    text = re.sub(r"\\end\{document\}.*", "", text, flags=re.S)
    text = re.sub(r"(?<!\\)%.*", "", text)                              # comments
    text = re.sub(r"\\begin\{(verbatim|lstlisting|tabular|array)\}.*?\\end\{\1\}", " ",
                  text, flags=re.S)
    text = re.sub(r"\\(?:Rin|VerbatimInput|lstinputlisting|includegraphics)\s*"
                  r"(?:\[[^\]]*\])?\{[^}]*\}", " ", text)
    text = re.sub(r"\\\[.*?\\\]", " MATH ", text, flags=re.S)           # display math
    text = re.sub(r"\$\$.*?\$\$", " MATH ", text, flags=re.S)
    text = re.sub(r"\$[^$]*\$", " MATH ", text)                         # inline math
    text = re.sub(r"\\(?:section|subsection|subsubsection)\*?\{[^}]*\}", "\n\n", text)
    text = re.sub(r"\\(?:texttt|textbf|emph|textit|boxed)\{([^{}]*)\}", r"\1", text)
    text = re.sub(r"\\begin\{[^}]*\}|\\end\{[^}]*\}", " ", text)
    text = re.sub(r"\\[a-zA-Z@]+\s*(?:\[[^\]]*\])?", " ", text)         # remaining commands
    text = re.sub(r"[{}]", " ", text)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n\s*\n\s*\n+", "\n\n", text)
    return text


def paragraphs(text):
    out = []
    for block in re.split(r"\n\s*\n", text):
        block = re.sub(r"\s+", " ", block).strip()
        if len(re.findall(r"\b[a-zA-Z]{2,}\b", block)) >= 12:           # drop captions and stubs
            out.append(block)
    return out


def sentences(para):
    # never split inside a decimal; MATH placeholders already removed the worst of it
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z(])", para)
    return [p.strip() for p in parts if len(re.findall(r"\b\w+\b", p)) >= 3]


def rhetorical_colons(sent):
    """(str) -> int   colons used as a pivot, not to introduce a display or split a cell range.

    "Timing is: the window closes in March"        -> 1
    "From I29, J29, K29: MATH"                     -> 0   (introduces a display)
    "the demand forecast in B7:K7"                 -> 0   (cell range)
    """
    s = re.sub(CELL_RANGE, " ", sent)
    n = 0
    for m in re.finditer(r":", s):
        after = s[m.end():].strip()
        if after.startswith("MATH") or not after:
            continue
        lead = re.findall(r"\b\w+\b", s[:m.start()])
        if len(lead) <= COLON_LEAD_MAX_WORDS:
            n += 1
    return n


def cv(xs):
    """(list[float]) -> float   coefficient of variation; [10,10,10] -> 0.0, [2,20] -> 0.82"""
    if len(xs) < 2:
        return 0.0
    m = statistics.mean(xs)
    return statistics.pstdev(xs) / m if m else 0.0


def main(path, plain=False):
    text = open(path, encoding="utf-8").read()
    if not plain:
        text = strip_latex(text)
    paras = paragraphs(text)
    sents = [s for p in paras for s in sentences(p)]
    if not sents:
        print("no prose found — wrong file, or everything is inside math and verbatim")
        return 1

    wordcount = lambda s: len(re.findall(r"\b\w+\b", s))
    slen = [wordcount(s) for s in sents]
    plen = [wordcount(p) for p in paras]

    pivots = [s for s in sents
              if wordcount(s) <= PIVOT_MAX_WORDS and re.search(NEGATION, s, re.I)]
    anti = [s for s in sents if re.search(ANTITHESIS, s, re.I)]
    colons = sum(rhetorical_colons(s) for s in sents)

    per100 = lambda n: 100.0 * n / len(sents)
    s_cv, p_cv = cv(slen), cv(plen)

    print(f"paragraphs: {len(paras)}   sentences: {len(sents)}   words: {sum(slen)}")
    print(f"sentence length: mean {statistics.mean(slen):.1f}  CV {s_cv:.2f}"
          f"   (floor {SENT_CV_MIN} — below it the sentences are all the same size)")
    print(f"paragraph length: mean {statistics.mean(plen):.1f}  CV {p_cv:.2f}"
          f"   (floor {PARA_CV_MIN} — below it every paragraph carries the same load)")
    print(f"short negating pivots (<={PIVOT_MAX_WORDS} words): {len(pivots)}"
          f"  = {per100(len(pivots)):.1f} per 100 sentences   (cap {PIVOT_MAX})")
    print(f"antithesis markers: {len(anti)}  = {per100(len(anti)):.1f} per 100 sentences"
          f"   (cap {ANTI_MAX})")
    print(f"rhetorical colons: {colons}  = {per100(colons):.1f} per 100 sentences"
          f"   (cap {COLON_MAX})")

    fails = []
    if s_cv < SENT_CV_MIN:
        fails.append(f"sentence-length CV {s_cv:.2f} < {SENT_CV_MIN}")
    if p_cv < PARA_CV_MIN:
        fails.append(f"paragraph-length CV {p_cv:.2f} < {PARA_CV_MIN}")
    if per100(len(pivots)) > PIVOT_MAX:
        fails.append(f"pivot rate {per100(len(pivots)):.1f} > {PIVOT_MAX} per 100")
    if per100(len(anti)) > ANTI_MAX:
        fails.append(f"antithesis rate {per100(len(anti)):.1f} > {ANTI_MAX} per 100")
    if per100(colons) > COLON_MAX:
        fails.append(f"rhetorical-colon rate {per100(colons):.1f} > {COLON_MAX} per 100")
    for f in fails:
        print(f"  FAIL {f}")
    if not fails:
        print("  shape ok")

    if len(pivots) > 3:
        print("\nlongest-running pivots, for the eye:")
        for s in pivots[:6]:
            print(f"    {s}")
    return 0


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a != "--plain"]
    if len(args) != 1:
        sys.exit(__doc__)
    sys.exit(main(args[0], plain="--plain" in sys.argv[1:]))
