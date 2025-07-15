"""Practice for-looping over lists and dicts."""

__author__ = "730766558"

# Part 1.1 w_sum()


def w_sum(vals: list[float]) -> float:
    """Returns the sum of all elements in a list with while loop."""
    sum: float = 0.0
    i: int = 0
    while i < len(vals):
        sum += vals[i]
        i += 1
    return sum


# Part 1.2 f_sum()
def f_sum(vals: list[float]) -> float:
    """Returns the sum of all elements in a list using a for loop."""
    sum: float = 0.0
    for x in vals:
        sum += x
    return sum


# part 1.3 f_range_sum()
def f_range_sum(vals: list[float]) -> float:
    """Returns the sum of all integers in a range using a for loop."""
    sum: float = 0.0
    for i in range(len(vals)):
        sum += vals[i]
    return sum


# Part 2 Looping Over Dictionaries


# Part 2.1 get_keys()
def get_keys(d: dict[str, int]) -> list[str]:
    """Returns a list of keys in the dictionary."""
    keys: list[str] = []
    for key in d:
        keys.append(key)
    return keys


# Part 2.2 get_values()
def get_values(d: dict[str, int]) -> list[int]:
    """Produce a list of all values in the input dictionary."""
    values: list[int] = []
    for key in d:
        values.append(d[key])
    return values
