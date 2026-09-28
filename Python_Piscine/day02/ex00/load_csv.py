from pandas import read_csv, set_option, DataFrame


def load(path: str) -> DataFrame:
    """load csv file and return pandas DataFrame"""
    try:
        resultat = read_csv(path)
    except Exception as e:
        return None
    print(f"Loading dataset of dimensions {resultat.shape}")
    set_option("display.show_dimensions", False)
    return resultat


def main():
    """main tester"""
    try:
        print(load("./data/life_expectancy_years.csv"))
        #print(load("./data/empty.csv"))
        #print(load("../requirements.txt"))
        #print(load(""))
    except Exception as e:
        print(f"{type(e).__name__} : {e}")


if __name__ == "__main__":
    main()
