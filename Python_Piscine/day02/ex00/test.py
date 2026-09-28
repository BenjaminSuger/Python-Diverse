from load_csv import load


def main():
    """main tester"""
    try:
        print(load("./data/life_expectancy_years.csv"))
    except Exception as e:
        print(f"{type(e).__name__} : {e}")


if __name__ == "__main__":
    main()
