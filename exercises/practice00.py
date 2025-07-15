def f1(x: int) -> int:
    # This function takes an integer, adds 4 to it, prints the result,
    x += 4
    print(x)
    return x - 1


def f2(units: list[int]) -> None:
    # This function takes a list of integers, adds the first two elements,
    calc: int = units[0] + units[1]
    units.append(calc)


digits: list[int] = [3, 2]  # Initialize a list with two integers
f2(units=digits)  # Call f2 with the list

# this program will print the result of f1(3) and the modified list digits
# the result is f1(3) = 7 and digits = [3, 2, 5]
