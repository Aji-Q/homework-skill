---
name: homework
description: Produce a submittable homework solution set from an assignment (images, PDF, or pasted text) plus its data files. Use when the user hands over a problem set and wants the answers worked out and written up as a document. Covers the whole path - enumerate sub-questions, compute reference answers, run the analysis so code and console output can be included verbatim, typeset in LaTeX, compile to PDF, verify every printed number against the output of its own sub-part, and deliver. Five settings tune the result - score (target mark), fluency (how experienced the code looks), narration (how much process is spoken), voice (how far the prose reasons and how firmly it lands), and nativeness (whether the English reads as a first or second language, so the write-up reads as the author it is meant to read as). Do NOT trigger for research papers, reports, or data analysis with no assignment behind it.
---

# Homework solution sets

The deliverable is a document a grader reads: formulas, computations, answers, and — whenever
the assignment asks for them — code, console output, and figures. Source, script and transcript
ship alongside the PDF.

The document is the user's own submission or study material, and the target is that it be
indistinguishable from what that person would hand in: the right grain of working, the right
depth of reasoning, their voice. The settings below are the dials for that.

Correctness is not the goal; it is a constraint, and it earns its place for two reasons only. A
paper that contradicts its own attachment is the most visible defect there is — a grader sees it
before reading a word. And an answer that is wrong for a *model's* reason gives the whole thing
away. None of the settings is a licence to invent results: at every setting, the numbers in the
prose are the numbers the source printed.

## Workflow

1. **Enumerate the sub-questions.** Write the list down before starting. Sub-parts hide inside
   prose ("also compare the volatilities", "print intervals for all four parameters"). Every one
   needs an explicit answer sentence in the document. A missed sub-part costs more than any
   stylistic choice.
2. **Locate and inspect the data, and whatever else the assignment points at.** Search the
   filesystem by the name the assignment uses. Print shape, type, column names and range before
   using it; those settle which variables the problems mean. A phrase like "the formula
   developed in class", "as we did in lecture", "the method from Chapter 7" or "this is the
   class example with X changed" names a *source*, not a hint: find the lecture notes or the
   chapter and use the form they give, including their notation **and their parameter values**.
   Slides often carry the call as a screenshot, so read the rendered page, not the text layer. If it cannot be found, ask for it before writing — a correct answer in the wrong
   formulation loses marks that no amount of care elsewhere recovers.
3. **Compute reference answers first**, in whatever is fastest, independently of the script you
   will submit. This is the ground truth the deliverable gets checked against.
4. **Fix the conventions and the five settings** — both below — before writing the submitted
   script, not after.
5. **Write one analysis script** with section markers, `mkdir -p chunk fig`, run it with echo on
   so code and output interleave, then split the transcript per sub-part. Put a marker above the
   imports too: content before the first marker is discarded.
   `assets/README.md`, `scripts/split_transcript.py`.
6. **Typeset.** `assets/template.tex` is the skeleton.
7. **Verify** against the thresholds in `references/verification.md`.
8. **Deliver** the whole tree into the user's coursework folder, recompile there to prove the
   relative paths hold, and report back in the shape given under *Reporting back*.

## Conventions

These are not preferences. Decide each one before writing, and hold it across the document.

### Language

- The document is written in **the language of the assignment**, whatever language the
  conversation is in; an explicit instruction from the user overrides this, nothing else does.
  The chat reply is always in the user's language.
- **One language inside the document** — prose, figure titles, axis labels, table headers, code
  identifiers, comments.
- Use the notation and terms the assignment and its textbook use, not a synonym or a
  back-translation.

### Document shape

- **Start at the first problem.** No title page, no abstract, no environment-and-versions
  preamble, no restatement of the question. The first line on page 1 is the first problem
  heading.
- **Mirror the assignment's numbering exactly** — `Problem 3`, `(b)` — so the grader can read
  the two side by side. Never renumber or merge parts.
- **Each sub-part in one place**: the formula, the computation, an explicit answer sentence, and
  the code block and figure that produced it. Hand derivations sit with the sub-part they
  answer, never in an appendix.
- **Figures inline, not floated**, so they stay with their discussion. Every figure the script
  produces is included; every figure referenced exists.
- A closing summary table is optional — worth it when the assignment has many numeric answers,
  noise when it has few.

### Numbers

- **Quote a value at the precision the output shows, or less. Never more.**
- **A displayed calculation must reproduce its own result.** If you write out the operands, print
  enough digits that the arithmetic as shown gives the stated answer. Four-decimal operands
  feeding a full-precision result is a defect a grader can catch with a calculator.
- **Convert to the units the question asks for** and show the conversion — a time in years into
  a date, a log return into a percentage — rather than leaving the reader to do it.
- **One rounding convention per quantity** across the whole document.
- **Every quoted value is attributable**: it comes from this sub-part's output, or the prose says
  which sub-part it came from.

### Reporting back

In the chat reply, in the user's language:

1. A results table, one row per sub-part: the answer, and where it lives (cell, chunk, or page).
   Name the document's arc in one phrase, so the next one can take a different shape.
2. Only what the user must know to defend the work: assumptions taken, boundary optima, a method
   choice that moved a number, anything deliberately left out.
3. The settings used, so they can be moved.

Nothing else. Do not narrate the process.

## The five settings

Set all five before writing the submitted script, and state them back to the user.

| Setting | Controls | Range | Default |
|---|---|---|---|
| `score` | how many marks to aim for | 70–100 | 90 |
| `fluency` | how experienced the **code and the maths** look | 1 (learner) – 3 (expert) | 2 |
| `narration` | how much of the working is said out loud | 0 (none) – 2 (full) | 1 |
| `voice` | how far the **prose** reasons and how firmly it lands | student / neutral / explanatory | neutral |
| `nativeness` | whether the English reads as a first or second language | native / near-native / non-native | near-native |

**`score`** — the target mark out of 100. At 100, answer every part as completely as it can be
answered. Below 100 the paper deliberately gives up explanation depth: deduction budget
`budget = total_points × (100 − score)/100`, spent only on the shorter half of a two-part
answer, a stationary point where a uniqueness proof was asked for, a weaker diagnosis of a real
discrepancy, dropped caveats. Spread over at least three sub-parts, none taking more than half
the budget. **Never** spend it on a number, a missing sub-part, or an artefact the
problem explicitly demanded. The default of 90 is a standing instruction, not an inference; set
it to 100 when the user asks for full marks, and never take it lower than they asked.

Write the spending down. A **deduction ledger** — one line per concession: the sub-part, what
was given up, the marks — goes in the reply to the user, and its entries sum to the budget. A
paper of ordinary depth with no ledger is not a `score` 90 paper; it is a `score` 100 paper with
the dial written on it, which is the failure this setting keeps having.

**`fluency`** — not syntax level, *fluency*. At 1 the code reads as someone still learning:
explicit loops, near-duplicate functions instead of one parameterised one, hardcoded constants,
naming that drifts between sections, exploratory calls left in, library-default plots. At 3 it
reads as a practised analyst. Hold one level across the whole script; a single expert construct
inside otherwise non-fluent code is the strongest tell there is. The same tier governs how the
maths is set and how the script prints its results: `references/notation.md`.

**`narration`** — how much first-person process appears. At 0: no "I tried", "the question
asks", "which I did not expect" anywhere outside the verbatim blocks, and no code comments
except section markers; texture then comes from what the script *does* — a leftover exploratory
call, a loop index checked by hand. At 1: brief hedges where genuinely warranted. At 2:
unrestricted, useful when the user wants to learn the material rather than submit it.

**`voice`** — the shape of the reasoning and the firmness of the verdicts, a different axis from
how much process is spoken. `student` is opt-in: the persona machinery does not switch itself on because the score is below
100. At `student` the persona is green, confident and faintly arrogant, in that order of
importance:
one verdict backed by at most one fact; the chain
stops one step past what the question asked **and says nothing about stopping**, because the
greenness is the blank itself, not an acknowledgement of it; judgments stated flatly, with boosters running about twice the hedges rather than the hedges
going to zero; rulings passed on the methods rather than neutral reports of them; a subtlety the
text does raise gets settled in the same clause rather than left open. At `neutral`: a
reference answer with no author, reasoning to the bottom. At `explanatory`: a teacher walking
the reader through.

The persona does not drift toward the assignment's register: vocabulary and notation cross over
from the source material, nothing else. Uneven effort across sub-parts is authentic; uneven
register is drift.

Four failure modes. `narration` 0 with an expert's `voice` gives the work away — the process is
silent but the reasoning runs two steps further than its author would take it. A document that
keeps flagging its own limits is not green; self-assessment is an expert's move. Trimming the reasoning below what the sub-part actually asked answers the wrong question:
*answer the question in full* overrides every rule in that file. And the quiet failure is the
likeliest: the deletion rules carry hard thresholds and greppable commands while the personality
rules are read by eye, so an executor under pressure runs the greps and produces something
diligent and characterless. The floors in `references/voice.md` exist against exactly that.

**`nativeness`** — whether the English reads as a first or second language. Idiomatic native
prose is a signature of its own, so a paper that reads neither as generated nor as its author is
the failure this prevents. At `near-native`, second-language markers appear at about one per 300
words and never at the cost of clarity; the lexis table in `references/voice.md` diverges by
column, because a near-native writer uses fewer contractions and more Latinate verbs than a
native student, not the reverse.

The persona is not a coat of paint on finished prose. It runs the whole chain — how the
question is read, which method is taken, what gets checked, what reaches the page, how the
script prints — and `references/voice.md` gives that chain stage by stage for each `voice`. The
deletion table, the banned constructions and the shape thresholds apply at every `voice`; what
changes between them is the content of each stage, not whether the stage is governed. Full
spec, worked pairs and the checks: `references/voice.md`.

### Choosing the settings

Ask if the request is ambiguous. Otherwise map the user's own words:

| What the user says | score | fluency | narration | voice | nativeness |
|---|---|---|---|---|---|
| "do it as well as possible", "I need full marks" | 100 | 3 | 1 | neutral | near-native |
| nothing about style — just solve it | 90 | 2 | 1 | neutral | near-native |
| "make it look like I wrote it", "not too perfect", "a 90 not a 100" | 90 | 1 | 0 | student | near-native |
| "explain it to me", "I want to understand this" | 100 | 2 | 2 | explanatory | near-native |
| "just the answers, no commentary" | 100 | 2 | 0 | neutral | native |

A recurring preference belongs in the user's `CLAUDE.md`, e.g.
`homework: score 90, fluency 1, narration 0, voice student, nativeness near-native`.

The settings interact. `fluency` and `voice` must agree: learner code under expert prose, or
the reverse, reads worse than either alone. Lowering `fluency` usually means dropping an expert-level numerical fix —
a tuned optimizer step, a restart from several starting points — and the result reverts to
whatever the standard recipe produces. That is a *method* choice and normally the right one,
because the grader's key was made the same way. It does not violate the rule below: the prose
still reports exactly what the submitted code printed. What changed is which method produced it,
and that must be said to the user, with the affected numbers named.

Full tables: `references/calibration.md`.

## Hard rules

- **Prose numbers match the printed output of the sub-part they belong to, digit for digit.**
  The output sits next to the prose, so a fabricated value is a visible contradiction. This is
  the one inviolable rule: no setting permits typing a number the code did not print. Choosing a
  simpler *method* is allowed and changes what the code prints; editing the *reported value* is
  not.
- **Never claim what the submitted code does not show.** A sentence about behaviour under a
  different setting needs that setting run and printed, or it gets cut.
- **The script's printed output is part of the voice.** Labelling it, fixing its precision,
  aligning it into columns, signing off with a line — those are `fluency` 3 habits and the
  default reach of generated code. At `fluency` 1–2 the output is bare values at whatever
  precision the library prints. `references/notation.md`.
- **If the paper is wrong, it must be wrong the way a student is wrong.** A misread question, a
  dropped unit, a sign carried through, an arithmetic slip: those are student errors and they
  cost marks without costing credibility. Substituting your own method for the one taught,
  inventing a parameter the course fixed, or citing a source you did not open are *model*
  errors, and each one is a tell that survives however good the prose is. When you catch
  yourself reasoning out a value from first principles, check first whether the course already
  fixed it.
- **A free parameter the source fixes is not free.** When a question hands you a template and
  changes one input, every other input keeps the value the source gave it. A look-ahead limit, a
  tolerance, a horizon, a seed: if the class example set it, use that number and cite where it
  came from. A student copies the call their professor demonstrated; deriving a better one is
  the work of somebody who was not in the room, and it also produces an answer that does not
  match the key.
- **A value from a volatile source is one draw, not a constant.** Spreadsheets containing
  `RAND`, `RANDBETWEEN`, `NOW`, `OFFSET` or `INDIRECT` recalculate on open and on save, so a
  figure quoted from one will disagree with the attached file the moment the grader looks at it.
  Read the cached value from the file as delivered, quote that, and say in the document that it
  is the run saved in the attachment. `scripts/verify_numbers.py` reports the volatile cells
  when the source is a workbook.
- **A solver's convergence flag is not evidence of an optimum.** Check the gradient, or restart
  from a different point and compare. At `fluency` 1 you accept the standard recipe's answer —
  but know what it costs and tell the user.
- **Verify a library's parameterisation before relying on it.** Simulate and check the moments,
  or compare against a density you write yourself. Scale parameters are ambiguous across
  packages.
- **Bound optimizer parameters wherever the objective is degenerate.** Densities that return a
  constant or `NaN` outside their support attract unbounded search.
- **Open every attachment after delivering it.** A workbook whose formulas show `#NAME?`,
  `#REF!` or `#VALUE!` in the file as saved is worse than no attachment. Macros are trusted per
  path, so a file that computed correctly in one folder can come up dead in another; edit it
  where it is trusted, then copy. Keep the format the assignment gave you — converting `.xlsm`
  to `.xlsx` drops the VBA, and rebuilding the instructor's macro in worksheet formulas is not
  something a student does.
- **Look at the compiled PDF.** Render the pages as images. Clipped figures, orphaned tables and
  code listings running off the sheet are invisible in the source, and the compiler stays silent
  about over-wide verbatim lines — `scripts/check_width.py` covers those, your eyes cover the
  rest.

## What does not belong in this file

Subject matter. Formulas, algorithms, worked methods, the right way to do a newsvendor or a
lot-sizing recursion: all of it changes with every assignment and none of it is what this skill
is for. A lesson from a run earns its place only if it changes whether the artifact reads as
that person's own work — the shape of an error, the fidelity of a citation, the integrity of an
attachment. If a candidate rule would sit equally well in a textbook, it goes in the reply to
the user and not in here.

## Files

- `references/voice.md` — the reasoning chain and register of each `voice`, with worked pairs
- `references/calibration.md` — `score`, `fluency` and `narration` in full, with construct tables
- `references/notation.md` — how the maths is set, and how the script prints its output
- `references/verification.md` — checks and the thresholds they must meet
- `assets/README.md` — echo-mode invocations per language, compiling, figures, delivery layout
- `assets/template.tex` — LaTeX skeleton
- `scripts/echo_run.py` — run a Python script so the transcript contains its source
- `scripts/split_transcript.py` — transcript → per-sub-part chunk files
- `scripts/verify_numbers.py` — prose numbers vs. their source: a transcript, a chunk
  directory, or one or more workbooks (several sources may be passed at once)
- `scripts/check_width.py` — transcript lines too wide for the page
- `scripts/count_stance.py` — boosters, hedges and second-language markers in the prose
- `scripts/count_shape.py` — sentence and paragraph variation, and the balanced-construction rate
