#https://leetcode.com/problems/search-insert-position/
def search_insert_position():
    value_to_insert=4
    user_input=[1,2,3,5]
    if value_to_insert in user_input:
        index_of_the_value=user_input.index(value_to_insert)
        print(index_of_the_value)
    else:
        user_input.append(value_to_insert)
        user_input.sort()
        print(user_input.index(value_to_insert))

search_insert_position()
