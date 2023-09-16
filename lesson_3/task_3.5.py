# 3.5. Создайте словарь film c ключами title, director, year, budget, main_actor, slogan.
# В значения можете передать информацию
#     о вашем любимом фильме.
#     - распечатайте только ключи
#     - распечатайте только значения
#     - распечатайте пары ключ - значение


film = {'title': 'Bleach',
        'director': 'Noriyuki Abe',
        'year': 2004,
        'budget': 120,
        'main_actor': 'Ichigo',
        'slogan': 'Bankai'}

print('\n')
#     - распечатайте только ключи
print(film.keys())
#     - распечатайте только значения
print(film.values())
#     - распечатайте пары ключ - значение
print(film.items())

print('\n')




# Выводим только ключи
print("Ключи словаря:")
for key in film:
    print(key)

# Выводим только значения
print("\nЗначения словаря:")
for value in film.values():
    print(value)

# Выводим пары ключ-значение
print("\nПары ключ-значение:")
for key, value in film.items():
    print(key, ":", value)