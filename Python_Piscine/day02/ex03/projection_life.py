from load_csv import load
from matplotlib.pyplot import show
from pandas import concat


def projection_life_GDP() -> None:
    data_income = "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
    income = load("./data/" + data_income)
    life = load("./data/life_expectancy_years.csv")
    if income.empty or life.empty:
        print("Error in loading data")
        return
    try:
        check_income = list(income['country'])
        check_life = list(life['country'])
        if not check_income == check_life:
            print("Errors in the data loaded, review your data")
            return
        new_df = concat([life['1900'], income['1900']],
                        keys=['Life Expectancy', 'Gross domestic product'],
                        axis=1)
    except Exception:
        print("Errors in Data not found, review your input data")
    ax = new_df.plot.scatter(x='Gross domestic product',
                             y='Life Expectancy',
                             title="1900", logx=True)
    ax.set_xticks([300, 1000, 10000])
    ax.set_xticklabels(["300", "1k", "10k"])
    show()


def main():
    try:
        projection_life_GDP()
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
