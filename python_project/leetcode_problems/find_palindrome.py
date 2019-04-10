#https://leetcode.com/problems/palindrome-number/
def find_palindrome():
    user_input = int(input("enter the number to check  palindrome are not:"))
    user_input = str(user_input)
    reversed_input = "".join(reversed(user_input))
    if user_input == reversed_input:
        return True
    return False


print(find_palindrome())
