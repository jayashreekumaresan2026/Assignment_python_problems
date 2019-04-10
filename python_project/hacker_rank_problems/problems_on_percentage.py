# https://www.hackerrank.com/challenges/finding-the-percentage/problem?h_r=internal-search
def problems_on_percetage():
    number_of_person = int(input("enter the number of student:"))
    student_dictionary = {}
    for i in range(number_of_person):
        student_details = input().split()
        name_of_the_student, marks = student_details[0], student_details[1:]
        marks = list(map(float, marks))
        student_dictionary[name_of_the_student] = marks
    print(student_dictionary)
    user_query = input()
    for name, mark in student_dictionary.items():
        if user_query == name:
            print("{0:.2f}".format((sum(mark) / len(mark))))


problems_on_percetage()
