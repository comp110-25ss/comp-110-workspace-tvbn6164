"""Implement algorithms to practice computational thinking."""

__author__ = "730766558"


# Part 1: all
def all(list: list[int], value: int) -> bool:
    """Returns a bool indicating whether the ints in a list are the same as given int"""
    for item in list:
        if item != value:
            return False
    return True


# Didn't take too long, but before for... in... it would take longer.


# Part 2: max
def max(list: list[int]) -> int:
    """Returns the largest value in the list"""
    if len(list) == 0:
        raise ValueError("max() arg is an empty List")  # if empty, raise error
    max_value: int = list[0]
    for item in list:
        if item > max_value:
            max_value = item
    return max_value


# Was confused about the raising valueerror.
# I remembered the playing cards during while loops.


# Part 3: is_equal
def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Returns a bool depending on if every element at every index is equal"""
    if len(list1) != len(list2):
        return False
    for i in range(len(list1)):
        if list1[i] != list2[i]:  # Saying that the indexes are equal in both lists.
            return False
    return True


# Took a second to figure out the index part. Longer than 2 mins.


# Part 4: extend
def extend(list1: list[int], list2: list[int]) -> None:
    """Mutates the first list by appending all elements from list2."""
    for item in list2:
        list1.append(item)


# This wasn't too bad. Less than 2 mins.
