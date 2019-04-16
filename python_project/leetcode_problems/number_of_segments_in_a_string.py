# https://leetcode.com/problems/number-of-segments-in-a-string/
def find_number_of_segment(user_string):
    count = 0
    for i in user_string.split():
            count = count + 1
    print(count)


user_string = "hai hello "
find_number_of_segment(user_string)
