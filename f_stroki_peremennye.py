"""Вывод переменных с помощью f строки"""
x = 14
y = 17
print(f"x = {x}, y = {y}")

x = 11
y = 98
print(f"{x=}, {y=}")
#пробелы будут учтены
print(f"{x  =}, {y= }")

"""На вход вашей программе поступают координаты точки x и y - два целых числа, каждое вводится
 на отдельной строчке. 
Ваша задача обязательно сохранить поступающие на вход значения в переменные x и y соответственно,
 и затем вывести строку вида Точка(x = {значение}, y = {значение})"""

x = int(input())
y = int(input())
print('Точка(x = {z}, y = {o})'.format(z = x,o = y))