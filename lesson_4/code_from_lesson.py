# min_item = min(20, 15, 77, 100)
# print(min_item)
#
#
# def person(age, first_name, last_name):
#     return f'Hello, my name is {first_name} {last_name}. I am {age} years old'
#
#
# print(person(25, 'Anna', 'Petrova'))
#
#

# def pattern(length, char1='', char2='*'):
#     return (char1 + char2) * length
#
#
# print(pattern(4, char1='|*|'))


# def decorator_function(func):
#     def wrapper(*args):
#         print('Wrapper function')
#         print(f'Wrapper function: {func.__name__}')
#         print(f'With arguments: {args}')
#         print('Wrapper function in process')
#         print(func(*args))
#         print(f'Exiting wrapper')
#
#     return wrapper
#
#
# @decorator_function
# def hello(item):
#     return f'{item} is wrapped!'
#
#
# hello('ELAY')


# def add_commentary(func):
#   def wrapper(home_team, away_team, score):
#     print(f'{home_team} vs {away_team}: {score}')
#     print(f'Commentary: {func.__doc__}')
#     return func(home_team, away_team, score)
#
#   return wrapper
#
#
# @add_commentary
# def goal(home_team, away_team, score):
#   """A goal has been scored!"""
#   return f'{home_team} {score} - {away_team}'


# result = goal('Real Madrid', 'Barcelona', '2-0')
# print(result)


# x = 15
# y = 25
#
#
# def sum_it(x, y):
#     print(f'locals: {locals()}')
#     return x + y
#
#
# print(sum_it(10, 10))
# print({x + y})
# print(f'Globals: {globals()}')


# name = 'Alice'
#
#
# def outer_function():
#     # name = 'Albert'
#
#     def inner_function():
#         # name = 'Alex'
#         return name
#
#     return inner_function()
#
#
# closure = outer_function()
# result = closure
#
# print(result)


# result = lambda n: n + n
# print(result(5))


list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]


def filter_and_sum(lst):
    new_1 = []
    for x in lst:
        if isinstance(x, int):
            new_1.append(x)
            return sum(new_1)


print(filter_and_sum(list_1))
