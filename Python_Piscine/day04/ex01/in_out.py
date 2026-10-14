def square(x: int | float) -> int | float:
    """square"""
    return x ** 2


def pow(x: int | float) -> int | float:
    """Exponentiation of argument by himself"""
    return x ** x


def outer(x: int | float, function) -> object:
    """outer function return inner"""
    count = 0

    def inner() -> float:
        """inner return new value"""
        nonlocal count
        nonlocal x
        count += 1
        x = function(x)
        return x
    return inner
