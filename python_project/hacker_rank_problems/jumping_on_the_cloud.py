#https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_r=internal-search
def jumping_on_the_cloud(user_input):
    i = 0
    jumps = 0
    while i < len(user_input) - 1:
        if i < len(user_input) and user_input[i] != 1:
            i += 1
        jumps += 1
        i += 1
    return jumps


user_input = [0, 1, 1, 0, 1, 0]
print(jumping_on_the_cloud(user_input))