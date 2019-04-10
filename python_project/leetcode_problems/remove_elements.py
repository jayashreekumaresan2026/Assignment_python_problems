#https://leetcode.com/problems/remove-element/
def remove_elements(user_input, value_to_remove):
    k = len(user_input) - 1
    for i in range(k, -1, -1):
        if user_input[i] == value_to_remove:
            del user_input[i]
            k = len(user_input) - 1
    return len(user_input)


user_input = [3,2,2,3]
value_to_remove = 3
print(remove_elements(user_input, value_to_remove))
