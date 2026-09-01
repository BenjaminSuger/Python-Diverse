from sys import argv


def convert_morse(sentence: str) -> str:
    NESTED_MORSE = {" ": "/ ", "A": ".- ", "B": " -... ", "C": "-.-. ",
                    "E": ". ", "F": "..-. ", "G": "--. ", "H": ".... ",
                    "I": ".. ", "J": ".--- ", "K": "-.- ", "L": ".-.. ",
                    "M": "-- ", "N": "-. ", "O": "--- ", "P": ".--. ",
                    "Q": "--.- ", "R": ".-. ", "S": "... ", "T": "- ",
                    "U": "..- ", "V": "...- ", "W": ".-- ", "X": "-..- ",
                    "Y": "-.-- ", "Z": "--.. ", "1": ".---- ", "2": "..--- ",
                    "3": "...-- ", "4": "....- ", "5": "..... ", "6": "-.... ",
                    "7": "--... ", "8": "---.. ", "9": "----. ", "0": "----- "}
    result = []
    for i in sentence:
        result.append(NESTED_MORSE[i.upper()])
    return ''.join(result)


if __name__ == "__main__":
    try:
        if len(argv) != 2:
            raise AssertionError("the arguments are bad")
        for i in argv[1]:
            if not (i.isalnum() or i == ' '):
                raise AssertionError("the arguments are bad")
        print(convert_morse(argv[1]))
    except AssertionError as e:
        print(f"AssertionError: {e}")
