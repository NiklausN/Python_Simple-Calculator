num1 = float(input("Enter the first number: "))

operation = str(input("Enter the desired operand (i.e +, -, /, *): "))

num2 = float(input("Enter the second number: "))

if operation == "+":

    ans = float(num1 + num2)

elif operation == "-":

    ans = float(num1 - num2)

elif operation == "/":

    ans = float(num1 / num2)

elif operation == "*":

    ans = float(num1 * num2)

print(ans)
