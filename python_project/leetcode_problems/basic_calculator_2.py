#https://leetcode.com/problems/basic-calculator/
def Infix(expr):
    expr = list(expr)
    stack = list()
    num = ""
    while len(expr) > 0:
        c = expr.pop(0)
        if c in "0123456789.":
            num += c
        else:
            if num != "":
                stack.append(num)
                num = ""
            if c in "+-*/":
                stack.append(c)
            elif c == "(":
                continue
            elif c == ")":
                num2 = stack.pop()
                op = stack.pop()
                num1 = stack.pop()
                if op == "+":
                    stack.append(str(float(num1) + float(num2)))
                elif op == "-":
                    stack.append(str(float(num1) - float(num2)))
                elif op == "*":
                    stack.append(str(float(num1) * float(num2)))
                elif op == "/":
                    stack.append(str(float(num1) / float(num2)))
    return stack.pop()


expr = "(3+(4*5))"
print(expr)
print(Infix(expr))
