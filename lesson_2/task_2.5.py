num1 = int(input("Введите первое число: "))
operator = str(input("Введите оператор (+, -, *, /): "))
num2 = int(input("Введите второе число: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
else:
    print("Некорректный оператор")
    exit()

print(f"{num1} {operator} {num2} = {result}")
