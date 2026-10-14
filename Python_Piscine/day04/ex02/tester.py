from callLimit import callLimit


@callLimit(3)
def f():
    """f()"""
    print("f()")


@callLimit(1)
def g():
    """g()"""
    print("g()")


def main():
    """main tester"""
    for i in range(3):
        f()
        g()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
