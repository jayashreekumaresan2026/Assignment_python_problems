# https://leetcode.com/problems/first-unique-character-in-a-string/
def firstuniquecharacter(user_string):
    counter = {}
    result = []
    if user_string == "":
        return -1
    else:
        for char in user_string:
            if char in counter:
                counter[char] += 1
            else:
                counter[char] = 1
                result.append(char)
    for i in result:
        if counter[i] == 1:
            if i in user_string:
                return user_string.index(i)

    return -1


user_string = "leetcode"
print(firstuniquecharacter(user_string))
