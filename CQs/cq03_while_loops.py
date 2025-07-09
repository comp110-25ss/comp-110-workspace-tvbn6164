"""Challenge Question with while loops."""

__author__ = "730766558"


def num_instances(phrase: str, search_char: str) -> int:
    """Counts the number of instances of a character in a string."""
    count: int = 0
    idx: int = 0
    # Loop through each character in the string
    while idx < len(phrase):
        # If the character at the index matches the search character, add to count
        if phrase[idx] == search_char:
            count += 1
        idx += 1
    return count
