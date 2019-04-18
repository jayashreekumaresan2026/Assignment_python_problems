import pandas as pd
from datetime import date
from collections import Counter

df = pd.read_csv('store.csv')
df.head()
data_location = pd.read_csv('location.csv')
dictionary = {}

#List all stores which have build_area greater than 4000
def list_of_stores_greater_than_4000(df):
    list_of_store_name = []
    for index, rows in df.iterrows():
        dictionary[rows[0]] = rows[1]
    for key, value in dictionary.items():
        if value > 4000:
            list_of_store_name.append(key)
    print(list_of_store_name)

list_of_stores_greater_than_4000(df)


# Find country having the most number of stores
def maximum_store_in_dict(max_value, result_in_dictionary, i):
    max_list = []
    country_list = []
    for key, value in result_in_dictionary.items():
        if value == max_value[i]:
            max_list.append(key)
    for index, rows in data_location.iterrows():
        dictionary[rows[1]] = rows[0]
    for key, values in dictionary.items():
        if str(values) in max_list:
            country_list.append(key)
    if len(country_list) == 0:
        i = i + i
        maximum_store_in_dict(max_value, result_in_dictionary, i)

    else:
        print(country_list)

i = -1
def maximum_store_in_a_country(df):
    new_list = []
    for index, rows in df.iterrows():
        new_list.append(str(rows[3]))
    result = Counter(new_list)
    result_in_dictionary = dict(result)
    max_value = sorted(result_in_dictionary.values())
    result = maximum_store_in_dict(max_value, result_in_dictionary,i)
    print(result)


maximum_store_in_a_country(df)

#Find the total build_area of all stores built last year
def stores_built_in_last_year(df):
    split_the_date = []
    no_of_bulit_area = []
    today = str(date.today())
    for i in today.split("-"):
        split_the_date.append(i)
    last_year = int(split_the_date[0]) - 1
    split_date = str(last_year)
    for index, rows in df.iterrows():
        dictionary[rows[2]] = rows[1]
    for key, value in dictionary.items():
        if split_date[-2:] == key[-2:]:
            no_of_bulit_area.append(value)

    print(no_of_bulit_area)

stores_built_in_last_year(df)

#Find all stores which were opened on a weekend (Saturday or Sunday)
def find_the_store_opened_in_weekend(df):
    date_list = []
    week_days_name_list = []
    store_list = []
    final_store_list=[]
    check_list=['Saturday','Sunday']
    for index, rows in df.iterrows():
        date_list.append(rows[2])
        store_list.append(rows[0])
    my_dictionary = {'date_of_opening': date_list}
    df = pd.DataFrame(my_dictionary)
    df['date_of_opening'] = pd.to_datetime(df['date_of_opening'])
    df['week_days_names'] = df['date_of_opening'].dt.day_name()
    for index, rows in df.iterrows():
        week_days_name_list.append(rows[1])
    combining_the_dict=dict(zip(store_list,week_days_name_list))
    for key,value in combining_the_dict.items():
        if value in check_list:
            final_store_list.append(key)
    print(final_store_list)

find_the_store_opened_in_weekend(df)

#List stores which are located in a city containing character `z` in it
def list_store_located_in_z_city():
    city_name_list = []
    store_name_list = []
    new_store_list = []
    for index, rows in df.iterrows():
        store_name_list.append(rows[0])
    for index, rows in data_location.iterrows():
        city_name_list.append(rows[1])
    dictionary_ = dict(zip(store_name_list, city_name_list))
    for key, value in dictionary_.items():
        if "z" in value:
            new_store_list.append(key)
    print(new_store_list)

list_store_located_in_z_city()

#Calculate number of stores in each City
def calculate_number_of_stores():
    store_list = []
    city_data = []
    for index, rows in df.iterrows():
        store_list.append(rows[0])
    counting_the_store_occurrence = Counter(store_list)
    result_in_dictionary = dict(counting_the_store_occurrence)
    for index, rows in data_location.iterrows():
        city_data.append(rows[1])
    combining_the_data = dict(zip(city_data, store_list))
    for key, values in combining_the_data.items():
        if values in result_in_dictionary.keys():
            dictionary[key] = values
    print(dictionary)


calculate_number_of_stores()
