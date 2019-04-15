# https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem?h_r=internal-search
def minimum_absolute_difference(user_input):
    result = []
    for i in range(0, len(user_input)):
        for j in range(i + 1, len(user_input)):
            result.append(abs(user_input[i] - user_input[j]))
    minimum_absolute_difference = min(result)
    print(minimum_absolute_difference)


user_input = [1, -3, 71, 68, 17]
minimum_absolute_difference(user_input)
