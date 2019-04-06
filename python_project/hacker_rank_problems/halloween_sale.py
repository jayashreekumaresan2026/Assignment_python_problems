# https://www.hackerrank.com/challenges/halloween-sale/problem?h_r=internal-search
def halloween_sale(staring_point, difference, ending_point, dollor):
    new_array=[staring_point]
    count=0
    while staring_point > ending_point+difference:
        staring_point = staring_point - difference
        new_array.append(staring_point)
        count=count+1
    sum_value=sum(new_array)
    while sum_value+ending_point<=dollor:
        count=count+1
        sum_value+=ending_point
    print(count)




staring_point = 100
difference = 12
ending_point = 15
dollor = 95
halloween_sale(staring_point, difference, ending_point, dollor)
