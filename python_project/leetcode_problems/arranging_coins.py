def arranging_coins(user_input):
    i = 1
    while user_input >= 0:
        user_input -= i
        i += 1
    return i - 2


user_input = 8
print(arranging_coins(user_input))
