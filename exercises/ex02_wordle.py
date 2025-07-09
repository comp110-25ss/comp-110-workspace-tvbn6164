"""Exercise 2: Wordle Game"""

__author__ = "730766558"


# Part 1: contains_char
def contains_char(word: str, char: str) -> bool:
    """Function is True if the character is found in any index of the word"""
    assert len(char) == 1, f"len('{char}') is not 1"
    idx: int = 0
    while idx < len(word):  # looping through each char of the word
        if word[idx] == char:
            return True
        idx += 1
    return False  # ending the check after every char has been checked


# This was my fastest section


# Part 2: emojified
def emojified(guess: str, secret: str) -> str:
    """Function returns a string of emojis whose color codifies the result of a guess"""
    assert len(guess) == len(secret), "Guess must be same length as secret"
    result: str = ""
    idx: int = 0
    while idx < len(
        guess
    ):  # loop to place emojis in right places. I kept messing up the yellow one
        if guess[idx] == secret[idx]:
            result += "\U0001f7e9"
        elif contains_char(secret, guess[idx]):
            result += "\U0001f7e8"
        else:
            result += "\U00002b1c"
        idx += 1
    return result


# This part was confusing but I got it now. I didn't use contains_char right


# Part 3: input_guess
def input_guess(N: int) -> str:
    """Function prompts the user for a guess and checks if it is the expected length"""
    guess: str = input("Enter a " + str(N) + " character word: ")
    while len(guess) != N:  # loop until right length
        guess = input("That wasn't " + str(N) + " chars! Try again: ")
    return guess


# This part wasn't as hard as before


# Part 4: main
def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    assert len(secret) >= 1, "Secret word must be at least 1 character long"
    turns: int = 1
    while turns <= 6:  # loop for 6 turns and use emojified to show emoji results
        print("=== Turn " + str(turns) + "/6 ===")
        guess: str = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            print("You won in " + str(turns) + "/6 turns!")
            return
        turns += 1
    print("X/6 - Sorry, try again tomorrow!")


# Trialed and error but it didn't work then I got it. I did 0 turns at first

if __name__ == "__main__":
    main(secret="codes")
