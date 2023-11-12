
def printHeader():
    # def defines a function/ you are able to name your functon anything that you want
    print("CARLIANA ROLAND")
    print("COMP163")
    print("simple calc")
# the function you made has to be typed in order to actually do any work
def DisplayMenu():
    print("A) Add: ")
    print("S) Subtract: ")
    print("M) Multi: ")
    print("D) Div: ")
    print("Q) QUIT: ")
# this def function makes an output of error when an input is not in the selection
# with the return statement, you are able to print this function when it's called
def displayMenuError():
    return "Invalid menu selection"
# declarations

printHeader()
# write a little bit of code and test it- incremental programming



validMenuItems = ("A", "S", "M", "D", "Q")


def calcAdd(num1, num2):
    return num1 + num2


def calcSub(num1, num2):
    return num1 - num2


def calcMult(num1, num2):
    return num1 * num2


def calcDiv(num1, num2):
    return num1 / num2




while True:
    DisplayMenu()
    menuSelect = input("Menu: ").upper()
    if menuSelect not in validMenuItems:
        print(displayMenuError())
    if menuSelect == "Q":
        break



    op1 = float(input("Input here: "))
    op2 = float(input("Input here: "))

    if menuSelect == "A":
        print(("The sum of " + str(op1) + " and " + str(op2) + " is " + str(calcAdd(op1, op2))))
    elif menuSelect == "S":
        print("The difference of " + str(op1) + " and " + str(op2) + " is " + str(calcSub(op1, op2)))
    elif menuSelect == "M":
        print("The product of" + str(op1) + " and " + str(op2) + " is " + str(calcMult(op1, op2)))
    elif menuSelect == "D":
        print("The product of " + str(op1) + " and " + str(op2) + " is " + str(calcDiv(op1, op2)))
    else:
        print("Invalid choice, try again.")

