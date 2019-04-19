# pandas is used for data analysis  most widely used for data munging
# munging means ( example:a person is rolled by long wire ),python is used to arrange in proper way
# pandas is used to analysis the data in easier and faster way
# we can do same work in excel but for large data it will be difficult to process
# it takes the data from csv(comma separated value),excel,sql(structure query language )
import pandas as pd
# usually we can use pandas.command in the code instead of that we can use pd.command
# import pandas
from datetime import date
# usually we can import datatime from the data for know the current time and date and we can process using the data given by
from collections import Counter

# collections is used to store collection of data like list,dictionary ,set,tuple
df = pd.read_csv('store.csv')
# df means a dataframe .It is the object in pandas.we can use any variable to store .i used to store the retiving data
# usually dataframe is used to represent the data in rows and columns from tabular or excel sheet data
# inside the bracket we can mention the path of the csv file
# There are different filetype can pandas work with pd.filetype .which filetype the pandas want to read in my case. i gave  csv file as a input to the pandas
data_location = pd.read_csv('location.csv')
# created a global dictionary variable
dictionary = {}


# List all stores which have build_area greater than 4000
def list_of_stores_greater_than_4000(df):
    # getting the df data as a input
    list_of_store_name = []
    # index shows the index_value for each rows in the data.it is necessary to specify
    # rows is the variable we can use any other attributes .i used rows to retrive the data or columns
    # df.iterrows will iterate over the rows as (index,series) pairs .series means a value in the file
    for index, rows in df.iterrows():
        # used dictionary to store the one columns has a key (store) and another columns a value(built_area)
        dictionary[rows[0]] = rows[1]
    for key, value in dictionary.items():
        # check the store value is greater the user_input
        if value > 4000:
            # append the store name
            list_of_store_name.append(key)
    print(list_of_store_name)

 list_of_stores_greater_than_4000(df)


# Find country having the most number of stores
i = -1
def maximum_store_in_a_country(df):
    new_list = []
    for index, rows in df.iterrows():
        # converted the data from integer to string
        new_list.append(str(rows[3]))
    # used counter to count the number of times the value occurs in the list
    counted_the_occurrences = Counter(new_list)
    # process with dictionary make the counter has a dictionary
    converted_into_dictionary = dict(counted_the_occurrences)
    # dict.value() is sorted to identify the max_value
    max_value = sorted(converted_into_dictionary.values())
    # call the other function by passing the parameter
    maximum_store_in_the_country(max_value, converted_into_dictionary, i)


def maximum_store_in_the_country(max_value, result_in_dictionary, i):
    max_list = []
    country_list = []
    # to get the maximum store in the country ,check the maximum store value
    for key, value in result_in_dictionary.items():
        # if it present append into the max_list
        if value == max_value[i]:
            max_list.append(key)
    # make the other dictionary for city and pincode
    for index, rows in data_location.iterrows():
        dictionary[rows[1]] = rows[0]
    # iterate over dict to check the maximum_store
    for key, values in dictionary.items():
        if str(values) in max_list:
            country_list.append(key)
    # if there is no country in the list the data is invalid .so take the other max_value
    if len(country_list) == 0:
        i = i + i
        maximum_store_in_the_country(max_value, result_in_dictionary, i)

    else:
        # if country in the list print the country name
        print(country_list)


maximum_store_in_a_country(df)


# Find the total build_area of all stores built last year
def stores_built_in_last_year(df):
    split_the_date = []
    no_of_bulit_area = []
    # take the current year to find the last year details
    today = str(date.today())
    # split is used to find only the year in the date
    for i in today.split("-"):
        split_the_date.append(i)
    # finded the last year
    last_year = int(split_the_date[0]) - 1
    # convert to string to apply the slicing
    split_date = str(last_year)
    for index, rows in df.iterrows():
        dictionary[rows[2]] = rows[1]
    # extracted last two number in the year and compare with user_value
    for key, value in dictionary.items():
        if split_date[-2:] == key[-2:]:
            no_of_bulit_area.append(value)

    print(no_of_bulit_area)


stores_built_in_last_year(df)


# Find all stores which were opened on a weekend (Saturday or Sunday)
def find_the_store_opened_in_weekend(df):
    date_list = []
    week_days_name_list = []
    store_list = []
    final_store_list = []
    check_list = ['Saturday', 'Sunday']
    for index, rows in df.iterrows():
        date_list.append(rows[2])
        store_list.append(rows[0])
    my_dictionary = {'date_of_opening': date_list}
    # dataframe is used to make the dictionary or list in the rows and columns
    df = pd.DataFrame(my_dictionary)
    # the dataframe read the input as a string rather then datetime object.so it is difficult to perform an operation.
    # to_datatime helps to convert string datatime to python datetime object
    df['date_of_opening'] = pd.to_datetime(df['date_of_opening'])
    # the date is converted into week_days_name by using dt is accessor object for datatimelike  and day_name()
    # is a function to represent date in days
    df['week_days_names'] = df['date_of_opening'].dt.day_name()
    for index, rows in df.iterrows():
        week_days_name_list.append(rows[1])
    # zip is used to combine the different entity into single entity
    combining_the_dict = dict(zip(store_list, week_days_name_list))
    for key, value in combining_the_dict.items():
        if value in check_list:
            final_store_list.append(key)
    print(final_store_list)


find_the_store_opened_in_weekend(df)


# List stores which are located in a city containing character `z` in it
def list_store_located_in_z_city():
    city_name_list = []
    store_name_list = []
    output_store_list = []
    for index, rows in df.iterrows():
        store_name_list.append(rows[0])
    # count the no of occurrences of the store
    finding_the_occurrence_of_store_in_the_file = Counter(store_name_list)
    # assign into the dictionary
    converting_into_dictionary = dict(finding_the_occurrence_of_store_in_the_file)
    # extract only the keys from the store data
    extract_keys_from_the_dict = converting_into_dictionary.keys()
    for index, rows in data_location.iterrows():
        city_name_list.append(rows[1])
    # wrappe the store_data and city name for process
    dictionary_ = dict(zip(extract_keys_from_the_dict, city_name_list))
    # check with the city having the character z in it"
    for key, value in dictionary_.items():
        # check the character is present in the name of the city
        if "z" in value:
            output_store_list.append(key)
    print(output_store_list)


list_store_located_in_z_city()


# Calculate number of stores in each City
def calculate_number_of_stores():
    pincode_list_in_store = []
    pincode_data_in_location = []
    city_data_in_location = []
    for index, rows in df.iterrows():
        pincode_list_in_store.append(rows[3])
    # count the no of stores present in the store data  using primary key
    counting_the_store_occurrence = Counter(pincode_list_in_store)
    # assign as a dictionary
    result_in_dictionary = dict(counting_the_store_occurrence)
    for index, rows in data_location.iterrows():
        pincode_data_in_location.append(rows[0])
        city_data_in_location.append(rows[1])
    # wrapping the primary key and city data in  a dictionary
    combining_the_data = dict(zip(pincode_data_in_location, city_data_in_location))
    for key, value in result_in_dictionary.items():
        temp1 = key
        temp2 = value
        # check the each store and assign to corresponding city in the data
        for keys, values in combining_the_data.items():
            if temp1 == keys:
                dictionary[values] = temp2
            else:
                continue
    print(dictionary)


calculate_number_of_stores()
