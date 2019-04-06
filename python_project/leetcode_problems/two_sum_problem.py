# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# Given nums = [2, 7, 11, 15], target = 9
def two_sum(list_element, target):
    new_array = []
    for i in range(0, len(list_element)):
        for j in range(i + 1, len(list_element)):
            if list_element[i] + list_element[j] == target:
                new_array.append(i)
                new_array.append(j)
    print(new_array)


list_element = [2, 7, 11, 15]
target = 9
two_sum(list_element, target)
