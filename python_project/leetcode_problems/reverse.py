# https://leetcode.com/problems/reverse-integer/
def reverse(x):
    if x >= 0:
        y = str(x)
        reverse_value = y[::-1]
    if x < 0:
        y=x*-1
        y=str(y)
        reverse_value=y[::-1]
    if int(reverse_value)>2147483647:
        return 0
    elif x>=0:
        return int(reverse_value)
    elif x<0:
        reverse_value=int(reverse_value)*-1
        return reverse_value



x = -1536739849013
print(reverse(x))



    # if x < 0:
    #     negative_value = -1 * x
    #     x = str(negative_value)
    #     result = x[::-1]
    #     value = "-" + result
    #     if int(x)<-2147483647:
    #         return 0
    #     return int(value)



