while True:
    try:
        n = int(input("Size: "))

        if 1 <= n <= 10:
            break
        else:
            print("Invalid size! Enter a number from 1 to 10.")

    except ValueError:
        print("Invalid input! Please enter an integer.")

for row in range(1, n + 1):
    for col in range(1, n + 1):
        print(f"{row * col:4}", end="")
    print()