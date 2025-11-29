"""
CP1404/CP5632 Practical 10 - Recursion examples.
"""

def do_it(n):
    """Return a simple recursive count pattern.

    Example:
        do_it(3) -> "1 2 3"
    """
    if n <= 0:
        return ""
    if n == 1:
        return "1"
    return f"{do_it(n - 1)} {n}"


def factorial(n):
    """Return n! using recursion.

    Example:
        factorial(5) -> 120
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def main():
    print("do_it(5) = ", do_it(5))
    print("factorial(5) = ", factorial(5))


if __name__ == "__main__":
    main()
