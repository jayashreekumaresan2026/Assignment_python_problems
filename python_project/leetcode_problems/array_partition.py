#https://leetcode.com/problems/array-partition-i/
def array_partition(user_input):
    user_input.sort()
    print(sum(user_input[::2]))

user_input=[1,4,3,2]
array_partition(user_input)