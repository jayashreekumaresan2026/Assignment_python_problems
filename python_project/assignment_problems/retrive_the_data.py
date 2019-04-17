import pandas
from datetime import date
from collections import Counter

df = pandas.read_csv('store.csv')
data_location = pandas.read_csv('location.csv')
dictionary = {}


def list_of_stores_greater_than_4000(df):
    list_of_store_name = []
    for index, rows in df.iterrows():
        dictionary[rows[0]] = rows[1]
    for key, value in dict.items():
        if value > 4000:
            list_of_store_name.append(key)
    print(list_of_store_name)


list_of_stores_greater_than_4000(df)


def maximum_store_in_a_country(df):
    new_list = []
    max_list = []
    country_list = []
    for index, rows in df.iterrows():
        new_list.append(str(rows[3]))
    result = Counter(new_list)
    result_in_dictionary = dict(result)
    print(result_in_dictionary)
    max_value = sorted(result_in_dictionary.values())
    print(max_value)
    print(max_value[-6])
    for key, value in result_in_dictionary.items():
        if value == max_value[-2]:
            max_list.append(key)
    print(max_list)
    for index, rows in data_location.iterrows():
        dictionary[rows[1]] = rows[0]
    for key, values in dictionary.items():
        if str(values) in max_list:
            country_list.append(key)
    print(country_list)


maximum_store_in_a_country(df)


def stores_built_in_last_year():
    split_the_date = []
    today = str(date.today())
    for i in today.split("-"):
        split_the_date.append(i)
    last_year = int(split_the_date[0]) - 1
    print(last_year)


stores_built_in_last_year()



