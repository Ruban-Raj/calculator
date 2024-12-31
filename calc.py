from art import  logo
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return  n1 - n2

def multiply(n1, n2):
    return  n1 * n2

def divide(n1, n2):
    return  n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

print(logo)

first_num = float(input("What's the first number?: "))

should_accumulate = True

while should_accumulate:
    opp = input("+ \n- \n* \n/\nPick an operation: ")
    second_num = float(input("What's the second number?: "))
    if opp == "+":
        result = (operations["+"](first_num, second_num))
    elif opp == "-":
         result =operations["-"](first_num, second_num)
    elif opp == "*":
         result = operations["*"](first_num, second_num)
    elif opp == "/":
        result = operations["/"](first_num, second_num)
    print(f"The result is {first_num} {opp} {second_num} = {result}")

    continue_math = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation?: or type 'q' to quite?: ").lower()
    if continue_math == "y":
        first_num = result
    elif continue_math == "n":
        print("\n"*100)
        first_num = float(input("What's the first number?: "))
    else:
        break
