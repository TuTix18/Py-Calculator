from os import system

print("******************")
print("PyCalculator v1 ")
print("By: TuTix18")
print("******************")

print("Put the numbers below")
x = float(input("First Number "))
signal = (input(" Signal ('+', '-', '*', '**', '/', '%') "))
y = float(input("Second Number "))

if (signal == '+'):
    print(x + y)
elif (signal == '-'):
    print(x - y)
elif (signal == '*'):
    print (x * y)
elif (signal == '/'):
    print (x / y)
elif (signal == '**'):
    print(x ** y)
elif (signal == '%'):
    print (x % y)
else:
  print("Please enter a valid signal")

system("pause")
