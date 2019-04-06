#https://www.hackerrank.com/challenges/python-loops/problem
def square_the_number():
    new_list=[]
    user_input=int(input("enter the limit of the number to be square "))
    for i in range(0,user_input):
        new_list.append(i*i)
    print(new_list)
square_the_number()
