# https://leetcode.com/problems/reverse-string/
import math


def reverse_string(user_string):
    for i in range(math.ceil(len(user_string) / 2)):
        flag = user_string[-1 - i]
        user_string[-1 - i] = user_string[i]
        user_string[i] = flag
    print(user_string)

user_string = ["h", "e", "l", "l", "o"]
reverse_string(user_string)
