#https://leetcode.com/problems/add-digits/
def add_digit():
    user_input = input("enter the number")
    user_input = list(map(int, user_input))
    sum_of_digits = sum(user_input)
    inputs = str(sum_of_digits)
    inputs = list(map(int, inputs))
    if len(inputs) == 1:
        return inputs[0]
    elif len(inputs) >= 2:
        result = sum(inputs)
        inputs = str(result)
        inputs = list(map(int, inputs))
        if len(inputs) == 1:
            return inputs[0]
        elif len(inputs) >= 2:
            result = sum(inputs)
        return result


print(add_digit())
