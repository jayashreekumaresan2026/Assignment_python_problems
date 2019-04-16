# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
# If the last word does not exist, return 0.
def length_of_last_word(user_string):
    if user_string.find(' ') == -1:
        return 0
    else:
        result = len(user_string.split(' ')[-1])
        return result


user_string = "hello world"
print(length_of_last_word(user_string))
