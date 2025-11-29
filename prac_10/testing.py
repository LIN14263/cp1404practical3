"""
CP1404/CP5632 - Practical 10
testing.py - simple examples of tests using assert and doctest.
"""

import doctest

# 如果你的 Car 类在别的模块里，请把这里的 import 改成正确路径
# 例如: from prac_06.car import Car
try:
    from car import Car
except ImportError:  # 方便没有 Car 的时候还能运行 doctest
    Car = None


def repeat_string(s: str, n: int) -> str:
    """Return string s repeated n times, with spaces between.

    >>> repeat_string("hi", 2)
    'hi hi'
    >>> repeat_string("abc", 1)
    'abc'
    >>> repeat_string("x", 0)
    ''
    """
    if n <= 0:
        return ""
    return " ".join([s] * n)


def is_long_word(word: str, length: int = 5) -> bool:
    """Return True if word is at least as long as length.

    >>> is_long_word("hello")
    True
    >>> is_long_word("hi")
    False
    >>> is_long_word("Python", 6)
    True
    >>> is_long_word("test", 4)
    True
    """
    return len(word) >= length


def format_sentence(phrase: str) -> str:
    """Return phrase formatted as a sentence:
    - First character capitalised
    - Ends with a single full stop

    >>> format_sentence("hello world")
    'Hello world.'
    >>> format_sentence("Already fine.")
    'Already fine.'
    >>> format_sentence("python is fun!")
    'Python is fun!.'
    """
    phrase = phrase.strip()
    if not phrase:
        return ""
    # Capitalise first character, leave rest as is
    phrase = phrase[0].upper() + phrase[1:]
    if not phrase.endswith("."):
        phrase += "."
    return phrase


def run_simple_tests():
    """Run simple assert-based tests (no output if all pass)."""
    # repeat_string tests
    assert repeat_string("hi", 2) == "hi hi"
    assert repeat_string("a", 3) == "a a a"
    assert repeat_string("x", 0) == ""

    # is_long_word tests
    assert is_long_word("hello") is True
    assert is_long_word("hi") is False
    assert is_long_word("Python", 3) is True
    assert is_long_word("cat", 3) is True
    assert is_long_word("go", 3) is False

    # format_sentence tests
    assert format_sentence("hello world") == "Hello world."
    assert format_sentence("Already fine.") == "Already fine."
    assert format_sentence("test") == "Test."
    assert format_sentence("  spaced out  ") == "Spaced out."

    # Optional Car test – 只有在成功导入 Car 时才测
    if Car is not None:
        car = Car("Test", 100)
        assert car.fuel == 100


def main():
    """Run doctest then simple assert tests."""
    doctest.testmod()
    run_simple_tests()
    print("All tests passed.")


if __name__ == "__main__":
    main()
