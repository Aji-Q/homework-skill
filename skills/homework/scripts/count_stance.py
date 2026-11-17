r"""Count boosters, hedges and second-language markers in the document prose.

The booster-to-hedge ratio is a stated threshold in references/voice.md and should not be
eyeballed. Verbatim includes are stripped, since they are console output, not prose.

    python3 count_stance.py solutions.tex
"""
import re
import sys

BOOSTER = r"\b(clearly|of course|obviously|certainly|evidently|undoubtedly|plainly|trivially|by inspection|it is easy to see)\b"
HEDGE = r"\b(I think|probably|it seems|arguably|perhaps|possibly|presumably|somewhat|mostly|fairly|apparently|likely|to some extent)\b"
L2 = (r"\b(carry out|carried out|according to the above|make a conclusion|is obtained|are obtained"
      r"|utilis[ez]|respectively|namely|as follows)\b"
      r"|(?<![\w])(Besides|Moreover|In addition|Furthermore),")
PRECISION = r"(~|\babout\b|\broughly\b|\bof order\b|\balmost\b)"


def main(path):
    text = open(path, encoding="utf-8").read()
    prose = re.sub(r"\\(?:Rin|VerbatimInput|lstinputlisting)\s*(?:\[[^\]]*\])?\{[^}]*\}", " ", text)
    prose = re.sub(r"\\begin\{(verbatim|lstlisting)\}.*?\\end\{\1\}", " ", prose, flags=re.S)
    # line wrapping must not hide a two-word marker: "of\ncourse" is still "of course"
    prose = re.sub(r"\s+", " ", prose)
    words = len(re.findall(r"\b\w+\b", prose))

    b = re.findall(BOOSTER, prose, re.I)
    h = re.findall(HEDGE, prose, re.I)
    l2 = [m.group(0) for m in re.finditer(L2, prose)]
    print(f"words of prose: {words}")
    print(f"boosters: {len(b)}  {sorted(set(x.lower() for x in b))}")
    print(f"hedges:   {len(h)}  {sorted(set(x.lower() for x in h))}")
    ratio = (len(b) / len(h)) if h else float("inf")
    print(f"booster:hedge = {ratio:.2f} : 1   (target about 2, neither term zero)")
    if not h:
        print("  FAIL zero hedges — voice.md calls a document with no qualification a caricature")
    elif not b:
        print("  FAIL zero boosters — the placement rule is the signature and it is absent")
    elif not 1.2 <= ratio <= 3.5:
        print("  off target")
    per300 = len(l2) / (words / 300) if words else 0
    print(f"second-language markers: {len(l2)}  = {per300:.2f} per 300 words (near-native target ~1)")
    print(f"precision markers, not budgeted: {len(re.findall(PRECISION, prose, re.I))}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "solutions.tex"))
