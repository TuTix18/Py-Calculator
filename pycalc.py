# Color settings
class colors:
    GREEN = '\033[92m'
    RED = '\033[91m'

# main program
while True:
    print() # prints a new line
    print("******************")
    print("PyCalculator v1 ")
    print("By: TuTix18")
    print("******************")
    print()
    print("Enter the numbers below")

    x = float(input(colors.GREEN + "First Number "))
    signal = (input(colors.GREEN + "Signal ('+', '-', '*', '**', '/', '%') "))
    y = float(input(colors.GREEN + "Second Number "))

    if signal == '+':
        print(x + y)
    elif signal == '-':
        print(x - y)
    elif signal == '*':
        print (x * y)
    elif signal == '/':
        print (x / y)
    elif signal == '**':
        print(x ** y)
    elif signal == '%':
        print(x % y)
    else:
        print(colors.RED + "Please enter a valid signal")
