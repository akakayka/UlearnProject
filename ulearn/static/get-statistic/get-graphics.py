import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt

def render_mpl_table(data, col_width=3.0, row_height=0.625, font_size=14,
                     header_color='#40466e', row_colors=['#f1f1f2', 'w'], edge_color='w',
                     bbox=[0, 0, 1, 1], header_columns=0,
                     ax=None, **kwargs):
    if ax is None:
        size = (np.array(data.shape[::-1]) + np.array([0, 1])) * np.array([col_width, row_height])
        fig, ax = plt.subplots(figsize=size)
        ax.axis('off')
    mpl_table = ax.table(cellText=data.values, bbox=bbox, colLabels=data.columns, **kwargs)
    mpl_table.auto_set_font_size(False)
    mpl_table.set_fontsize(font_size)

    for k, cell in mpl_table._cells.items():
        cell.set_edgecolor(edge_color)
        if k[0] == 0 or k[1] < header_columns:
            cell.set_text_props(weight='bold', color='w')
            cell.set_facecolor(header_color)
        else:
            cell.set_facecolor(row_colors[k[0]%len(row_colors) ])
    return ax.get_figure(), ax

currency_dict = {
    "AZN": 51.5563,
    "BYR": 27.8408,
    "EUR": 95.6007,
    "GEL": 32.9718,
    "KGS": 98.1295,
    "KZT": 19.4177,
    "RUR": 1,
    "UAH": 2.31474,
    "USD": 87.6457,
    "UZS": 0.007135,
}

def get_avg_salary(row, conversion_rates):
    if pd.isna(row['salary_from']):
        avg_salary = row['salary_to']
    elif pd.isna(row['salary_to']):
        avg_salary = row['salary_from']
    else:
        avg_salary = (row['salary_to'] + row['salary_from']) / 2

    if pd.isna(row['salary_currency']):
        currency_rate = 1
    else:
        currency_rate = conversion_rates[row['salary_currency']]

    avg_salary_rub = avg_salary * currency_rate
    return avg_salary_rub

dtype_dict = {'name': 'str','key_skills': 'str', 'salary_from': 'float64', 'salary_to': 'float64',
              'salary_currency': 'str', 'area_name': 'str', 'published_at': 'str'}
df = pd.read_csv('vacancies.csv', dtype=dtype_dict)
df = df.dropna(subset=['salary_from', 'salary_to'], how='all')
df = df.dropna(subset=['salary_currency'], how='all')
df = df.dropna(subset=['area_name'], how='all')
df = df.dropna(subset=['published_at'], how='all')
print(df)
df['published_at'] = df['published_at'].apply(lambda x: datetime.datetime.strptime(x[:10], '%Y-%m-%d'))


df['year_published'] = df['published_at'].dt.year


df['average_salary'] = df.apply(lambda row: get_avg_salary(row, currency_dict), axis=1)
df = df.query('average_salary <= 500000')

df['published_at'] = pd.to_datetime(df['published_at'])


df['year_published'] = df['published_at'].dt.year


avg_salary_year = df.groupby('year_published')['average_salary'].mean()
vacancy_count_by_year = df.groupby('year_published').size()





plt.figure(figsize=(7, 4))
plt.plot(avg_salary_year.index, avg_salary_year.values, marker='o')
plt.title('Динамика уровня зарплат по годам')
plt.xlabel('Год')
plt.ylabel('Средняя зарплата')

plt.savefig('graphics/salary_year.png')

sf = pd.DataFrame({'Год':avg_salary_year.index, 'Зарплата':np.round(avg_salary_year.values,
                                                                    decimals = 0)})
fig,ax = render_mpl_table(sf, header_columns=0, col_width=2.0)
fig.savefig("graphics/table_salary_year.png")


plt.figure(figsize=(7, 4))
plt.plot(vacancy_count_by_year.index, vacancy_count_by_year.values, marker='o', color='b')
plt.title('Динамика количества вакансий по годам')
plt.xlabel('Год')
plt.ylabel('Количество вакансий')
plt.savefig('graphics/count_year.png')
sf = pd.DataFrame({'Год':vacancy_count_by_year.index, 'Количество': np.round(vacancy_count_by_year.values,
                       decimals = 0)  })
fig,ax = render_mpl_table(sf, header_columns=0, col_width=2.0)
fig.savefig("graphics/table_count_year.png")


selected_df = df[df['name'].str.contains("1С") | df['name'].str.contains("1C")]


average_salary_by_year_selected = selected_df.groupby('year_published')['average_salary'].mean()
vacancy_count_by_year_selected = selected_df.groupby('year_published').size()


plt.figure(figsize=(7, 4))
plt.plot(average_salary_by_year_selected.index, average_salary_by_year_selected.values, marker='o', color='b')
plt.title('Динамика уровня зарплат для профессии 1С-разработчик по годам')
plt.xlabel('Год')
plt.ylabel('Средняя зарплата')
plt.rc('xtick', labelsize= 10 )
plt.savefig('graphics/salary_year_vac.png')
sf = pd.DataFrame({'Зарплата':np.round(average_salary_by_year_selected.values), 'Год':average_salary_by_year_selected.index})
fig,ax = render_mpl_table(sf, header_columns=0, col_width=2.0)
fig.savefig("graphics/table_salary_year_vac.png")

plt.figure(figsize=(7, 4))
plt.plot(vacancy_count_by_year_selected.index, vacancy_count_by_year_selected.values, marker='o', color='b')
plt.title('Динамика количества вакансий для профессии 1С-разработчик по годам')
plt.xlabel('Год')
plt.ylabel('Количество вакансий')
plt.savefig('graphics/count_year_vac.png')

sf = pd.DataFrame({'Год':vacancy_count_by_year_selected.index, 'Количество':np.round(vacancy_count_by_year_selected.values,
                       decimals = 0)})
fig,ax = render_mpl_table(sf, header_columns=0, col_width=2.0)
fig.savefig("graphics/table_count_year_vac.png")


avg_salary_year = df.groupby('area_name')['average_salary'].mean()
vacancy_count_by_year = df.groupby('area_name').size().sort_values(ascending=False).head(10)
avg_salary_year = avg_salary_year.sort_values(ascending=False).head(10)

plt.figure(figsize=(21, 7))
plt.barh(avg_salary_year.index, avg_salary_year.values )
plt.title('Динамика уровня зарплат по городам')
plt.xlabel('Город')
plt.ylabel('Средняя зарплата')
plt.savefig('graphics/salary_city.png')

sf = pd.DataFrame({'Город':avg_salary_year.index, 'Зарплата':np.round(avg_salary_year.values,
                                                                      decimals = 0)})
fig,ax = render_mpl_table(sf, header_columns=0, col_width=5.0)

fig.savefig("graphics/table_salary_city.png")


plt.figure(figsize=(15, 7))
plt.barh(vacancy_count_by_year.index, vacancy_count_by_year.values, color='b')
plt.title('Динамика количества вакансий по городам')
plt.xlabel('Город')
plt.ylabel('Количество вакансий')

plt.savefig('graphics/count_city.png')

sf = pd.DataFrame({'Город':vacancy_count_by_year.index, 'Количество':np.round(vacancy_count_by_year.values,
                       decimals = 0)})
fig,ax = render_mpl_table(sf, header_columns=0, col_width=3.0)
fig.savefig("graphics/table_count_city.png")


selected_df = df[df['name'].str.contains("1С") | df['name'].str.contains("1C") | df['name'].str.contains("1c")
            | df['name'].str.contains("1 c") | df['name'].str.contains("1с") | df['name'].str.contains("1 с")]


average_salary_by_year_selected = selected_df.groupby('area_name')['average_salary'].mean()
vacancy_count_by_year_selected = selected_df.groupby('area_name').size().sort_values(ascending=False).head(10)
average_salary_by_year_selected = average_salary_by_year_selected.sort_values(ascending=False).head(10)

plt.figure(figsize=(27, 7))
plt.barh(average_salary_by_year_selected.index, average_salary_by_year_selected.values, color='b')
plt.title('Динамика уровня зарплат для профессии 1С-разработчик по городам')
plt.ylabel('Город')
plt.xlabel('Средняя зарплата')

plt.savefig('graphics/salary_city_vac.png')

sf = pd.DataFrame({'Город':average_salary_by_year_selected.index, 'Зарплата':np.round(average_salary_by_year_selected.values,
                       decimals = 0)})
fig,ax = render_mpl_table(sf, header_columns=0, col_width=6.0)
fig.savefig("graphics/table_salary_city_vac.png")


plt.figure(figsize=(15, 7))
plt.barh(vacancy_count_by_year_selected.index, vacancy_count_by_year_selected.values, color='b')
plt.title('Динамика количества вакансий для профессии 1С-разработчик по городам')
plt.ylabel('Город')

plt.xlabel('Количество вакансий')
plt.savefig('graphics/count_city_vac.png')

sf = pd.DataFrame({'Количество':np.round(vacancy_count_by_year_selected.values,
                       decimals = 0), 'Город':vacancy_count_by_year_selected.index})
fig,ax = render_mpl_table(sf, header_columns=0, col_width=4.0)
fig.savefig("graphics/table_count_city_vac.png")

skills = df['key_skills'].str.split('\n').explode().value_counts()

top_skills = skills.head(20)

colors = plt.cm.tab20c(range(len(top_skills)))
plt.figure(figsize=(10, 6))
bars = plt.barh(top_skills.index[::-1], top_skills.values[::-1], color=colors[::-1])

plt.title('Топ 20 популярных навыков')
plt.xlabel('Количество')
plt.ylabel('Навык')

handles = [plt.Rectangle((0,0),1,1, color=color) for color in colors]
plt.legend(handles[::], top_skills.index[::], loc='lower right', fontsize= 8)


plt.gca().axes.get_xaxis().set_visible(False)
plt.gca().axes.get_yaxis().set_visible(False)

plt.savefig('graphics/skills.png')

skills = selected_df['key_skills'].str.split('\n').explode().value_counts()

top_skills = skills.head(20)

colors = plt.cm.tab20c(range(len(top_skills)))
plt.figure(figsize=(10, 6))
bars = plt.barh(top_skills.index[::-1], top_skills.values[::-1], color=colors[::-1])

plt.title('Топ 20 популярных навыков\nдля 1C-разработчика')
plt.xlabel('Количество')
plt.ylabel('Навык')


handles = [plt.Rectangle((0,0),1,1, color=color) for color in colors]
plt.legend(handles[::], top_skills.index[::], loc='lower right', fontsize= 8)


plt.gca().axes.get_xaxis().set_visible(False)
plt.gca().axes.get_yaxis().set_visible(False)


plt.savefig('graphics/skills_vac.png')