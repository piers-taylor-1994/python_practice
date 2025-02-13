import art
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(art.logo)
    keep_going = True
    num1 = float(input("What is your first number?\n"))
    while keep_going:
        for o in operations:
            print(o)
        operator = input("Choose an operator\n")
        num2 = float(input("What is your next number?\n"))
        answer = operations[operator](num1, num2)
        print(f"{num1} {operator} {num2} = {answer}")

        what_next = input("If you would like to continue, press y or press n to stop\n")
        if what_next == "y":
            num1 = answer
        else:
            calculator()
calculator()