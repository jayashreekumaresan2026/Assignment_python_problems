#https://leetcode.com/problems/baseball-game/
def baseball_game(user_score):
    operations = []
    for score in user_score:
        if score == "C":
            operations.pop()
        elif score == 'D':
            operations.append(operations[-1] * 2)
        elif score == '+':
            operations.append(operations[-1] + operations[-2])
        else:
            operations.append(int(score))
    return sum(operations)


user_score = ["5", "-2", "4", "C", "D","9","+","+"]
print(baseball_game(user_score))
