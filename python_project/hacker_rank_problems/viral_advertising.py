# https://www.hackerrank.com/challenges/strange-advertising/problem?h_r=internal-search
import math

number_of_day = int(input())
user_input = 5
likes = 0

for i in range(number_of_day):
    likes += math.floor(user_input / 2)
    user_input = math.floor(user_input/ 2) * 3

print(likes)