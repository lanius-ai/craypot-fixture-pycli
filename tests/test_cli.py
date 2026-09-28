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


def test_words_are_split_on_non_letters_and_compared_case_insensitively():
    out = run(["-"], "The quick fox.\nThe lazy dog, the end.\n")
    assert out.returncode == 0
    assert out.stdout == "3 the\n1 dog\n1 end\n1 fox\n1 lazy\n1 quick\n"


def test_apostrophes_join_words():
    out = run(["-"], "Don't stop; don't.\n")
    assert out.stdout == "2 don't\n1 stop\n"
