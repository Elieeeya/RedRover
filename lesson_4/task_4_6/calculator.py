from lesson_4.task_4_6 import my_calc

x = int(input("Введите первое число: "))
y = int(input("Введите второе число: "))

result_add = my_calc.add(x, y)
result_subtract = my_calc.subtract(x, y)
result_multiply = my_calc.multiply(x, y)
result_divide = my_calc.divide(x, y)

print("Результат сложения:", result_add)
print("Результат вычитания:", result_subtract)
print("Результат умножения:", result_multiply)
print("Результат деления:", result_divide)
