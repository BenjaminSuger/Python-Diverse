from S1E9 import Character, Stark


def main():
    """main tester"""
    Ned = Stark("Ned")
    print(Ned.__dict__)
    print(Ned.is_alive)
    Ned.die()
    print(Ned.is_alive)
    print(Ned.__doc__)
    print(Ned.__init__.__doc__)
    print(Ned.die.__doc__)
    print("---")
    Lyanna = Stark("Lyanna", False)
    print(Lyanna.__dict__)


def main_error():
    """main error tester"""
    print("---")
    test = Character("chien", False)
    print(test.__doc__)


if __name__ == "__main__":
    try:
        main()
        main_error()
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
