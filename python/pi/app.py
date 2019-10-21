
def calculate(number):
    formula = "4 * (1/1-"
    count = 1
    term = 1
    operator = ""
    for i in range(number):
        if(i is number):
            pass
        else:
            formula += operator
        count += 2
        if (term is 0):
            operator = "-"
            term = 1
        elif (term is 1):
            operator = "+"
            term = 0
        formula += f"1/{count}"
    formula += ")"
    return eval(formula)

number = int(input("How many numbers should we use to calculate PI?\n"))
print(calculate(number))
