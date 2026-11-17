# homework — a Claude skill

Hand Claude a problem set (images, PDF, or pasted text) plus its data files and get back a
solution set: sub-questions enumerated, answers computed, code and console output included
verbatim, typeset in LaTeX, compiled to PDF, and every printed number checked against the
output of its own sub-part.

Five settings tune the write-up: `score`, `fluency`, `narration`, `voice`, `nativeness`.
See [skills/homework/SKILL.md](skills/homework/SKILL.md).

## Install

**Claude Code (plugin, gets updates):**

```
/plugin marketplace add Aji-Q/homework-skill
/plugin install homework@homework-skill
```

Then run `/homework:homework`, or just hand Claude an assignment.

**Claude Code (plain skill):** copy `skills/homework/` into `~/.claude/skills/`, then `/homework`.

**Claude Desktop / claude.ai:** zip the `skills/homework/` folder (the zip root must be the
`homework/` folder) and upload it on the Skills page (under Customize, or Plugins in newer
builds) with "Upload a skill". Code execution must be enabled; whether the hosted container
has LaTeX is untested.

## Requirements

- A LaTeX distribution (`pdflatex` or `xelatex`) to compile the PDF
- Python 3 for the checkers in `skills/homework/scripts/`
- R or Python for the analysis itself, depending on the assignment

## 中文

把作业题目（图片、PDF 或粘贴的文字）和数据文件交给 Claude，产出一份可提交的解答：逐小问列出、
算出答案、代码与控制台输出原样收录、LaTeX 排版并编译成 PDF，每个印出来的数字都对照所在小问的
输出核对。安装命令见上；需要本机有 LaTeX 和 Python 3。
