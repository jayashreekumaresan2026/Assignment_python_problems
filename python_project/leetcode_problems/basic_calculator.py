def basic_calculator():
    print("1.addition")
    print("2.subtraction")
    print("3.multiplication")
    print("4.division")
    print("5.exit")

    while True:
        choice = int(input("enter your choice to calculate"))
        if choice >= 1 and choice <= 5:
            num1 = int(input("enter your first number"))
            num2 = int(input("enter your second number"))
            if choice == 1:
                addition_result = num1 + num2
                return addition_result
            elif choice == 2:
                subtraction_result = num1 - num2
                return subtraction_result
            elif choice == 3:
                multiplication_result = num1 * num2
                return multiplication_result
            elif choice == 4:
                division_result = num1 * num2
                return division_result
            elif choice == 5:
                print("Thank you")


print(basic_calculator())
