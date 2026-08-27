from sys import argv


def is_valid(value: str) -> bool:
    if value[0] == '-' or value[0] == '+':
        return value[1:].isnumeric()
    return value.isnumeric()


def main():
    try:
        if len(argv) > 2:
            raise AssertionError("more than one argument is provided")
        if len(argv) < 2:
            raise AssertionError("missing one argument")
        if not is_valid(argv[1]):
            raise AssertionError("argument is not an integer")
        print("I'm Even." if int(argv[1]) % 2 == 0 else "I'm Odd.")
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
