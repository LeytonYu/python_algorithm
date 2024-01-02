def find_min_x_y(a, b, c):
    min_sum = float('inf')
    min_x, min_y = None, None

    for x in range(1, c + 1):
        y = (c - a * x) / b
        if y.is_integer() and y > 0:
            y = int(y)
            current_sum = x + y
            if current_sum < min_sum:
                min_sum = current_sum
                min_x, min_y = x, y

    return min_x, min_y, min_sum

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

x, y, min_sum = find_min_x_y(a, b, c)

if x is None or y is None:
    print("No valid solution found.")
else:
    print(f"x = {x}, y = {y}")
    print(f"Minimum sum x + y = {min_sum}")
