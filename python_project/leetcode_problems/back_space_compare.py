#https://leetcode.com/problems/backspace-string-compare/
def back_space_compare(user_string1, user_string2):
    new_list = []
    string = ""
    user_string1 = list(user_string1)
    user_string2 = list(user_string2)
    for str1 in range(0, len(user_string1)):
        for str2 in range(0, len(user_string2)):
            if user_string1[str1] == user_string2[str2] and str1 == str2 and user_string1[str1] != '#':
                new_list.append(user_string2[str1])

    result = string.join(new_list)
    print('"' + result + '"')


user_string1 = "ab#c"
user_string2 = "ad#c"
back_space_compare(user_string1, user_string2)
