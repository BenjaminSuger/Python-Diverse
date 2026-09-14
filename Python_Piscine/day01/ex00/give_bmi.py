from numpy import divide, power


def check_input(input: list[int | float]) -> None:
    """check the input needs to be a list and int or float"""
    if not isinstance(input, list):
        raise TypeError("Wrong Input: is not a list")
    if not input:
        raise ValueError("Wrong Input: empty list")
    for i in input:
        if not isinstance(i, (int, float)):
            raise TypeError("Wrong Input: is not composed of int or float")
        if i <= 0:
            raise ValueError("Wrong Input: Value cannot be 0 or negative")


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """give the bmi from 2 lists with numpy divide and power
    BMI formula weight / height^2 """
    check_input(height)
    check_input(weight)
    if len(height) != len(weight):
        raise AssertionError("give_bmi ; lists are not the same size")
    return divide(weight, power(height, 2)).tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """for each element in bmi check the limit"""
    check_input(bmi)
    if not isinstance(limit, int):
        raise TypeError("Apply_limit ; limit should be int")
    return [True if x > limit else False for x in bmi]


if __name__ == "__main__":
    try:
        result = give_bmi([4.0, 21.0, 6.6666], [4.0, 5, 9.2])
        result_apply = apply_limit(result, 15)
        print(f"Give BMI ; {result}")
        print(f"Apply limit; {result_apply}")
    except (TypeError, AssertionError, ValueError) as e:
        print(f"{type(e).__name__} {e}")
