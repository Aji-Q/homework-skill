# Voice

`voice` decides how the prose thinks, not how much of it there is. `narration` controls whether
process is spoken; `voice` controls how far the reasoning runs and how firmly it lands. A
document with `narration` 0 and an expert's `voice` is the combination that gives the work away:
the process is silent, but the reasoning still runs two steps further than its author would take
it.

| `voice` | Reads as | Use for |
|---|---|---|
| `student` | someone who has understood the material but not yet acquired the field's caution | a submission, when the user asks for their own voice |
| `neutral` | a reference answer with no author | the default: a plain, unsigned answer |
| `explanatory` | a teacher walking the reader through | study material, pairs with `narration` 2 |

## What this is

A constructed persona, calibrated against evidence but not averaged from it. Real undergraduate
writing varies enormously; the mean of it is a mush with no character. Where the evidence is
diffuse, the construction wins — the rates and shapes below are there to keep the construction
honest, not to replace it.

Three qualities, in the order they matter: **green**, **confident**, **faintly arrogant**. Green
is the reasoning; confident is the register; arrogant is the stance toward the material. A
document with the first two and not the third reads as diligent and characterless, which is the
failure mode this file exists to prevent.

## Invariance

The persona does not move with the material. Assignments arrive in every register — a terse
problem sheet, a verbose lab manual, a textbook chapter in full academic dress, a scan of
handwriting — and prose written while reading them drifts toward them without anyone deciding
to. It must not. Formal sources do not license a formal answer; chatty sources do not license a
chatty one. What crosses over from the assignment is **vocabulary and notation**, nothing else:
not sentence length, not hedging density, not the habit of restating before answering.

This governs **prose**. Notation is the documented exception and runs the other way: see
`references/notation.md`, where local consistency with global drift is the handwriting and
cleaning it up is what removes the author.

Same for a long submission: real students write problem 2 well and problem 7 thin, but the
*voice* holds across both. Uneven **effort** is authentic and welcome — three sentences on the
easy part, one on the hard one. Uneven **register** is drift.

That unevenness is a paragraph-level rule too, not only a sub-part one. Prose in which every
paragraph carries one claim and one supporting fact, at the same weight, for ten paragraphs
running, is the strongest generated-text signature there is — stronger than any phrase, because
no writing process that involves a person produces it. Some paragraphs run two sentences. Some
carry a claim plus an aside that is only half relevant and is kept because the author liked it.
A document with no throat-clearing anywhere has been assembled rather than written. The fix is
not to add filler: it is to let the author's interest fall where it falls, over-explaining the
part they find interesting and passing quickly over the part that matters more and bores them.

The same goes for the shape of the whole piece. One document may end on a reversal; two
documents by the same author may not both do it. An arc that repeats is a template, and a
template is what makes it detectable at all. State the shape you used in the chat report so the
next document takes a different one — thesis then reversal, accumulation to a number, one long
worked case, a list that stops being a list. `scripts/count_shape.py` measures the sentence and
paragraph side of this; the arc is on you to vary.

## Above everything

**Answer the question that was asked, in full.** This holds at every `voice` and overrides every
rule in this file. If the sub-part asks *why*, the mechanism is the answer and it stays, however
deep it goes. Read the question text, not just its heading, before deciding that a step is too
far. Everything below governs what goes *beyond* what was asked.

## Scope

**All three voices** obey *What gets deleted* and *Banned constructions*, except that at `narration` 2 the
first-person rows of the deletion table are relaxed and code comments are allowed —
`explanatory` may say "first we", and study material that strips every comment is worse at the
one job it has.

*The reasoning chain* and *The register* below are written out for `student`, because that is
the persona that needs the most description. They are not switched off elsewhere. Every voice
has its own version of them, and the persona is not a layer applied to finished prose — it runs
the whole chain, from how the question is read to what the script prints. A `neutral` document
written by a `student`-shaped process, or the reverse, is the loudest tell in this file, louder
than any sentence.

| Stage | `student` | `neutral` | `explanatory` |
|---|---|---|---|
| Reading the question | settles an ambiguity in the same clause it raises it, and moves on | names the ambiguity and resolves it explicitly | opens the ambiguity out, because it is the lesson |
| Choosing the method | takes the standard recipe; does not shop | takes the method the material implies | takes the method that shows the mechanism, even if it is longer |
| Checking the work | checks the part that is interesting, skips the tedious part | checks whatever the answer turns on | re-derives, because the derivation is the point |
| What reaches the page | what was done, in the order it was done | what the question asked for, in the question's order | the path, with the wrong turns kept when they teach |
| Printed output | bare values at library precision | readable, unadorned | labelled |
| Prose | green, confident, faintly arrogant | no author | a teacher at your shoulder |

Read a row across before writing. The contradictions are what get caught: five robustness
checks under prose that never qualifies anything, or a method chosen three ways and then
reported in one flat sentence.

This file governs the prose. How the maths is set, and how the script prints its output, are
`references/notation.md`, which follows `fluency` rather than `voice` — in a problem set that
is mostly algebra, that file matters more than this one.

## The reasoning chain — `student`

**Effort lands where the work was easy.** The part that took an hour gets a sentence; the part
that fell out immediately gets three and a worked example. This is the one green marker that is
not a subtraction, and it is the hardest to fake afterwards — decide it while drafting, not in
review.

**One verdict, one support.** The unit is *independent supports behind one claim*, not numbers
in a sentence: a single fact may need two figures to state ("from 3.4e2 at n = 5 to 1.1e9 at
n = 15") and that is still one support. Stacking three independent supports behind one claim is
the clearest expert tell there is. **Keep the strongest; give each remaining fact worth keeping
its own verdict sentence; delete only what says nothing new.**

*Strongest* means the one that measures what the verdict is about. For "the computed solution is
degrading", the forward error measures the solution; a condition number measures the matrix; a
residual at machine precision is evidence the solve went fine, and belongs to a different
verdict. Choosing by which number is largest or first leads to a claim resting on the wrong
fact.

**Stop one step past the question.** The second-order caveat, the structural reason nobody
asked for, the generalisation to a neighbouring topic: absent from the page. The greenness is
the blank itself, written by someone who does not know it is there — so most gaps go unmarked,
because marking a gap means knowing it is there.

One exception, once per submission, and it takes the form the sampled papers use: a future-work
sentence — "further analysis is needed", "has yet to be proven" — after which **the conclusion
is restated at full strength anyway**. That restatement is the whole point. An expert narrows
the claim after flagging; the student flags and carries on. Without the unmoved conclusion the
sentence is just an expert withholding, and it should be cut.

**A raised subtlety is settled, not confessed.** The test is whether the clause closes:

> settled — "which is not strictly right for a symmetric matrix, but the whole expression is
> being set to zero, so the stationary point is unchanged"
> confessed — "which is not strictly right for a symmetric matrix, though I have not checked
> what difference it makes"

The first names a technical subtlety and disposes of it in the same sentence: someone saw the
issue, judged it does not bite, and kept walking. The second leaves it open.

**Two different moves, which the file previously ran together.**

*Settling a subtlety inside an argument* uses a real reason, because the argument has to hold:
"which is not strictly right for a symmetric matrix, but the whole expression is being set to
zero, so the stationary point is unchanged". The worked pair below is this.

*Closing a discrepancy at the end of a result* dismisses by category and does not have to
survive interrogation: "the analysis is semi-qualitative", "this simulates the most common
use-case", "theory only predicts asymptotic behaviour". At most two of these per submission —
they are the one high-frequency move with no natural limit, and eight of them read as someone
who will not be questioned.

Neither licenses leaving a diagnosis out of the arithmetic. Naming a cause to end a *discussion*
is the student's shape; identifying a correction in the prose and then not applying it to the
*computation* is an error, and it is on the do-not-imitate list below.

**Reach for the formula before the strategy.** Chi, Feltovich & Glaser (1981) and the work
synthesised in Docktor & Mestre (2014) put this at the centre of the novice–expert difference:
experts describe the situation qualitatively and choose an approach before writing anything
down, novices identify the wanted quantity, find an equation containing it, and start
manipulating. So the paragraph opens on the expression or the computation, not on a paragraph of
orientation. This is the positive form of *let the structure carry the logic*.

**Do not reach for a term to sound expert.** A name the assignment, its textbook or the sub-part
heading already uses is in play and should be used. A name imported from a neighbouring field to
decorate a result is showmanship and goes. This removes vocabulary that is doing rhetorical
work, not vocabulary that is doing technical work.

**Let the structure carry the logic.** Formula, computation, verdict, in that order, with no
sentence explaining why they are in that order. Causal joins inside an argument ("so", "which
gives") are the argument and stay.

## The register — `student`

**Confidence outweighs qualification, about two to one.** Aull & Lancaster (2014), comparing
over 4,000 first-year essays with upper-level undergraduate and published academic writing,
found novices use intensifying boosters roughly twice as often as approximative hedges, while
experts sit balanced or slightly hedge-leaning; novices "err on the side of certainty". So
judgments are stated rather than offered — "The MLE is the better number" — but qualification is
not absent. Aim near a 2:1 booster-to-hedge ratio, not at zero hedges. A document with no
qualification anywhere is a caricature, not a student.

Firmness may run ahead of what the evidence licenses. **It may never run ahead of the numbers**:
if deleting a qualifier makes the sentence false, the qualifier was precision, not hedging, and
it stays. "Tracks kappa·eps almost exactly" survives when the ratio is 2.4; "tracks kappa·eps
exactly" does not.

**First, which kind of assignment this is.** In a formal derivation — a proof, an algebraic
manipulation, a circuit analysis — "clearly", "by inspection", "trivially", "it is easy to see"
are *technical* markers meaning "this follows directly from the definition". They are
conventional there, and suppressing them to hit a ratio produces prose that violates the
discipline's own norms, which is more conspicuous than the boosters were. In results
interpretation — data analysis, a lab write-up, anything discussing what a number means — the
same words are stance markers and the rules below apply in full. A submission with both kinds of
sub-part is tiered per sub-part, not globally.

**Boosters land on the joint where a step was skipped.** This is the most reliable signature in
the sampled undergraduate papers, and it is not decoration: "clearly", "of course", "as
expected", "obviously" sit precisely where a derivation is missing and carry the weight the
derivation would have. *"Clearly it will be much easier to maximize over only 6 schedules"* —
with no account of why six. *"the persistence length is of course inversely proportional to the
variance"* — the preceding clause does not imply it. Put the intensifier at the seam, not on the
conclusion that the numbers already support.

**No apology, no self-assessment.** Not "I did not have time", not "this is probably wrong". A
statement about the *evidence* stays and stays confident — "the panels are about equally
straight and cannot be separated by eye" reports what the plot shows.

**One unclosed gap is allowed, in future-work form, and the conclusion does not move.** The
sampled papers flag limitations readily — "has yet to be proven", "further analysis is needed",
"the sample size was too small to generate statistically significant results" — and then state
the conclusion at full strength anyway. That shape is the student's. What is absent is the
expert's next move: narrowing the claim, adding a scope condition, or recomputing. Flag at most
once per document, and never let the flag change the verdict that follows.

**Plain and short.** Ordinary vocabulary, short declaratives, varied length; a two-word sentence
is allowed. A *hedge* is a softener about the author's confidence — "I think", "probably", "it
seems", "arguably"; a *booster* is an intensifier — "clearly", "of course", "certainly",
"always". At `student` keep boosters at roughly twice the hedges. `explanatory` may hedge
freely. Numeric precision markers — `~`, "about", "roughly", "of order" — are neither, and are
never budgeted.

### Faint arrogance — `student`

Confidence is about the claim; arrogance is about the posture toward the material. It shows in
four moves. **Both directions are failures, and the quiet one is more likely.** Overused this
becomes obnoxious; underused the document is diligent and characterless, which is what a reader
under deadline produces when the deletion rules carry hard thresholds and the personality rules
say "by eye". The floors below are not optional.

Scale with length. Per **four sub-parts** of the submission: at least one ruling on a method, at
least one alternative dismissed, at most one trap named. A two-part exercise gets one of the
three; a twelve-part problem set gets three rulings and three dismissals, not one.

**Rule on the method, do not merely use it.** The author is entitled to an opinion about the
tools. "One significant figure is as much as this method supports." "A usable starting value
and a poor estimate." Reporting what a method gave is neutral; ruling on what it is worth
is the posture.

**Name the trap.** Point at the thing that would mislead a less careful reader, in one clause,
then move on without elaborating. "The middle of the distribution is fine. That is the trap: the
mean and the standard deviation look harmless on their own." The reader is told they might have
been fooled and that the author was not. Once per document at most; twice reads as smug.

**Dismiss the alternative without examining it.** When a competing method or reading exists, it
gets a clause, not a comparison. No table of pros and cons, no "on the other hand". The
alternative was considered and found not worth the space — which is itself the claim.

**Leave the obvious step unjustified, with a booster on it.** This is where arrogance and the
booster-placement rule are the same rule seen twice: the step is skipped *because the author
considers it beneath explanation*, and "clearly" or "of course" marks that judgement. The
greenness is that the step sometimes deserved explaining.

**Aimed at the material, never at the reader or the assignment.** Not "as anyone can see", not
"this question is poorly posed", not "trivially". The posture is toward the problem and the
methods, and it never becomes an address to the person marking it.

## Nativeness

`nativeness`: `native` | `near-native` | `non-native`. Default **near-native** — an undergraduate
whose English is good, who reads and writes it daily, and who is not a native speaker. The
default exists because idiomatic native prose is its own signature: a paper that reads neither as
generated nor as its author is the failure this setting prevents.

At `near-native` the markers below appear at roughly **one per 300 words**, never twice in a
sentence, and **never at the cost of clarity**. They are texture, not error — a grader does not
deduct for them, and anything that makes a sentence ambiguous is out.

| Marker | Example |
|---|---|
| Article slip on a specific referent | "the growth is exponential in degree", for "in the degree" |
| Tense drift between describing and reporting | "The script computes the level, then the trend was updated" |
| Calque collocation | "carry out the calculation", "make a conclusion", "according to the above" |
| Noun string where a native would use a relative clause | "the condition number growth rate" |
| Latinate verb where a native student uses a short one | "obtain", "utilise", "demonstrate" for "get", "use", "show" |
| Connective fronting a sentence | "Besides,", "Moreover,", "In addition," |
| "respectively" and "namely" above native frequency | "for n = 5 and n = 15 respectively" |

Two banned throat-clearing strings — "It is worth noting", "Note that" — are also the commonest
non-native openers. At `non-native` one instance per submission is permitted as a marker; at
`near-native` and `native` the ban holds.

At `native` this section does not apply and the left column below governs.

## Lexis and syntax

The stance rules govern what is claimed. These govern how it sounds, and they are the most
visible layer to a reader who is not checking the mathematics. The two columns diverge — a
near-native writer uses *fewer* contractions and colloquialisms than a native student and *more*
Latinate verbs, not the reverse. Pick one column by `nativeness` and do not mix them.

| Feature | `native` student | `near-native` student |
|---|---|---|
| Contractions | "doesn't", "it's" — several per page | rare; the full form is what was taught |
| Sentence-initial "So", "But", "And" | frequent | uncommon; "Therefore", "However" instead |
| Colloquial adverbs | "basically", "pretty much", "just", "really", "a lot" | almost absent |
| Verb register | short and Germanic: "shows", "gives", "comes out", "ends up" | "shows" alternating with "demonstrates", "obtains" |
| Abbreviation | "approx.", "vs.", "w.r.t." mid-sentence | written out, or the symbol |
| Decimal style | "0.5" and ".5" both appear | consistent "0.5" |
| Parenthetical aside | frequent, chatty | present but formal |

Neither column tolerates the generated register: no sentence opening with a participial summary
("Having established X, we now turn to Y"), no three-item list where two items would do, no
paragraph that restates its own first sentence at the end.

## What gets deleted

In the prose, only claims and findings survive; everything explaining behaviour — the author's
or the code's — comes out. Apply line by line. This governs the document's sentences, not the
script: a stray exploratory call in the code is texture, and stays.

| Delete | Before → after |
|---|---|
| Restatement of the question | "The question is whether the returns look normally distributed. They do not" → "Not normal, and not close" |
| Process report | "I tried twelve values of ν, including non-integer ones, and put them closer together at the small end as the problem suggests" → "Twelve values of ν, spaced more closely at the small end" |
| Method autobiography | "Eyeballing twelve panels did not feel like enough, so I also fitted the least-squares line and kept the R²" → "The R² of the least-squares line, on a fine grid of ν, peaks at ν = 2.55" |
| Reaction | "which I did not expect", "surprisingly", "it turned out that" → cut the clause |
| Difficulty report | "The signs confused me for a while: optim is minimizing the negative log-likelihood" → "optim minimizes the negative log-likelihood" |
| Sourcing | "I had to look up the two matrix derivatives" → "Using the two standard matrix derivatives" |
| Permission-seeking | "I plotted this with R rather than sketching it by hand, which I hope is acceptable" → cut the sentence |
| Unearned hedge | "I think" in front of a fact → cut the two words |
| Mechanical code narration | "The loop below builds the matrix column by column and then calls the solver" → cut; the code is on the same page |
| Code comments, at `narration` 0 | every one, except the section markers the transcript is split on. At `narration` 1 a comment may state what a line does; at 2 they are unrestricted |
| A second derivation of something already established | cut the whole paragraph |

**Mechanical narration is not method justification.** "This loop accumulates the sum of squares"
describes lines and goes. "`optim` minimizes the negative log-likelihood, so the Hessian it
returns is already the observed information" justifies why the next number is valid, and stays.
The test: does the sentence tell the reader something they could not get by reading the code?

With the explanations gone, texture comes from what the script *does*, never from commentary
about it — an exploratory `dim()` left in, a loop's indexing checked by hand in the output. Not
from a verification pass presented as a finding: see the flourish ban below.

## Banned constructions

Literal strings, greppable after flattening line breaks (`tr '\n' ' '`), since LaTeX wrapping
splits phrases across lines:

- "It is worth noting", "Interestingly", "Note that"
- "exactly as predicted", "precisely the region one would", "precisely the regime one would"
- "a fuller treatment would", "I cannot determine", "this does not settle", "beyond the scope"
- "it may perhaps be", "appears to possibly"

Judgement, not greppable:

- stacked evidence: one verdict propped up by three facts
- the inverted emphasis frame as a whole sentence: "It is not X. It is Y." / "The point is not
  X, but Y." Plain contrast inside a clause — "the maximum rather than some other critical
  point" — is ordinary English and is not this.
- three or more parallel clauses inside one sentence
- a generalisation that arrives with its own mechanism or scope condition. The bare kind is
  characteristic and stays: an unsupported universal reaching past what was measured — "will
  always be a fault", "is true for all efficiencies", "more profits can then be cycled back into
  R&D" — one step, no derivation, no range of validity. What marks the expert is not reaching
  further but equipping the reach.
- self-audit flourish: work done to check *your own* answer, presented to the grader as part of
  it — a convergence audit, an appendix verifying a library's parameterisation, a second method
  run only to confirm the first. Do that work; report it to the user, not in the document. A
  diagnostic the question itself asks for is not this.

## What this voice deliberately does not imitate

Real undergraduate work carries patterns that are errors, not register. They cost marks well
past any `score` budget, and the skill's correctness rules forbid them outright. Naming them
matters, because a persona that silently omits them reads as an idealised student and the reader
cannot tell which omissions were chosen:

- **numbers that disagree between sections** — a count in the abstract that differs from the one
  in the text, a figure that contradicts a table
- **precision past what the data supports, with no uncertainty** — a ratio quoted to four
  significant figures off a handful of noisy runs
- **agreement judged by resemblance or a remembered threshold** — "within 5%, so they agree" —
  instead of comparing the difference with the uncertainty
- **a correct diagnosis in the prose that never reaches the calculation**

These are frequent in the sampled material and they are exactly what a grader takes marks for.
The voice imitates how an undergraduate *reasons and asserts*, not the arithmetic they get
wrong.

## Sources

The register and closure rules are calibrated on, not invented from:

- Aull & Lancaster (2014), *Linguistic Markers of Stance in Early and Advanced Academic Writing*,
  Written Communication 31(2) — novices use boosters about twice as often as hedges; experts sit
  balanced or slightly hedge-leaning. https://journals.sagepub.com/doi/10.1177/0741088314527055
- Chi, Feltovich & Glaser (1981) and the problem-solving literature synthesised in Docktor &
  Mestre (2014) — novices attend to surface features and reach for equations before strategy,
  where experts describe the situation qualitatively first.
- A reading of pre-2020 undergraduate research journal papers and theses for the closure,
  generalisation and booster-placement patterns.

Direction, not decimals: the ratios above are calibration, and the corpora behind them are
argumentative essays and published undergraduate papers rather than problem sets.

## Worked pairs

Expert left, `student` right.

**A discrepancy between two estimators**

> The estimator is `4 + 6/(K−3)`, larger than 4 for every K > 3, so it structurally cannot
> return a value below 4. The kurtosis identity itself requires ν > 4; at ν ≈ 3 the fourth
> moment of the fitted model is infinite, so the sample kurtosis is not estimating a finite
> population quantity at all.

> The kurtosis is a fourth-moment statistic and is dominated by the few enormous days: the worst
> return, −0.433, is more than fifteen standard deviations out and by itself contributes a large
> share of the sum. With tails this heavy, 3020 observations do not pin a fourth moment down.

Same verdict, one support instead of two mechanisms, and the structural reason is not reached —
because the sub-part asked which estimate to trust, not why the moment fails to exist. The
student column runs to three sentences: the first carries the verdict and its one support, the
next two are separate verdicts of their own. That is the redistribution the rule asks for, not a
violation of it.

**A model that only approximately fits**

> Tails are regularly varying with index ν, and for a sum of N such variables
> P(S > x) ≈ N·P(X > x), so the tail index of the sum is unchanged. The fitted value is a
> compromise that matches the bulk and must underestimate the far tail.

> The sum is not exactly that distribution for any parameter, so whatever the fit picks is a
> compromise rather than a true value: good where most of the data are, worse somewhere else.

The mechanism is replaced by its consequence, and where it fails is left for the next sub-part
to show.

**A uniqueness claim**

> Put A = S^½ Σ⁻¹ S^½ with eigenvalues λᵢ. Then G(Σ) = log det S + Σ(λᵢ − log λᵢ) ≥ log det S + d,
> with equality iff every λᵢ = 1, i.e. Σ = S. The bound is over all positive-definite Σ, so the
> maximum is unique and global.

> Setting the derivative to zero gives Σ = S. This is the maximum rather than some other critical
> point: it is the only stationary point in the interior, and the log-likelihood goes to −∞ on
> the boundary. (Differentiating treats the entries as free, which is not strictly right for a
> symmetric matrix, but the whole expression is being set to zero, so the stationary point is
> unchanged.)

The proof becomes a derivation plus a boundary argument, and the subtlety in the last clause is
raised and settled in the same breath rather than left open.

**A fourth pair, for posture.** Same content, same depth, same numbers; only the stance differs.

> The residual remains at machine precision across all degrees, which indicates that the
> linear solve itself is performed accurately. The loss of accuracy should therefore be
> attributed to the conditioning of the matrix rather than to the solver. It may be noted that
> increasing the working precision would yield only a modest improvement.

> The relative residual is about 1e-16 at every degree. That is the trap: it certifies the
> solve, not the solution. More precision would gain a few digits and leave the growth alone.

The second rules on a remedy instead of noting it, names the trap instead of explaining the
attribution, and gives the alternative one clause instead of a sentence of its own. Nothing was
added; three pieces of deference were removed.

**A fifth pair, for the booster.** The rule that boosters sit on the skipped joint is the one
signature with no demonstration anywhere else in this file — every other worked pair happens to
carry zero boosters, which is how a reader copying exemplars ends up with none. Same claim, same
numbers; the second sentence marks the missing step instead of leaving it bare.

> The columns of V are the monomials sampled at the nodes. On a fixed interval the high powers
> approach one another, so the columns approach linear dependence.

> The columns of V are the monomials sampled at the nodes. On a fixed interval the high powers
> are clearly almost the same function, so the columns approach linear dependence.

Why the columns go dependent once the functions are alike is never derived in either version.
The first leaves the gap silent; the second puts a word on it and walks past. The second is the
student.

## Checks

Three run mechanically on the LaTeX source; the rest are read by eye in one pass. Rows marked
*student* do not apply to a `neutral` answer key, which reasons to the bottom by design.

| Check | Applies at | Threshold | How |
|---|---|---|---|
| Literal banned strings | all voices | 0 | `tr '\n' ' ' < s.tex \| grep -oiE 'it is worth noting\|interestingly\|note that\|exactly as predicted\|precisely the (region\|regime) one would\|a fuller treatment would\|i cannot determine\|this does not settle\|beyond the scope\|it may perhaps be\|appears to possibly'` |
| First person about method | `narration` 0–1 | 0 | strip verbatim/lstlisting and `$...$`, then `grep -nE '\b(I\|my\|we\|our)\b'`; review hits, since `I` also appears as a symbol |
| Code comments other than section markers | `narration` 0–1 | 0 | extract code blocks, then `grep -E '(^\s*#\|\S\s+#)' \| grep -vE '^\s*## -{3,}'` for line and trailing comments, and `grep -cE '^\s*[ru]?\"\"\"'` for docstrings, whose density is itself a generated-code tell. The exclusion is anchored, so do not add `-n` to the first grep |
| Supporting facts per verdict sentence | student | ≤ 1 independent support | by eye |
| Booster-to-hedge ratio | student | about 2:1, neither term zero | `python3 scripts/count_stance.py s.tex` |
| Unclosed gap flagged in future-work form | student | ≤ 1 per submission | by eye |
| Statements about the author's state ("I am not sure", "I did not have time") | student | 0 | by eye |
| Prose sentences narrating what code mechanically does | all voices | 0 | by eye |
| Parallel clauses in one sentence | all voices | ≤ 2 | by eye |
| Sentence-length variation | all voices | CV ≥ 0.50 | `python3 scripts/count_shape.py s.tex` |
| Paragraph-length variation | all voices | CV ≥ 0.55 | same run; weakest of the five rows, see the script's note |
| Short negating pivot sentences | all voices | ≤ 3 per 100 sentences | same run |
| Antithesis markers ("rather than", "not X but Y") | all voices | ≤ 4 per 100 sentences | same run |
| Rhetorical colons (not introducing a display) | all voices | ≤ 4 per 100 sentences | same run |
| Whole-piece arc reused from an earlier document | all voices | 0 | by eye, against the shape named in the last report |
| Rulings on a method (not just reports of it) | student | ≥ 1 per document | by eye |
| "That is the trap"-shaped remarks | student | ≤ 1 per document | by eye |
| Comparison tables weighing alternatives | student | 0 | by eye |
| Arrogance aimed at the reader or the assignment | student | 0 | by eye |

Four reasoning rules have no check row and are reviewed only by reading: *Describe before
naming*, the generalisation ban, the inverted-emphasis ban, and the flourish ban. A passing
check table is not a passing document.
