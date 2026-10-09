from load_csv import load
from matplotlib.pyplot import (show, title, ylabel, xlabel,
                               FuncFormatter, MultipleLocator)


def parse(v) -> float:
    suffixes = {'k': 1e3, 'M': 1e6, 'B': 1e9}
    v = str(v).strip()
    if v[-1] in suffixes:
        return float(v[:-1]) * suffixes[v[-1]]
    return float(v)


def viz_population_total(country1: str, country2: str) -> None:
    """visualization of total population of a country"""
    data = load("./data/population_total.csv")
    if data.empty:
        print("No data loaded")
        return
    try:
        countries = [country1, country2]
        new_df = data.set_index('country').loc[countries].T.map(parse)
        new_df.index = new_df.index.astype(int)
    except Exception:
        print("Errors in data")
        return
    new_df = new_df.loc[1800:2050]
    ax = new_df.plot(color={country1: "blue", country2: "green"})
    ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _: f"{y / 1e6:.0f}M"))
    ax.yaxis.set_major_locator(MultipleLocator(20e6))
    ax.legend(loc="lower right")
    title("Population Projections")
    ylabel("Population")
    xlabel("Years")
    show()


def main():
    """main tester required"""
    try:
        viz_population_total('France', 'Belgium')
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
