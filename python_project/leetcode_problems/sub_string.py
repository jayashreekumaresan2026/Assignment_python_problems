#https://leetcode.com/problems/implement-strstr/
def find_sub_string(user_input, query):
    if query in user_input:
        print(user_input.index(query))
    else:
        print("-1")


user_input = "hello"
query = "ll"
user_input1 = "aaaaa"
query1 = "bba"
find_sub_string(user_input, query)
find_sub_string(user_input1, query1)
