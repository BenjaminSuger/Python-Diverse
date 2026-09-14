from array2D import slice_me


def main():
    """tester function with several cases"""
    try:
        family = [[1.80, 78.4], [2.15, 102.7], [2.10, 98.5], [1.88, 75.2]]
        print(slice_me(family, 0, 2))
        print(slice_me(family, 1, -2))
        family2 = [[1.80, 78.4], [2.15, 102.7], [2.10, 98.5], [4.14, 9],
                   [22.31, -45], [1.88, 75.2]]
        print(slice_me(family2, 0, 2))
        print(slice_me(family2, 1, -2))
        family3 = []
        print(slice_me(family3, 1, 5))
    except (TypeError, ValueError) as e:
        print(f"{type(e).__name__} {e}")
    try:
        family = [[1.80, 78.4], [2.15]]
        print(slice_me(family, 0, 2))
    except (TypeError, ValueError) as e:
        print(f"{type(e).__name__} {e}")
    try:
        family = ([1.80, 78.4], [2.15, 4.5])
        print(slice_me(family, 0, 2))
    except (TypeError, ValueError) as e:
        print(f"{type(e).__name__} {e}")
    try:
        family = [(1.80, 78.4), (2.15, 4.5)]
        print(slice_me(family, 0, 2))
    except (TypeError, ValueError) as e:
        print(f"{type(e).__name__} {e}")


if __name__ == "__main__":
    main()
