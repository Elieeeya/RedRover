# 4.2. Напишите фукнцию, которая принимает произвольное количество
# именнованных аргументов и выводит их построчно
#      в формате аргумент: значение. Например:
# 	name: John
# 	last_name: Smith
# 	age: 35
# 	position: web developer

def print_arguments(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} : {value}')

