
num1 = float(input("Please enter a number "))
num2 = float(input("Please enter a second number "))
operation = input("Please enter an operation (+,-,:,*)")


if operation=='+':
    print(num1+num2)
elif operation=='-':
    print(num1-num2)
elif operation==':':
    print(num1/num2)
elif operation=='*':
    print(num1*num2)
else:
    print('No operation added')
