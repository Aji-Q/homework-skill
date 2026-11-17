# Verification

Two passes, both mandatory for graded work.

## Thresholds

| Check | Threshold |
|---|---|
| Prose numbers with ≥3 decimals traced to printed output of their own sub-part | 100%, minus cross-references confirmed by hand |
| Overfull boxes reported by the compiler (prose, displays, tables) | 0 distinct |
| Transcript lines over the column budget (`scripts/check_width.py`) | 0 |
| Sub-questions from the enumeration with an explicit answer | 100% |
| Figures produced by the script vs. figures included in the document | equal |
| Headline results reproduced by an independent implementation | agree, or the difference is explained by a known method choice and reported to the user |
| Compile in the delivery folder after copying | succeeds |
| A formula the assignment attributes to a course source matches that source's form, notation and parameter values | yes |
| Every constant not given by the question traced to the source that fixes it | yes |
| Attachments reopened after delivery, no `#NAME?` / `#REF!` / `#VALUE!` in the saved file | yes |
| Attachment file formats unchanged from what the assignment supplied | yes |
| Any error that remains is student-shaped, not model-shaped | yes |
| Values quoted from a volatile source read from the file as delivered, and declared as one run | yes |
| Deduction ledger present and summing to the budget, at `score` < 100 | yes |
| Document written in one language, and that language is the assignment's | yes |
| Sub-part headings matching the assignment's own numbering | all |
| Displayed calculations that reproduce their stated result at the digits shown | all |
| Literal banned strings from `references/voice.md` | 0 |
| Supporting facts per verdict sentence | ≤ 1 independent support, at `voice` student |
| Booster-to-hedge ratio | about 2:1 at `voice` student, neither term zero |
| Rulings on a method, and alternatives dismissed | ≥ 1 of each per four sub-parts at `voice` student |
| Discrepancies closed by naming a category | ≤ 2 per submission |
| Register drift toward the assignment's own style | none |
| Unclosed gap flagged in future-work form, conclusion unmoved | ≤ 1 per submission at `voice` student |
| Statements about the author's state ("I am not sure", "I did not have time") | 0 at `voice` student |
| First person about method | 0 at `narration` 0–1 |
| Parallel clauses in one sentence | ≤ 2 |
| "That is the trap"-shaped remarks | ≤ 1 per four sub-parts at `voice` student |
| Comparison tables weighing alternatives | 0 at `voice` student |
| Arrogance aimed at the reader or the assignment | 0 |
| Second-language markers | about 1 per 300 words at `nativeness` near-native, 0 at native |
| Lexis column mixed between native and near-native | never |
| Boosters suppressed inside a formal derivation | never — they are technical there |
| Prose sentences narrating what code mechanically does | 0 |
| Maths set at the tier its `fluency` calls for | per `references/notation.md` |
| Printed output formatted no further than that tier allows | per `references/notation.md` |
| Code comments other than section markers | 0 at `narration` 0–1 |

The voice rows are the mechanical half only. Four judgement rules in `references/voice.md` carry
no check and are reviewed by reading; a passing table is not a passing document. Same for the two
`notation.md` rows: the greppable half lives in that file's own table, and the notation drift it
exists to preserve has to be seen.

The two width rows are separate because the compiler is silent about over-wide verbatim lines:
a document whose code listings run off the page still reports zero overfull boxes. Looking at the
rendered pages is what catches the rest.

The language and numbering rows are checkable by eye in one pass over the rendered PDF, and
they are the rows a grader notices first.

## Pass 1 — numbers

`scripts/verify_numbers.py solutions.tex chunk` extracts every number with three or more decimals
from the prose (the verbatim includes *are* the output, so they are stripped) and looks for it in
the printed output at the displayed precision. Two refinements matter:

- **Echoed source does not count as output.** With echo on, the transcript contains the code too,
  so a literal sitting in an unused assignment or a tolerance would otherwise satisfy a claim
  about a result. Prompt-carrying lines are excluded.
- **Numbers are scoped to their sub-part.** Given the chunk directory, each number is checked
  against the chunks its own section includes. A value found only in another section is reported
  separately — prose does legitimately quote an earlier result, and that is for you to confirm,
  one by one. Passing a flat transcript instead disables this and checks globally.

Account for every entry in both lists individually. Legitimate causes for a miss:

- a constant that was typed rather than computed (1.96, 2.576)
- a value derived from two printed numbers — check that derivation by hand
- a value typeset with the exponent as markup (`1.2345\times10^{-7}`), which the checker
  compares as `1.2345`; verify those by hand

Anything else is a defect. Scientific notation on the *transcript* side is handled and is not a
legitimate excuse for a miss.

## Pass 2 — independent re-derivation and audit

Re-derive the results from the raw data with code written independently of the submitted script
— a different language, or at minimum a hand-written formula instead of the library call — and
diff. Then audit along separate lenses, because one reader misses different things than another:

- **numbers** — recompute everything, including quantities quoted only in prose
- **references** — every formula, path, and cross-reference quoted in the text holds in the file
  it names
- **math** — every step, sign, and constant in the hand derivations, verified numerically
  wherever a numeric check exists
- **coverage** — walk the enumeration sub-question by sub-question against the document
- **conventions** — language, numbering, precision and attribution, against the Conventions
  section of SKILL.md
- **voice** — reasoning depth and register against `references/voice.md`: does any paragraph
  stack evidence, reach the structural reason, close on a generalisation, or point at its own
  gap; does any sentence explain behaviour rather than state a finding
- **notation** — the maths and the printed output against `references/notation.md`: is the
  setting at the tier `fluency` calls for, and is the transcript formatted past it

Try to refute each finding before acting on it. Lens sweeps produce false positives, and a
confident argument about mathematics can still be wrong. Re-run the check yourself; a
subagent's narrative is not evidence.

## When the two implementations disagree

A difference is not automatically a defect. A deliberately simpler method — the textbook call
rather than a tuned one, chosen at low `fluency` — produces a different number by construction.
What matters is that the document reports what the submitted code printed, that the size of the
gap is known, and that the user is told which numbers it affects. An unexplained difference is a
defect.

## What this reliably catches

Claims contradicted by a table printed a few lines above them; optimizers reporting success
while short of the optimum; sentences describing a setting the submitted code no longer uses;
scaling factors that are right in one special case and wrong in general. All of these survive
several readings of the source, which is why the checks are mechanical.
