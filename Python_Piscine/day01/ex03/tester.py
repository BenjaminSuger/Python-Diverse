from zoom import ft_zoom


def main() -> None:
    """main tester ft_zoom"""
    try:
        ft_zoom("./images/animal.jpeg")
    except Exception as e:
        print(f"{type(e).__name__} : {e}")


if __name__ == "__main__":
    main()
