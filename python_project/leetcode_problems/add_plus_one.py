#https://leetcode.com/problems/plus-one/
def plus_one(user_input):
    num = int(''.join(map(str, user_input)))
    num += 1
    return [int(i) for i in str(num)]


user_input = [4, 3, 2, 1]
print(plus_one(user_input))
