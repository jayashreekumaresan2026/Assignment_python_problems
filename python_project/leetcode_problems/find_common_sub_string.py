def common_sub_string():
    user_input = ["flower", "flow", "flight"]
    prefix = ""
    if len(user_input) == 0:
        return prefix

    for i in range(len(user_input)):
        c = user_input[0][i]
        if all(a[i] == c for a in user_input):
            prefix += c
        else:
            break
    return prefix


print(common_sub_string())
