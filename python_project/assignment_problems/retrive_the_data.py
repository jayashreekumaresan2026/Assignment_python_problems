import pandas

df = pandas.read_csv('store.csv')


def list_of_stores_greater_than_4000(df):
    list_of_store_name = []
    dict = {}
    for index, rows in df.iterrows():
        dict[rows[0]] = rows[1]
    for key, value in dict.items():
        if value > 4000:
            list_of_store_name.append(key)
    print(list_of_store_name)


list_of_stores_greater_than_4000(df)


def
