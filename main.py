# Все комбинации 3-х букв алфавита
# import string
#
# for i in string.ascii_uppercase:
#     for j in string.ascii_uppercase:
#         for k in string.ascii_uppercase:
#             print(i+j+k)


# Задача 1
# Есть список
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# Выведите все элементы, которые меньше 5.
#
# for i in a:
#     if i>5:
#         print(i)


# # Задача 2
# # Даны списки:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# #
# # Нужно вернуть список, который состоит из элементов, общих для этих двух списков.
#
# # Лямбда - функция — это функция, которая состоит только из одной строки с инструкцией return
# # lambda arguments: expression
# # f = lambda x: x * x
# result = list(filter(lambda elem: elem in b, a))
#
# result1 = [n for n in a if n in b]
#
# # Set в python - "контейнер", содержащий не повторяющиеся элементы в случайном порядке.
# # привести оба списка к множествам и найти их пересечение
# result2 = list(set(a) & set(b))
#
# print(result)
# print(result1)
# print(result2)


# Задача 3
# Отсортируйте словарь по значению в порядке возрастания и убывания.
# import operator
#
# # operator.itemgetter(n) создает вызываемый, который принимает итерируемый объект
# # (например, list, tuple, set) в качестве входных данных и извлекает из него n-й элемент.
#
# d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# res = sorted(d.items(), key=operator.itemgetter(1))
# res1 = sorted(d.items(), key=operator.itemgetter(1), reverse=True)
#
# print(res)
# print(res1)


# Задача 4
# Напишите программу для слияния нескольких словарей в один.
#
#
# dict1 = {1:'anya', 2:'katya', 3:'olya'}
# dict2 = {4:'kolya', 5:'ivan'}

# result1 = {}
# for d in (dict1, dict2):
#     result1.update(d)
#
# # А можно с помощью «звёздочного» синтаксиса:
#
# result2 = {**dict1, **dict2}
# print(result1)
# print(result2)

#
#
# Задача 5
# Найдите три ключа с самыми высокими значениями в словаре
# import operator
# my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
# res= sorted(my_dict.items(), key= operator.itemgetter(1), reverse=True)[:3]
# print(res)


# Задача 6
# Напишите код, который переводит целое число в строку, при том что его можно применить в любой системе счисления.
# number=123
# print(str(number))


# Задача 7
# Нужно вывести первые n строк треугольника Паскаля. В этом треугольнике на вершине и по бокам стоят единицы,
# а каждое число внутри равно сумме двух расположенных над ним чисел.
# def pascal_triangle(n):
#     row = [1]
#     y = [0]
#     for x in range(max(n, 0)):
#         print(row)
#         row = [left + right for left, right in zip(row + y, y + row)]
#
#
# pascal_triangle(6)


# Задача 8
# Напишите проверку на то, является ли строка палиндромом. Палиндром — это слово или фраза, которые одинаково читаются слева направо и справа налево.

# def check(w):
#     return w == ''.join(reversed(w))
#
# print(check('abccba'))
# # Того же эффекта можно добиться с помощью срезов:
# def is_palindrome(string):
#     return string == string[::-1]
# print(is_palindrome('abba'))


# Задача 9
# Сделайте так, чтобы число секунд отображалось в виде дни:часы:минуты:секунды.
# def clock():
#     for i in range(0, 24):
#         for j in range(0, 60):
#             for k in range(0, 60):
#                 print(str(i) + ':' + str(j)+':' + str(k))
#
# clock()


# Вариант решения
# Задача 10
# Вы принимаете от пользователя последовательность чисел, разделённых запятой. Составьте список и кортеж с этими числами.

# values = input('Введите числа через запятую: ')
# ints_as_strings = values.split(',')
# ints = map(int, ints_as_strings)
#
# lst = list(ints)
# tup = tuple(lst)
# print('Список:', lst)
# print('Кортеж:', tup)

# Вариант решения
# Задача 11
# Выведите первый и последний элемент списка.

# list = [1, 4, 7, 23, 65]
# print(list[:1])
# print(list[-1:])



# Задача 12
# Напишите программу, которая принимает имя файла и выводит его расширение. Если расширение у файла определить невозможно, выбросите исключение.




# Задача 13
# При заданном целом числе n посчитайте n + nn + nnn.

# def sum(num):
#     n1=num
#     n2= int(str(num)*2)
#     n3 = int(str(num)*3)
#     print(n1+ n2+ n3)
# sum(5)


# Задача 14
# Напишите программу, которая выводит чётные числа из заданного списка и останавливается, если встречает число 237.
# l=[3, 45, 97, 21, 12, 34,  323, 237, 353, 34]
# def check_even(l):
#
#     for i in l:
#         if i == 237:
#             break
#         if i%2 == 0:
#             print(i)
#
# check_even(l)


# Вариант решения
# Задача 15
# Напишите программу, которая принимает два списка и выводит все элементы первого, которых нет во втором.
# list1=[ 3, 6, 8, 121, 45]
# list2= [4, 8, 32, 3]
#
# print(set(list1)-set(list2))


# Задача 16
# Выведите список файлов в указанной директории.



# Задача 17
# Сложите цифры целого числа.

# l=[4, 22, 12, 28, 45]
# def check_even(l):
#
#     for i in l:
#         s = 0
#         if i%2 == 0:
#             for k in str(i):
#                 # print(k)
#                 s = s + int(k)
#             print(s)
#
# check_even(l)



# Задача 18
# Посчитайте, сколько раз символ встречается в строке.
# list='dkvbdslkvnhv djkwow'


# количество всех символов
# def count_symb1(l):
#     unik= set(l)
#     for i in unik:
#         print(i + ':'+ str(l.count(i)) )

#  # количество  символa
# def count_symb2(l, o):
#     # unik = set(l)
#     print(o + ':' + str(l.count(o)))


# count_symb1(list)
# count_symb2(list, 'd')




# Задача 19
# Поменяйте значения переменных местами.
# a=4
# b=7
#
# # 1
# # a,b=b,a
#
# # 2
# # c=a
# # a=b
# # b=c
#
# print(a)
# print(b)
#

#
# Задача 20
# С помощью анонимной функции извлеките из списка числа, делимые на 15.

# list_num=[23, 15, 76, 30, 60, 32]
# fun=list(filter(lambda x: not x % 15, list_num ))
# print(fun)


# Задача 21
# Нужно проверить, все ли числа в последовательности уникальны.
# nums = [45, 55, 60, 37, 100, 105, 220, 220]
# def unique(numbers):
#     return len(numbers) == len(set(numbers))
#
# print(unique(nums))

# Вариант решения
# Задача 22
# Напишите программу, которая принимает текст и выводит два слова: наиболее часто встречающееся и самое длинное.

# import collections
#
# text = 'lorem ipsum dolor sit amet amet amet'
# words = text.split()
#
# counter = collections.Counter(words)
#
# most_common, occurrences = counter.most_common()[0]
#
# longest = max(words, key=len)
#
# print(most_common)
# print(longest)