from numpy import asarray


def check_input(family: list, start: int, end: int) -> None:
    """check the input is a list, int for values and same lenght overall"""
    if not isinstance(family, list):
        raise TypeError("Wrong Input : Not a list")
    if not family:
        var = "Wrong Input : List empty or wrong shape should be 2D array"
        raise ValueError(var)
    if not isinstance(start, int) or not isinstance(end, int):
        var = "Wrong Input : start and end needs to be int type"
        raise TypeError(var)
    if not all(isinstance(i, list) for i in family):
        var = "Wrong Input : all elements in the list are not a list"
        raise ValueError(var)
    if not all(len(family[0]) == len(i) for i in family):
        var = "Wrong Input : all elements in the list are not the same length"
        raise ValueError(var)


def slice_me(family: list, start: int, end: int) -> list:
    """function slicing list with numpy and changing shape"""
    check_input(family, start, end)
    family = asarray(family)
    print(f"My shape is : {family.shape}")
    family = family[start:end]
    print(f"My new shape is : {family.shape}")
    return family.tolist()


if __name__ == "__main__":
    pass
