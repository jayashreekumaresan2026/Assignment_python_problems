#https://leetcode.com/problems/minimum-size-subarray-sum/minimum_size_subarray(user_input, value)
def minimum_size_subarray(user_input, value):
    new_array = []
    for i in range(0, len(user_input)):
        for j in range(i + 1, len(user_input)):
            if user_input[i] + user_input[j] == value:
                new_array.append(user_input[i])
                new_array.append(user_input[j])


user_input = [2, 3, 1, 2, 4, 3]
value = 7
