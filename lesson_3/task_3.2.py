# 3.2 Дан список list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
#    - получите сумму всех чисел,
#    - распечатайте все строки, где есть буква 'a'


list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]

x = list_1[2] + list_1[4] + list_1[-1] + list_1[-2]
print(x)

sum_of_numbers = 0
for element in list_1:
    if isinstance(element, int):
        sum_of_numbers += element
        print(sum_of_numbers)
