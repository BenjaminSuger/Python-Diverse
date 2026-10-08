from load_csv import load
from matplotlib.pyplot import show


def viz_life_expectancy(country: str) -> None:
    """visualization of life expectancy of a country"""
    data = load("./data/life_expectancy_years.csv")
    if data.empty:
        print("No data loaded")
        return
    try:
        graph = data.set_index("country").loc[country]
    except Exception:
        print(f"no data for {country}")
        return
    graph.plot(title=f"{country} Life expectancy Projections",
               xlabel="Year", ylabel="Life expectancy")
    show()


def main():
    try:
        viz_life_expectancy('France')
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
