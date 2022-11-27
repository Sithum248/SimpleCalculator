

operator = input("Enter an Operator: (+ , - , * , /):\n")
num1 = float(input("Enter the 1st Number: "))
num2 = float(input("Enter the 2nd Number: "))

if operator == "+":
  result = num1 + num2
  print(round(result, 3))
elif operator == "-":
  result = num1 - num2
  print(round(result, 3))
elif operator == "*":
  result = num1 * num2
  print(round(result, 3))
elif operator == "/":
  result = num1 / num2
  print(round(result, 3))
else:
  print(f"{operator}Not a valid Operator!")