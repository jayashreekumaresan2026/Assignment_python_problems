#https://leetcode.com/problems/median-of-two-sorted-arrays/
def median_of_two_sorted_array(user_input1, user_input2):
    combining_element = sorted(user_input1 + user_input2)
    median_index = len(combining_element) // 2
    if len(combining_element) % 2 is not 0:
        return combining_element[median_index]
    else:
        return (combining_element[median_index - 1] + combining_element[median_index]) / 2.0


user_input1 = [1, 2]
user_input2 = [3, 4]
print(median_of_two_sorted_array(user_input1, user_input2))
