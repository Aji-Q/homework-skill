# Notation and printed output

Two surfaces carry the author's hand once a document is mostly formulas and console output:
how the maths is *set*, and how the script *prints*. `references/voice.md` governs the prose
that sits between them. In a problem set that is mostly algebra, this file matters more than
that one.

Both surfaces are the same idea as `fluency`. A document produced in one pass comes out
globally consistent, and consistency is the tell. A derivation written over an evening in
several sittings drifts: `\epsilon` in part (a), `\varepsilon` in part (c); the transpose as
`^T` here, `\top` there. That drift is the handwriting. It is not cleaned up afterwards.

**Drift is permitted only where meaning is not.** Two spellings of one symbol is drift. A
symbol that means one thing in (a) and another in (c) is an error, and no tier licenses it.
Same rule as `references/voice.md`: firmness may run ahead of the evidence, it may never run
ahead of the numbers.

## When this applies

These rules follow `fluency`, not `voice` — the same axis that decides how experienced the
code looks, because it is the same person writing both.

| `fluency` | The maths reads as |
|---|---|
| 3 | set by someone who has written a great deal of it: `\left(` `\right)`, `\text{}` subscripts, `align`, `\implies`, spacing macros where they earn their place |
| 2 | half of it: plain brackets, inline in preference to display, italic subscripts and units, no spacing macros; the connectives and the alignment stay tidy |
| 1 | all of it, plus the drift: the same quantity set two ways in two sections |

At `voice: neutral` none of this applies. A reference answer has no author in it, and a
nameless answer is set cleanly and consistently — that is what "no author" means. The default `voice` is `neutral`, so the tiering below reaches only a document that has been
asked to carry a hand: see *Choosing the settings* in `SKILL.md`.

## The maths

| | Set cleanly (3) | Written by hand (1–2) |
|---|---|---|
| Parentheses | `\left( \frac{a}{b} \right)` | `(\frac{a}{b})` — bracket smaller than its contents |
| Inline fractions | promoted to a display | `\displaystyle` pushed inside `$...$` |
| Subscript words | `x_{\text{obs}}` | `x_{obs}` |
| Units | `\text{m\,s}^{-1}` | `m/s`, `ms^{-1}` |
| Connectives | `\implies`, `\iff`, `\therefore` | `\Rightarrow`, `\leftrightarrow`, `\to` |
| Spacing | `\,` `\;` `\quad` `\!` | none |
| Alignment | every `=` lined up in `align*` | newline and go; `=` positions ragged |
| Fractions | `\frac` everywhere | `/` inline, `\frac` displayed, not unified |
| Display vs inline | a fresh `equation` for anything substantial | inline until it will not fit |
| Numbering | a tag or number per step | untagged; occasionally a hand-written `(*)` |
| Multiplication | `\cdot` for scalar, `\times` for cross, chosen per case | `\cdot` throughout, or omitted |
| Matrix brackets | one environment, chosen once | `bmatrix` in one part, `array` in another |

Every row is correct LaTeX in both columns. Nothing in the right column is an error; the
difference is entirely in how it is set.

**Effort runs opposite to the prose.** The steps of a hard derivation get written out; the
easy ones get skipped. This is the mirror of `references/voice.md`'s *Effort lands where the
work was easy*, and the two together are what a real submission looks like: the hard part is a
wall of algebra with one sentence in front of it, the easy part is a single line followed by
three sentences of prose. The prose is long where the author is comfortable. The algebra is
long where the author is not.

**Do not define a notation macro to hold the document together.** A `\newcommand` for the
transpose, or for a likelihood, forces one spelling on every occurrence — which is exactly
the global consistency being avoided. Take the notation from the assignment (see *Language*
in `SKILL.md`) and type it, even when the typing is not identical twice.

## Printed output

`\VerbatimInput` sets the console verbatim, so the formatting *of the output* is as visible
as the code that produced it. `references/calibration.md` covers what the code looks like;
this is the other half.

| | Practised (3) | Learner (1) |
|---|---|---|
| Result lines | `print(f"mean = {m:.4f}")` | `print(m)` at full precision |
| Labels | every printed number labelled | bare values, at most a short name beside |
| Furniture | `print("=" * 40)`, section banners | none |
| Tabulation | `to_string()`, aligned columns | library default, index prefix, truncated with `...` |
| Sign-off | `print("Done.")` | none |
| Intermediates | cleared out | `dim()`, `head()`, `str()` left where they were called |

**The right-hand column of this table is where an assistant lands by default, and it is the
wrong one whenever `fluency` is below 3.** Formatting the output is a habit of experienced
code and a reflex of generated code, and it is the single most visible generated-code tell in
a transcript, because nothing on the page sits between the reader and the console. A script at
`fluency` 2 that prints a labelled, four-decimal, column-aligned block has jumped a tier.

What changes here is only how the script prints. Precision quoted in the *prose* is still
governed by *Numbers* in `SKILL.md`, unchanged.

## Checks

| Check | Threshold |
|---|---|
| `\left` and `\right` | 0 at `fluency` 1, a few at 2 |
| Spacing macros (`\,` `\;` `\quad` `\!`) outside tables | 0 at `fluency` 1 |
| `\implies`, `\iff`, `\therefore` | 0 at `fluency` 1 |
| `\text{` in subscripts and units | rare at `fluency` 1–2 |
| Result lines at fixed precision | 0 at `fluency` 1–2 |
| Banner and sign-off prints | 0 at `fluency` 1–2 |

```bash
grep -c '\\left' solutions.tex                          # lines with scaled brackets
grep -oE '\\[;,!]|\\quad' solutions.tex | wc -l         # spacing macros, by occurrence
grep -oE '\\(implies|iff|therefore)' solutions.tex | wc -l
grep -n '\\text{' solutions.tex                         # read the hits
grep -cE ':\.[0-9]+f\}' analysis.py                     # result formatting
grep -cE '"=" ?\*|Done\.|Finished\.' analysis.py        # output furniture
```

Read the hits rather than the counts: `\left` also opens a matrix, and `\text` has legitimate
uses outside a subscript. An assignment with two displayed formulas is not tested on alignment,
and the drift — the same quantity set two ways in two sections — is not greppable at all.
