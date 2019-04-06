#https://www.hackerrank.com/challenges/sherlock-and-squares/problem?h_r=internal-search
from math import *


def sherlock_and_squares(a, b):
    count = 0
    for i in range(a, b + 1):
        square_root_of_number = sqrt(i)
        if square_root_of_number == ceil(square_root_of_number):
            count = count + 1
    print(count)


sherlock_and_squares(3, 9)
