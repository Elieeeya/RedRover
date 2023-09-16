# 4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата,
# и возвращающую 3 значения (с помощью кортежа):
#      периметр квадрата, площадь квадрата и диагональ квадрата.
import math


def square(side):
    perimeter = 4 * side
    area = side ** 2
    diagonal = math.sqrt(2) * side
    print("Perimeter:", perimeter)
    print("Area:", area)
    print("Diagonal:", diagonal)
    return (perimeter, area, diagonal)


square(side=2)