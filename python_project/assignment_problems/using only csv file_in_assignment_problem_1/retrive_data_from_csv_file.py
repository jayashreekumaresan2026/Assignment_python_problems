import csv
from datetime import date
import datetime
from collections import Counter


def read_csv_for_store_data():
    with open('store.csv', 'r')as location_data:
        return list(csv.reader(location_data))


def read_csv_for_location_data():
    with open('location.csv', newline='', encoding='utf-8')as store_data:
        return list(csv.reader(store_data))

# List all stores which have build_area greater than 4000
def list_of_stores_greater_than_4000(csv_reader_for_store):
    dictionary = {}
    list_of_store_name = []
    for row in csv_reader_for_store:
        dictionary[row[0]] = row[1]
    for key, value in dictionary.items():
        if value > str(4000):
            list_of_store_name.append(key)
    list_of_store_name.pop(0)
    return list_of_store_name


# Find country having the most number of stores
i = -1
def maximum_store_in_a_country(csv_reader_for_store, csv_reader_for_location):
    new_list = []
    for rows in csv_reader_for_store:
        new_list.append(str(rows[3]))
    counted_the_occurrences = Counter(new_list)
    converted_into_dictionary = dict(counted_the_occurrences)
    max_value = sorted(converted_into_dictionary.values())
    maximum_store_in_the_country(max_value, converted_into_dictionary, i, csv_reader_for_location)


def maximum_store_in_the_country(max_value, result_in_dictionary, i, csv_reader_for_location):
    max_list = []
    country_list = []
    dictionary = {}
    for key, value in result_in_dictionary.items():
        if value == max_value[i]:
            max_list.append(key)
    for rows in csv_reader_for_location:
        dictionary[rows[1]] = rows[0]
    for key, values in dictionary.items():
        if str(values) in max_list:
            country_list.append(key)
    if len(country_list) == 0:
        i = i + i
        maximum_store_in_the_country(max_value, result_in_dictionary, i, csv_reader_for_location)

    else:
        print(country_list)


#  Find the total build_area of all stores built last year
def stores_built_in_last_year(csv_reader_for_store):
    dictionary = {}
    split_the_date = []
    no_of_built_area = []
    today = str(date.today())
    for i in today.split("-"):
        split_the_date.append(i)
    last_year = int(split_the_date[0]) - 1
    split_date = str(last_year)
    for rows in csv_reader_for_store:
        dictionary[rows[2]] = rows[1]
    for key, value in dictionary.items():
        if split_date[-2:] == key[-2:]:
            no_of_built_area.append(value)
    total_built_area = list(map(float, no_of_built_area))
    result_of_total_built = sum(total_built_area)

    return result_of_total_built


# Find all stores which were opened on a weekend (Saturday or Sunday)
def find_the_store_opened_in_weekend(csv_reader_for_store):
    date_list = []
    week_days_name_list = []
    store_list = []
    final_store_list = []
    check_list = ['Saturday', 'Sunday']
    for rows in csv_reader_for_store:
        store_list.append(rows[0])
        date_list.append(rows[2])
    date_list.pop(0)
    store_list.pop(0)
    for date in date_list:
         month, day, year = (int(x) for x in date.split('/'))
         if year == 00:
             year=int(2000)
             result=datetime.date(year,month,day)
             week_days_name_list.append(result.strftime("%A"))
         else:
             result = datetime.date(year, month, day)
             week_days_name_list.append(result.strftime("%A"))
    combining_the_dict = dict(zip(store_list, week_days_name_list))
    for key, value in combining_the_dict.items():
        if value in check_list:
            final_store_list.append(key)
    return final_store_list


# List stores which are located in a city containing character `z` in it
def list_store_located_in_z_city(read_csv_for_store_data,read_csv_for_location_data):
    city_name_list = []
    store_name_list = []
    output_store_list = []
    for  rows in read_csv_for_store_data:
        store_name_list.append(rows[0])
    finding_the_occurrence_of_store_in_the_file = Counter(store_name_list)
    converting_into_dictionary = dict(finding_the_occurrence_of_store_in_the_file)
    extract_keys_from_the_dict = converting_into_dictionary.keys()
    for rows in read_csv_for_location_data:
        city_name_list.append(rows[1])
    dictionary_ = dict(zip(extract_keys_from_the_dict, city_name_list))
    for key, value in dictionary_.items():
        if "z" in value:
            output_store_list.append(key)
    return output_store_list



#Calculate number of stores in each City
def calculate_number_of_stores(read_csv_for_store_data,read_csv_for_location_data):
    dictionary={}
    pincode_list_in_store = []
    pincode_data_in_location = []
    city_data_in_location = []
    for rows in read_csv_for_store_data:
        pincode_list_in_store.append(rows[3])
    counting_the_store_occurrence = Counter(pincode_list_in_store)
    result_in_dictionary = dict(counting_the_store_occurrence)
    for  rows in read_csv_for_location_data:
        pincode_data_in_location.append(rows[0])
        city_data_in_location.append(rows[2])
    combining_the_data = dict(zip(pincode_data_in_location, city_data_in_location))
    for key, value in result_in_dictionary.items():
        store_key = key
        store_values = value
        for keys, values in combining_the_data.items():
            if store_key == keys:
                dictionary[values] = store_values
            else:
                continue
    return dictionary

#Calculate number of stores  in extension problem each City
def calculate_number_of_stores_in_country(csv_reader_for_store,csv_reader_for_location):
    dictionary={}
    pincode_list_in_store = []
    for rows in csv_reader_for_store:
        pincode_list_in_store.append(rows[3])
    counting_the_store_occurrence = Counter(pincode_list_in_store)
    result_in_dictionary = dict(counting_the_store_occurrence)
    for rows in csv_reader_for_location:
        dictionary[rows[0]] = rows[2]
    country_names = list(set(dictionary.values()))
    result=country_name_list(country_names, result_in_dictionary,dictionary)
    print(result)


def country_name_list(country_names, result_in_dictionary,dictionary):
    dictionary_list = {}
    for i in range(len(country_names)):
        count = 0
        for keys, values in dictionary.items():
            pincode = keys
            if country_names[i] == values:
                for key, value in result_in_dictionary.items():
                    if pincode == key:
                        count += value
                dictionary_list[country_names[i]] = count
    return dictionary_list



def main():
    csv_reader_for_store = read_csv_for_store_data()
    print( list_of_stores_greater_than_4000(csv_reader_for_store))
    csv_reader_for_location = read_csv_for_location_data()
    print(maximum_store_in_a_country(csv_reader_for_store, csv_reader_for_location))
    print( stores_built_in_last_year(csv_reader_for_store))
    print(find_the_store_opened_in_weekend(csv_reader_for_store))
    print(list_store_located_in_z_city(csv_reader_for_store,csv_reader_for_location))
    print(calculate_number_of_stores(csv_reader_for_store,csv_reader_for_location))
    print(calculate_number_of_stores_in_country(csv_reader_for_store,csv_reader_for_location))
if __name__ == '__main__':
    main()
