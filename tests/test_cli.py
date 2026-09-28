import subprocess
import sys

import pytest


def run(args, stdin=""):
    return subprocess.run(
        [sys.executable, "-m", "wordcount", *args],
        input=stdin, capture_output=True, text=True, check=False,
    )


def test_counts_simple_line():
    out = run(["-"], "a b a")
    assert out.returncode == 0
    assert out.stdout == "2 a\n1 b\n"


def test_empty_input_prints_nothing():
    out = run(["-"], "")
    assert out.returncode == 0
    assert out.stdout == ""


@pytest.mark.parametrize("top", ["0", "-2"])
def test_top_must_be_positive(top):
    out = run(["--top", top, "-"], "a")
    assert out.returncode == 2
    assert "--top must be at least 1" in out.stderr
