def crunch(a: int, b: int) -> float:
    return (a + b) / 3


def measaure(val: int) -> str:
    return str(crunch(a=val, b=val) // 2) + ", cool!"


print(crunch(a=6, b=9))
