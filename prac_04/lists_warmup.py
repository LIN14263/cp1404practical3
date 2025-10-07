"""
CP1404/CP5632 Practical 04 - Lists Warmup
Starting list and simple list operations.
"""

def main():
    numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

    # 1) Change the first element to "ten"
    numbers[0] = "ten"

    # 2) Change the last element to 1
    numbers[-1] = 1

    # 显示修改后的列表（可选，但通常助教会查看）
    print(numbers)

    # 3) Print all the elements from numbers[2:]
    print(numbers[2:])

    # 4) Check if 9 is in the list
    print(9 in numbers)

if __name__ == "__main__":
    main()
