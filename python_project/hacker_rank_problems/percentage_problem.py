def find_percentage():
    new_array = []
    second_array = []
    user_input = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
    dictionary = dict(user_input)
    print(dictionary)
    for key, values in dictionary.items():
        new_array.append(values)
    minimum_value = min(new_array)
    if minimum_value in dictionary.values() :
        del minimum_value
    print(dictionary)
find_percentage()
