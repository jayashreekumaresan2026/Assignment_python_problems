# https://leetcode.com/problems/reverse-integer/
def reversing_the_number():
    user_input = int(input("enter the number :"))
    if user_input>=0:
        user_input = str(user_input)
        user_input = user_input[::-1]
        print("the reversed number is:",int(user_input))
    if int(user_input)<0:
            negative_value = -1 * user_input
            user_input = str(negative_value)
            result =user_input[::-1]
            value="-"+result
            print(value)
    if int(user_input) > 2147483647:
        print("0")


reversing_the_number()
