"""
Part 1:
Write a Python program to find the addition and subtraction of two numbers.

Ask the user to input two numbers (num1 and num2). Given those two numbers, add them together to find the output. Also, subtract the two numbers to find the output.

Part 2:
Write a Python program to find the multiplication and division of two numbers.

Ask the user to input two numbers (num1 and num2). Given those two numbers, multiply them together to find the output. Also, divide num1/num2 to find the output.

Compile and submit your pseudocode, source code, and screenshots of the application executing the code from parts 1 and 2, the results and GIT repository in a single document (Word is preferred).

"""
def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    if num2 == 0:
        return "NA"
    return num1 / num2


if __name__ == '__main__':
    num1 = int(input("Enter first Number "))
    num2 = int(input("Enter second Number "))

    # Part one
    print("Addition output = ", add(num1, num2))
    print("Substraction output = ", sub(num1, num2))

    # Part Two
    print("Multiplication output = ", mul(num1, num2))
    print("Division output = ", div(num1, num2))

