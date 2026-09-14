from give_bmi import give_bmi, apply_limit


def main() -> None:
    """main tester"""
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    try:
        bmi = give_bmi(height, weight)
        print(bmi, type(bmi))
        print(apply_limit(bmi, 26))
    except (TypeError, AssertionError, ValueError) as e:
        print(f"AssertionError : {e}")
    try:
        height = (2.71, 1.15)
        weight = [165.3, 38.4]
        bmi = give_bmi(height, weight)
    except (TypeError, AssertionError, ValueError) as e:
        print(f"AssertionError : {e}")
    try:
        height = [2.71, 1.15]
        weight = [165.3, 'a']
        bmi = give_bmi(height, weight)
    except (TypeError, AssertionError, ValueError) as e:
        print(f"AssertionError : {e}")
    try:
        height = [2.71, 1.15]
        weight = [165.3, -42.4]
        bmi = give_bmi(height, weight)
    except (TypeError, AssertionError, ValueError) as e:
        print(f"AssertionError : {e}")


if __name__ == "__main__":
    main()
