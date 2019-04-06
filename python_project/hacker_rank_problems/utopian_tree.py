#https://www.hackerrank.com/challenges/utopian-tree/problem?h_r=internal-search
def utopian_tree(list_array):
    sum = 0
    index_array = list_array[-1]
    new_array = []
    for i in range(0, index_array + 1):
        if i % 2 == 0:
            sum = sum + 1
            new_array.append(sum)
        elif i % 2 != 0:
            sum = sum + sum
            new_array.append(sum)
    for i in list_array:
        print(new_array[i])


list_array = [0, 1, 4]
utopian_tree(list_array)