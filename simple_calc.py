# simple calculator

num1 = float(input("Enter a number: "))
num2 = float(input("Enter a second number: "))
operator = input("Enter the mathematical operator you wish to use (+,-,%,*): ")

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1-num2)
elif operator == "%":
    print(num1/num2)
elif operator == "*":
    print(int(num1*num2))
else:
    print("You have entered an invalid mathematical operator. Please re-run the program and try again.")
