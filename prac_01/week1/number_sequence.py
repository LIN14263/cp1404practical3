"""CP1404/CP5632 - Practical 1
Print a number sequence based on start, end and step (inclusive).
"""

def main():
    start = int(input("Start: "))
    end = int(input("End: "))
    step = int(input("Step: "))
    while step == 0:
        print("Step cannot be 0.")
        step = int(input("Step: "))

    # Handle direction automatically
    if start <= end and step < 0:
        step = abs(step)
    if start > end and step > 0:
        step = -step

    for i in range(start, end + (1 if step > 0 else -1), step):
        print(i, end=" ")
    print()

if __name__ == "__main__":
    main()
