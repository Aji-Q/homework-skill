# The three dials

## `score` — target mark

The target mark out of 100. At 100 nothing below applies: answer everything as fully as it can
be answered.

Below 100, budget the loss. Read the per-part marks off the assignment and total them; if the
assignment prints no marks, weight the sub-parts equally and let `total` be their count. Then

    budget = total x (100 - score) / 100

expressed in the same units as `total` — marks, or sub-parts.

Constraints on spending it:

- at least three separate sub-parts contribute; expect three to six
- no single deduction exceeds half the budget
- every deduction comes from the safe list below
- nothing comes from the forbidden list, at any `score`

If the safe list cannot absorb the budget — a short assignment at `score` 70, say — stop and
tell the user. Do not make up the difference from the forbidden list.

**The ledger.** Each concession is recorded as it is made:

| Sub-part | Given up | Marks |
|---|---|---|
| 2(c) | the second mechanism behind the discrepancy, only the consequence stated | 3 |
| 4 | the zero-inventory-ordering property asserted, not shown | 4 |

The ledger goes to the user, not into the document, and its total is the budget. Without it the
setting has no effect that can be pointed at afterwards, which has been its failure mode twice.

**Safe, ranked by how natural the loss looks.** Costs are given relative to the marks `p` of the
part they are taken from, so a 12-mark part giving up "0.2–0.3 p" contributes 2.4 to 3.6 marks.

| Loss | Cost |
|---|---|
| Answer the obvious half of a two-part "why", omit the subtle half | 0.2–0.3 p |
| Derive a stationary point where a uniqueness or global-maximum proof was asked for | 0.25 p |
| Diagnose a real discrepancy weakly (the statistic is unstable) rather than structurally (the statistic does not exist) | 0.3 p |
| Give one clean statement for an open "discuss the relationship" part instead of several framings | 0.2 p |
| Drop a caveat: the comparison that is not apples-to-apples, the assumption the result rests on | 0.1–0.15 p |

A skipped step is simply not on the page. Do not flag it, do not apologise for it, do not write
a sentence about what a fuller treatment would do — that is metacognition, and it reads as an
expert deliberately withholding rather than as someone who did not go there. The exception is a
subtlety the text actually touches: dispose of it in one confident clause and move on. See
`references/voice.md`.

**Forbidden at every `score`**

- any number that differs from what the submitted code printed
- a sub-question with no explicit answer
- an artefact the problem named: the reference line, the plot, "intervals for all four
  parameters", the direct answer to "which is shortest"

**Flourish test, independent of `score`.** Work that earns no marks still costs reading time and
sets an expectation the rest of the paper has to meet: an audit of the optimizer's convergence,
an appendix verifying a library's parameterisation, standard errors cross-checked by a second
method, an observation about where a surface stops being concave. Do that work — it is how the
answers get verified — and then keep it out of the submitted document unless the assignment
asked for it. Report it to the user instead.

## `fluency` — how experienced the code looks

Not syntax level. A learner and an expert write the same language differently.

| Category | `fluency` 3, practised | `fluency` 1, still learning |
|---|---|---|
| Iteration | vectorized map/apply/comprehension | explicit indexed loop over `1..n` |
| Reuse | one parameterised function | near-duplicate copies, one per dataset |
| Constants | quantile/CDF calls | hardcoded `1.96`, `2.576` |
| Naming | one convention throughout | conventions drift between sections |
| Intermediate output | final results only | shape/type/head calls left in |
| Self-checks | none, or a formal assertion | a value recomputed by hand and printed beside it |
| Plot styling | tuned marker sizes, typeset math titles, computed label positions | library defaults, plain string titles |
| Axis labels | custom | whatever the plotting function writes |
| Numerical tuning | step sizes, scaling, restarts | the textbook call, as printed in the notes |
| Result formatting | labelled values at fixed precision | bare values at whatever precision the library prints |
| Output furniture | separators, headers, a sign-off line | none |

`fluency` 2 is the middle: vectorized where it is natural, loops where it is not; consistent naming;
default plots with a custom title.

The last two rows are the ones generated code violates without being asked. Formatting the
printed output is an experienced habit and a generator's reflex, and in a transcript — which is
set verbatim, with nothing between the reader and the console — it is the most visible tell
there is. A script at `fluency` 2 that prints a labelled, four-decimal, column-aligned block has
jumped a tier.

Hold one tier throughout. Mixed tiers are more conspicuous than either tier alone.

See also `references/voice.md`, which governs how far the reasoning runs and what gets deleted,
and `references/notation.md`, which carries the same tiering for the maths and the printed output.

## `narration` — how much of the working is said out loud

How much first-person process appears in the prose and the code.

| `narration` | First person | Code comments | Check |
|---|---|---|---|
| 0 | none | section markers only | `grep -cE '\b(I|my|we|our)\b'` on the source, excluding verbatim includes, returns 0 |
| 1 | ≤1 hedge per section | what a line does, never why you tried it | — |
| 2 | unrestricted | unrestricted | — |

At 0, delete: restatements of the question ("the question asks whether…"), process reports
("I tried", "I had to look up", "I only caught it by"), reaction ("which I did not expect"),
and unearned hedges ("I think" in front of a fact). Keep judgments — "the second
estimator is the better number", "one significant figure is as much as this method supports" —
those are findings.

Texture at 0 comes from what the script *does*: an exploratory call that was never removed,
a loop's indexing checked by hand, a redundant convergence print. Actions, not commentary.
