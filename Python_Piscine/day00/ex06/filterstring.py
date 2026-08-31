from sys import argv
from ft_filter import ft_filter


def filterstring(string: str, length: int) -> list[str]:
    """program filterstring core"""
    result = [x for x in ft_filter(lambda x: len(x) > length, string.split())]
    return result


if __name__ == "__main__":
    try:
        if len(argv) != 3:
            raise AssertionError
        try:
            int(argv[1])
        except ValueError:
            pass
        else:
            raise AssertionError
        result = filterstring(argv[1], int(argv[2]))
        print(result)
    except (AssertionError, ValueError):
        print("AssertionError: the arguments are bad")
