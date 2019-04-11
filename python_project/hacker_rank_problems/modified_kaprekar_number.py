#https://www.hackerrank.com/challenges/kaprekar-numbers/problem?h_r=internal-search
def modified_kaprekar_number(lower_limit, upper_limit):
    new_list = []
    for i in range(lower_limit, upper_limit + 1):
        square_of_the_number = str(i * i)
        finding_the_length = len(square_of_the_number) // 2
        if int(square_of_the_number) == 1:
            new_list.append(i)
        if len(square_of_the_number) == 1:
            continue
        if len(square_of_the_number) > 1:
            result = int(square_of_the_number[:finding_the_length]) + int(square_of_the_number[finding_the_length:])
            if result == i:
                new_list.append(i)
    if len(new_list) == 0:
        print("Invalid range")
    else:
        for i in new_list:
            print(i, end=" ")


lower_limit = 1
upper_limit = 99999
modified_kaprekar_number(lower_limit, upper_limit)
