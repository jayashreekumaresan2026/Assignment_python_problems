#https://www.hackerrank.com/challenges/save-the-prisoner/problem?h_r=internal-search
def save_the_prisoner():
    t = int(input())
    for i in range(t):
        number_of_prisoner, number_of_sweets, starting = input().split()
        number_of_prisoner, number_of_sweets, starting = [int(number_of_prisoner), int(number_of_sweets), int(starting)]
        result = (number_of_sweets + starting - 1) % number_of_prisoner
        if result == 0:
            print(number_of_prisoner)
        else:
           result


save_the_prisoner()