# 3.4. Напишите программу, которая определяет, какая семья больше.
#       1) Программа имеет два input() - например, family_1, family_2.
#       2) Членов семьи нужно перечислить через запятую.
#      Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')

family_1 = input("Введите членов первой семьи через запятую: ")
family_2 = input("Введите членов второй семьи через запятую: ")

members_1 = family_1.split()
members_2 = family_2.split()

if len(members_1) > len(members_2):
    print("Первая семья больше")
elif len(members_1) < len(members_2):
    print("Вторая семья больше")
else:
    print("Equal")
