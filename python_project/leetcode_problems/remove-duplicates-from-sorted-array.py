#https://leetcode.com/problems/remove-duplicates-from-sorted-array/
import collections
def removing_duplicates_elements(user_input):
    list_data=[]
    result = collections.Counter(user_input)
    for key,value in result.items():
        list_data.append(key)
    return list_data

user_input = [1,1,2]
print(removing_duplicates_elements(user_input))
