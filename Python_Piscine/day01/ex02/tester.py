from load_image import ft_load


def main() -> None:
    """main tester"""
    try:
        print(ft_load("./images/landscape.jpg"))
    except Exception as e:
        print(f"{type(e).__name__} : {e}")
    print("\n========OTHER TEST========")
    try:
        print(ft_load("./images/potit_chat_fait_dodo.png"))
    except Exception as e:
        print(f"{type(e).__name__} : {e}")
    try:
        print(ft_load("does_not_exist"))
    except Exception as e:
        print(f"{type(e).__name__} : {e}")


if __name__ == "__main__":
    main()
