#https://leetcode.com/problems/third-maximum-number/
def third_maximum_number(user_input):
    remove_duplicates = list(set(user_input))
    remove_duplicates.sort(reverse=True)
    print(remove_duplicates)
    if len(remove_duplicates) < 3:
        print(remove_duplicates[0])
    else:
        print(remove_duplicates[2])


user_input = [1,2]
third_maximum_number(user_input)
