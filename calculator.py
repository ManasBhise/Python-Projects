# Function to perform operations
def add(n1, n2):
    return n1+n2

def sub(n1, n2):
    return n1-n2

def multiply(n1, n2):
    return n1*n2

def division(n1, n2):
    return n1/n2

# User help message
print("""Welcome to calculator to use it press
      1: Add two numbers
      2: Substract two numbers
      3: Multiply two numbers
      4: Divide two numbers """)

# Input number's and operation
n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number:  "))
opr = input("Enter the desired operation number: ")


# Conditions to perform operation's
if (opr == "1"):
    print(add(n1,n2))
elif (opr == "2"):
    print(sub(n1,n2))
elif (opr == "3"):
    print(multiply(n1,n2))
elif (opr == "4"):
    print(division(n1,n2))
else:
    print("You have entered inncorrect number, run the program again to use the calculator")
    exit

