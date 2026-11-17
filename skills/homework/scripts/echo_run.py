r"""Run a Python script the way an interactive interpreter would, so the transcript
contains the source as well as its output.

R echoes natively (R --quiet --no-save --file=s.R). Python does not: neither
"python3 -u s.py" nor IPython's %run prints the source lines, so a transcript captured
that way has no code in it and \VerbatimInput has nothing to show.

Statement boundaries come from the parse tree, so multi-line blocks (def, for, with,
try, class) are echoed and executed whole, and real line numbers survive into warnings
and tracebacks.

    python3 echo_run.py analysis.py > transcript.txt 2>&1

Comment lines, including "## ---- 1(a)" section markers, are echoed in place so
split_transcript.py can find them. stdout is line-buffered, so merging stderr with 2>&1
keeps warnings beside the statement that raised them.

The runtime is set up to match "python3 script.py args": sys.path[0] is the script's own
directory, sys.argv is the script's, and __future__ imports affect the statements after
them. What still differs from a plain run: the module is executed statement by statement,
so a bare expression prints its repr the way a REPL does.
"""
import __future__
import ast
import os
import sys
import traceback

FUTURE_FLAGS = {n: getattr(__future__, n).compiler_flag for n in __future__.all_feature_names}


def run(path, argv):
    try:
        sys.stdout.reconfigure(line_buffering=True)
    except AttributeError:
        pass

    # match what "python3 script.py args" sets up, so imports beside the script resolve
    # and the script sees its own argv
    sys.path[0] = os.path.dirname(os.path.abspath(path))
    sys.argv = [path] + list(argv)

    source = open(path, encoding="utf-8").read()
    lines = source.splitlines()
    tree = ast.parse(source, filename=path)
    env = {"__name__": "__main__", "__file__": path}

    def show(i, prompt):
        text = lines[i - 1]
        print(prompt + text if text.strip() else prompt.rstrip())

    def echo_gap(a, b):
        for i in range(a, b + 1):
            show(i, ">>> ")

    def echo_stmt(a, b):
        for i in range(a, b + 1):
            show(i, ">>> " if i == a else "... ")

    flags = 0          # __future__ imports must affect how later statements compile
    cursor = 1
    for node in tree.body:
        start = min([node.lineno] + [d.lineno for d in getattr(node, "decorator_list", [])])
        echo_gap(cursor, start - 1)
        echo_stmt(start, node.end_lineno)
        cursor = node.end_lineno + 1
        try:
            if isinstance(node, ast.Expr):
                code = compile(ast.Expression(node.value), path, "eval",
                               flags=flags, dont_inherit=True)
                value = eval(code, env)
                if value is not None:
                    print(repr(value))
            else:
                module = ast.Module(body=[node], type_ignores=[])
                exec(compile(module, path, "exec", flags=flags, dont_inherit=True), env)
                if isinstance(node, ast.ImportFrom) and node.module == "__future__":
                    for alias in node.names:
                        flags |= FUTURE_FLAGS.get(alias.name, 0)
        except SystemExit:
            raise
        except BaseException as exc:
            tb = exc.__traceback__.tb_next        # hide this runner's own frame
            traceback.print_exception(type(exc), exc, tb)
            sys.stdout.flush()
            sys.exit(1)
    echo_gap(cursor, len(lines))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("usage: python3 echo_run.py script.py [args...] > transcript.txt 2>&1")
    run(sys.argv[1], sys.argv[2:])
