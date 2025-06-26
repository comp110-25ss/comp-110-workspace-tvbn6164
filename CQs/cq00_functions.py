"""CQ00 Assignment"""

__author__ = "730766558"


def mimic(message: str) -> str:
    """Takes an input and repeats it back."""
    return message


def main() -> None:
    print(mimic(message=input("What is your message?")))
    return


if __name__ == "__main__":
    main()
