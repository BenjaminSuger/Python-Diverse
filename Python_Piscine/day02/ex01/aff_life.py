from load_csv import load
from matplotlib.pyplot import show, step


def viz_life_expectancy(country: str) -> None:
    data = load("./data/life_expectancy_years.csv")
    if data.empty:
        print(f"No data loaded")
        return
    graph = data[data['country'] == country].iloc[0].drop('country')
    country = country + " Life expectancy Projections"
    ax = graph.plot(title=country, xlabel="Years", ylabel="Life expectancy")
    show()


def main():
    try:
        viz_life_expectancy('France')
    except Exception as e:
        print(f"{type(e).__name__}: {e}")

if __name__ == "__main__":
    main()
