from sys import argv, stdin


def string_stat(sentence: str) -> None:
    """function counting sentence length, upper letters, punctuation
    marks, spaces and digits"""
    upper, lower, punctuation, spaces, digits = 0, 0, 0, 0, 0
    punctuations = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    for i in sentence:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
        elif i.isspace():
            spaces += 1
        elif i.isdigit():
            digits += 1
        elif i in punctuations:
            punctuation += 1
    print(f"The text contains {len(sentence)} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punctuation} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


def main():
    """main function taking the input"""
    try:
        if len(argv) > 2:
            raise AssertionError("Too many arguments")
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return 1
    if len(argv) == 2:
        string_stat(argv[1])
    else:
        print("What is the text to count?", flush=True)
        arg = stdin.readline()
        string_stat(arg)
    return 0


if __name__ == "__main__":
    main()
