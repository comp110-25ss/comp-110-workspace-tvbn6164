"""Mutating functions."""

__author__ = "730766558"


def manual_append(list: list[int], value: int) -> None:
    """Mutates by appending a value to the end of the list."""
    list.append(value)


def double(list: list[int]) -> None:
    """Mutates the list by doubling each value."""
    idx: int = 0
    while idx < len(list):
        list[idx] *= 2
        idx += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(list_2)

print(list_1)
print(list_2)
