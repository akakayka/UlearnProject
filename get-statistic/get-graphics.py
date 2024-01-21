import matplotlib.pyplot
import numpy
import pandas
import matplotlib.pyplot as plt
from matplotlib.axes import Axes


def read_data(file_path: str) -> pandas.DataFrame:
    return (
        pandas
        .read_csv(
            file_path,
            names=["name", "salary_from", "salary_to", "salary_currency", "area_name", "published_at"],
        )
        .loc[lambda df: df["salary_currency"] == "RUR"]
        .assign(
            year=lambda d: d["published_at"].apply(lambda date: date.split("-")[0]).astype(int),
            salary_from=lambda df: df["salary_from"].fillna(df["salary_to"]),
            salary_to=lambda df: df["salary_to"].fillna(df["salary_from"]),
            salary_avg=lambda df: (df["salary_from"] + df["salary_to"]) / 2
        )
    )


def filter_by_profession(dataframe: pandas.DataFrame, profession: str) -> pandas.DataFrame:
    return dataframe.loc[lambda df: df["name"].str.contains(profession, case=False)]


def salary_dynamic_by_years(dataframe: pandas.DataFrame, profession: str = None) -> dict:
    all_years = range(dataframe["year"].min(), dataframe["year"].max() + 1)
    if profession is not None:
        dataframe = filter_by_profession(dataframe, profession)
    return dataframe.groupby("year")["salary_avg"].mean().reindex(all_years, fill_value=0).round().to_dict()


def vacancies_count_by_years(dataframe: pandas.DataFrame, profession: str = None) -> dict:
    all_years = range(dataframe["year"].min(), dataframe["year"].max() + 1)
    if profession is not None:
        dataframe = filter_by_profession(dataframe, profession)
    return dataframe.groupby("year")["salary_avg"].count().reindex(all_years, fill_value=0).to_dict()


def filter_by_count(dataframe: pandas.DataFrame, threshold: float) -> pandas.DataFrame:
    return dataframe.groupby("area_name").filter(lambda df: df["salary_avg"].count() > threshold)


def salary_dynamic_by_cities(dataframe: pandas.DataFrame, profession: str = None) -> dict:
    if profession is not None:
        dataframe = filter_by_profession(dataframe, profession)
    dataframe = filter_by_count(dataframe, len(dataframe) // 100)
    return (
        dataframe
        .groupby("area_name")["salary_avg"]
        .mean().round()
        .reset_index()
        .sort_values(by=["salary_avg", "area_name"], ascending=[False, True])
        .set_index("area_name")["salary_avg"]
        .head(10)
    ).to_dict()


def vacancies_percentage_by_cities(dataframe: pandas.DataFrame, profession: str = None) -> dict:
    if profession is not None:
        dataframe = filter_by_profession(dataframe, profession)
    total_vacancies = len(dataframe)
    dataframe = filter_by_count(dataframe, total_vacancies // 100)
    return (
        dataframe
        .groupby("area_name")["salary_avg"]
        .size()
        .div(total_vacancies).mul(100).round(2)
        .reset_index()
        .sort_values(by=["salary_avg", "area_name"], ascending=[False, True])
        .set_index("area_name")["salary_avg"]
        .head(10)
    ).to_dict()


def add_years_bars(sub: Axes, dict_1: dict, dict_2: dict, label_1: str, label_2: str):
    x = numpy.array(list(dict_1.keys()))
    y_1 = numpy.array(list(dict_1.values()))
    y_2 = numpy.array(list(dict_2.values()))

    bar_width = 0.8
    sub.bar(x - bar_width / 4, y_1, width=bar_width / 2, label=label_1)
    sub.bar(x + bar_width / 4, y_2, width=bar_width / 2, label=label_2)
    sub.set_xticks(x)
    sub.tick_params(axis="both", labelsize=8)
    sub.tick_params(axis="x", rotation=90)
    sub.legend(fontsize=8)
    sub.grid(axis="y")


def add_cities_bar(sub: Axes, dict_: dict):
    y = [city.replace(" ", "\n").replace("-", "-\n") for city in dict_.keys()]
    x = list(dict_.values())

    sub.barh(y, x)
    sub.invert_yaxis()
    sub.tick_params(axis="x", labelsize=8)
    sub.tick_params(axis="y", labelsize=6)
    sub.set_yticks(y)
    sub.set_yticklabels(y, ha='right', va='center')
    sub.grid(axis="x")


def add_cities_pie(sub: Axes, dict_: dict):
    vals = [100 - sum(dict_.values())] + list(dict_.values())
    labels = ["Другие"] + list(dict_.keys())

    sub.pie(vals, labels=labels, startangle=0, textprops={'fontsize': 6})


def create_plot():
    csv = 'vacancies.csv'
    vac = input()
    data = read_data(csv)

    fig, sub = plt.subplots(2, 2)
    (sub_1, sub_2), (sub_3, sub_4) = sub

    add_years_bars(sub_1, salary_dynamic_by_years(data), salary_dynamic_by_years(data, vac),
                   "средняя з/п", f"з/п {vac}")
    add_years_bars(sub_2, vacancies_count_by_years(data), vacancies_count_by_years(data, vac),
                   "Количество вакансий", f"Количество вакансий {vac}")
    add_cities_bar(sub_3, salary_dynamic_by_cities(data))
    add_cities_pie(sub_4, vacancies_percentage_by_cities(data))

    plt.tight_layout()
    return sub