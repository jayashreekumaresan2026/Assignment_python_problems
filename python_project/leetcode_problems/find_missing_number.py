#https://leetcode.com/problems/missing-number/
def find_missing_number(user_input):
    user_input.sort()
    endValue = user_input[-1]
    for i in range(0, endValue + 1):
        if user_input[i] != i:
            return i
    return endValue + 1


user_input = [9, 6, 4, 2, 3, 5, 7, 0, 1]
print(find_missing_number(user_input))
