from numpy import divide, power


def check_input(input: list[int | float]) -> bool:
    """check the input needs to be a list and int or float"""
    if not isinstance(input, list):
        return False
    if not input:
        return False
    for i in input:
        if not isinstance(i, (int, float)):
            return False
        if i <= 0:
            return False
    return True


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """give the bmi from 2 lists with numpy divide and power
    BMI formula weight / height^2 """
    if not check_input(height) or not check_input(weight):
        raise AssertionError("give_bmi ; Input not valid")
    if len(height) != len(weight):
        raise AssertionError("give_bmi ; Input not valid")
    return divide(weight, power(height, 2)).tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """for each element in bmi check the limit"""
    if not check_input(bmi) or not isinstance(limit, int):
        raise AssertionError("Apply_limit ; input not valid")
    return [True if x > limit else False for x in bmi]


if __name__ == "__main__":
    try:
        result = give_bmi([4.0, 21.0, 6.6666], [4.0, 5, 9.2])
        result_apply = apply_limit(result, 15)
        print(f"Give BMI ; {result}")
        print(f"Apply limit; {result_apply}")
    except AssertionError as e:
        print(f"{type(e).__name__} {e}")
