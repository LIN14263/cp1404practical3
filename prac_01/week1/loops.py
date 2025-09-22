"""CP1404/CP5632 - Practical 1
Loop practice tasks:
- odd numbers 1..20
- count by 10s 0..100
- countdown 20..1
- print n stars on one line
- print 1--n increasing star lines
"""

def main():
    # a) odd numbers 1..20
    for i in range(1, 21, 2):
        print(i, end=" ")
    print()

    # b) count in 10s 0..100
    for i in range(0, 101, 10):
        print(i, end=" ")
    print()

    # c) countdown 20..1
    for i in range(20, 0, -1):
        print(i, end=" ")
    print()

    # d) print n stars on one line
    n = int(input("Number of stars: "))
    print("*" * n)

    # e) print 1..n increasing star lines
    for i in range(1, n + 1):
        print("*" * i)

if __name__ == "__main__":
    main()
