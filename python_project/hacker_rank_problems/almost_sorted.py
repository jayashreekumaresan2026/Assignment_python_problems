# https://www.hackerrank.com/challenges/almost-sorted/problem
def almost_sorted():
    new_list = []
    check_list = []
    user_input = int(input("enter the total number of items in list "))
    for i in range(0, user_input):
        user_list = int(input("enter your list items "))
        new_list.append(user_list)
    sorted_new_list = sorted(new_list)
    for i in range(len(new_list)):
        if new_list[i] != sorted_new_list[i]:
            check_list.append(new_list[i])
    if len(check_list) == 0:
        print("Yes")
    else:
        if len(check_list) == 2:
            print("yes")
            temp = check_list[0]
            check_list[0] = check_list[1]
            check_list[1] = temp
            print("swap {} {}".format(check_list.index(check_list[0]), check_list.index(check_list[1])))
        elif len(check_list) > 2:
            temp = check_list[0]
            check_list[0] = check_list[1]
            check_list[1] = temp
            if check_list==sorted_new_list:
               print("yes")
            else:
                print(check_list)
                check_list = check_list[::-1]
                print(check_list)

                if check_list == sorted(check_list):
                    print("yes")
        else:
            print("no")



almost_sorted()
