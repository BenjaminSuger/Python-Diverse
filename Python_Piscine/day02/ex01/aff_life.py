from load_csv import load
from matplotlib.pyplot import show, step


def main():
    data = load("./data/life_expectancy_years.csv")
    if data.empty:
        print(f"No data loaded")
        return 1
    graph = data[data['country'] == 'France'].iloc[0].drop('country')
    country = "France" + " Life expectancy Projections"
    ax = graph.plot(title=country, xlabel="Years", ylabel="Life expectancy")
    show()


if __name__ == "__main__":
    main()
