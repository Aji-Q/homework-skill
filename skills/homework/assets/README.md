# Capture, typesetting, delivery

## Getting the code into the transcript

`\VerbatimInput` shows whatever the transcript contains, so the run has to echo the source as
well as the output. Only R does this natively.

| Language | Command | Echoes source? |
|---|---|---|
| R | `R --quiet --no-save --file=s.R > t.txt 2>&1` | yes (`Rscript` does **not**) |
| Python | `python3 scripts/echo_run.py s.py [args] > t.txt 2>&1` | yes, via the bundled runner |
| anything else | run each section, print its source before its output | you must arrange it |

`python3 -u s.py` and IPython's `%run` print output only — a transcript captured that way has no
code in it. `scripts/echo_run.py` reproduces REPL behaviour: each statement echoed behind
`>>> ` / `... `, then executed, with bare expression values printed. It sets `sys.path[0]` to the
script's own directory, passes through `sys.argv`, and honours `__future__` imports, so imports
of neighbouring modules, command-line arguments and future statements behave as they do under
`python3 script.py`. The one remaining difference is deliberate: a bare expression prints its
repr, the way a REPL does. For a language with neither option, the pattern to copy is the same:
split the script at the markers, print the block, run the block.

Mark sections with a comment that survives echo, one per assignment sub-part:

```
## ------------------------------------------------------------------ 1(a)
```

`scripts/split_transcript.py` splits on these — tolerating a leading `> `, `>>> `, `In [3]: ` or
`julia> ` prompt — and writes `chunk/1a.txt`, `chunk/5_picture.txt` and so on.

- **Everything above the first marker is dropped** (it warns). Put a marker above the imports
  and the data-loading output if the document should show them.
- **Two markers with the same label is an error**, not a silent overwrite.
- **Files left over from an earlier run are reported**; `--clean` deletes them. Without this a
  renamed sub-part leaves a stale chunk that `\VerbatimInput` happily shows.
- **UTF-8 passes through unchanged.** XeTeX and LuaTeX — so tectonic — typeset it inside
  verbatim correctly, including a Unicode minus; CJK additionally needs a CJK font
  (`xeCJK`, or `fontspec` with a CJK family). Under pdfLaTeX non-ASCII in verbatim fails to
  compile: pass `--ascii`, which folds it and reports every substitution with line and column,
  so a mangled number cannot slip through.

## Layout on disk

Create the directories before the first run — `mkdir -p chunk fig` — or the first
`savefig("fig/q1a.pdf")` fails. The `.tex` file sits beside the directories it references:

```
solutions.tex      chunk/1a.txt ...      fig/q1a.pdf ...
solutions.pdf      analysis.R            transcript.txt
```

Figure filenames are yours to choose, but the `.tex` must match: `assets/template.tex` uses
`fig/q<sub-part>.pdf`. Write vector PDF from the plotting library — R `pdf("fig/q1a.pdf", ...)`
then `dev.off()`, matplotlib `savefig("fig/q1a.pdf")` — and include it inline rather than
floated so it stays with its discussion.

A single square plot sits well at `width=0.56\textwidth`; a panel grid wants the full width.
Tens of thousands of points make a multi-megabyte vector file: fine for submission, worth
mentioning if the user has an upload limit.

## Compiling

`tectonic solutions.tex` needs no TeX distribution and downloads the packages it uses, but
tectonic itself must be installed: `brew install tectonic`, `cargo install tectonic`, or a
release binary from the project. Where a full distribution already exists, `latexmk -pdf` or
`pdflatex` twice works instead.

Two width checks are needed, because they catch different things.

```bash
tectonic solutions.tex 2>&1 | grep -i overfull     # prose, displays, tables
python3 scripts/check_width.py chunk               # transcript lines
```

The compiler's warning does **not** fire for over-wide verbatim lines: each is set in a box that
runs quietly into the margin, and console output is exactly the content that produces them. So
`grep -ci overfull` can return 0 on a document whose code listings print off the sheet. Note also
that tectonic runs TeX more than once and repeats each warning, so a raw count is inflated —
read the distinct messages, not the number.

Fixes for prose overfulls, in order: break a wide display into `align*`, reduce a printed
precision, shrink `\tabcolsep`, split a wide table into stacked halves. For transcript lines:
drop to `\scriptsize`, widen the page, or shorten the printing in the script itself
(fewer columns per call, `options(width=...)` in R, `np.set_printoptions(linewidth=...)`).

## Delivery

Copy the whole tree — PDF, source, script, transcript, `chunk/`, `fig/` — into the destination,
then compile again **there**. If it builds, the relative paths are intact and the user can edit
and rebuild without you.
