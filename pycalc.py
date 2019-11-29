# main program
while True:
    print() # prints a new line
    print("******************")
    print("PyCalculator v1 ")
    print("By: TuTix18")
    print("******************")
    print()
    print("Enter the numbers below")

    x = float(input("First Number "))
    signal = (input("Signal ('+', '-', '*', '**', '/', '%') "))
    y = float(input("Second Number "))

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
        print("Please enter a valid signal")
