 # Списки, словари, кортежи, множества

# # Задача 1.1
# # Условие
# # 1. Создать произвольный список
# list=[1, 45, 67, 'df', 56, True]
# # 2. Добавить новый элемент типа str в конец списка
# list.append('ghjk')
# print(list)
# # 3. Добавить новый элемент типа int на место с индексом
# list[2]=12
# print(list)
# # 4. Добавить новый элемент типа list в конец списка
# list1=[12, 53, 43, 'cdc']
# list=list+list1
# print(list)
# # 5. Добавить новый элемент типа tuple на место с индексом
# list[8]=(123)
# print(list)
# # 6. Получить элемент по индексу
# print(list[7])
# # 7. Удалить элемент
# list.remove(12)
# print(list)
# # 8. Найти число повторений элемента списка
# print(list.count(1))
#
#
# Задача 1.2
# Условие
# list=[23, 65, 87, 12, 56, 97, 34, 65]
# # Получите первый и последний элемент списка
# print(list[0])
# print(list[-1])
# # Задача 1.3
# # Условие
# # Поменяйте значения переменных a и b местами
#
# a=4
# b=7
# print(a, b)
# temp=a
# a=b
# b=temp
# print(a, b)
# a,b=b,a
# print(a, b)

# # Задача 1.4
# # Условие
# list=[23, 65, 87, 12, 56, 97, 34, 65]
# # Проверить, есть ли в последовательности дубликаты
# n_list=set(list)
# print(len(n_list)==len(list))

# # Задача 1.5
# # Условие
# # 1. Создать произвольный словарь
# dict={1:'anna', 2:'inna', 3:'oleg'}
# # 2. Добавить новый элемент с ключом типа str и значением типа int
# dict[6]='ivan'
# print(dict)
# # 3. Добавить новый элемент с ключом типа кортеж(tuple) и значением типа список(list)
# dict[('it', 'is', 'tuple')] = [11, 22, 'list_value', 33, {1, 2, 3}]
# print(dict)
# # 4. Получить элемент по ключу
# print(dict[2])
# # 5. Удалить элемент по ключу
# dict.pop(2)
# print(dict)
# # 6. Получить список ключей словаря
# print(dict.keys())
#
# # Задача 1.6
# # Условие
# # 1. Создать множество(set)
# set={1, 'dfsf', 'vs', 3}
#
# # 2. Создать неизменяемое множество(frozenset)
# fr_set=frozenset({2, '423', 43, 3})
# # 3. Выполнить операцию объединения созданных множеств
# union=set|fr_set
# print(union)
# # 4. Выполнить операцию пересечения созданных множеств
# cros=set&fr_set
# print(cros)
#




# 2. Функции, условия и циклы
#
#
# Задача 2.1
# Условие
# Создать функцию calc(a, b, operation). Описание входных параметров:
# 1. Первое число
# 2. Второе число
# 3. Действие над ними:
#    1) + Сложить
#    2) - Вычесть
#    3) * Умножить
#    4) / Разделить
#    5) В остальных случаях функция должна возвращать "Операция не поддерживается"
# def calk_fun(a,b, operator):
#     if operator=='+':
#         return a+b
#     if operator=='-':
#         return a-b
#     if operator=='*':
#         return a*b
#     if operator=='/':
#         return a/b
#     else:
#         return "Операция не поддерживается"
# print(calk_fun(2,1,'+'))


# Задача 2.2
# Условие
# Напишите программу, которая будет выводить нечетные числа из списка и остановится, если встретит число 139
#
# list=[21, 54, 87, 45, 66, 40, 139, 65, 12]
# def fun(list):
#     main_list=[]
#     for i in list:
#         if i==139:
#             break
#         if i%2==0:
#             main_list.append(i)
#     print(main_list)
# fun(list)



# Задача 2.3
# Условие
# Создайте список [ 18, 14, 10, 6, 2 ]  с помощью функции range()
# list=[]
# for i in range(18, 0, -4 ):
#     list.append(i)
#
# print(list)

# Задача 2.4
# Условие
# Дан список
# lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
# Необходимо вывести элементы, которые одновременно 1) меньше 30 и 2) делятся на 3 без остатка.
# Все остальные элементы списка необходимо просуммировать и вывести конечный результат.
#

# def sum_fun(lst):
#     sum = 0
#     for i in lst:
#         if i<30 and i%3==0:
#             print(i)
#         else:
#             sum=sum+i
#     print(sum)
# sum_fun(lst)
#
# Задача 2.5
# Условие
# Написать функцию month_to_season(), которая принимает 1 аргумент - номер месяца - и возвращает название сезона,
# к которому относится этот месяц.
# Например, передаем 2, на выходе получаем 'Зима'.

# def month_to_season(month):
#
#     if month == 12 or month == 1 or month == 2:
#         return 'winter'
#     if month == 3 or month == 4 or month == 5:
#         return 'spring'
#     if month == 6 or month == 7 or month == 8:
#         return 'summer'
#     if month == 9 or month == 10 or month == 11:
#         return 'autumn'
#     else:
#         print("Wrong number")
#
# print(month_to_season(7))



#
# 3. Работа со строками
#
# # Задача 3.1
# # Условие
# # Дана следующая строка: ‘Сидел барсук в своей норе и ел картошечку пюре’
# #
# # 1. Создайте данную строку
# str='Сидел барсук в своей норе и ел картошечку пюре'
# # 2. Получите ее длину
# print(len(str))
# # 3. Проведите операцию сложения со строкой ‘.’
# str=str+'.'
# print(str)
# # 4. Проверьте, входит ли подстрока ‘ре’ в заданную строку
# print('ре' in str)
# # 5. Посчитайте количество вхождений подстроки ‘ре’
# print(str.count('ре'))
# # 6. Получите предпоследний символ строки
# print(str[-2])
# # 7. Получите все символы с нечетными индексами
# print(str[1::2])
# # 8. Определите, сколько слов в строке
# count=str.split()
# print(len(count))

#
# Задача 3.2
# Условие
# # Дана строка: ‘пишите код так, как будто сопровождать его будет склонный к насилию психопат, который знает, где вы живете.’
# str='пишите код так, как будто сопровождать его будет склонный к насилию психопат, который знает, где вы живете.'
# # 1. Начните строку с заглавной буквы, если она находится в нижнем регистре.
# str=str.capitalize()
# print(str)
# # 2. Найдите индекс вхождения подстроки ‘сопровождать’.
# print(str.index('сопровождать'))
# # 3. Замените вхождение подстроки ‘сопровождать’ на ‘поддерживать’.
# str= str.replace('сопровождать', 'поддерживать')
# print(str)
# # 4. Разбейте предложение на части по запятым. Соедините части обратно, снова добавив запятые между частями.
# new_str=str.split(',')
# print(new_str)
# new_new_str=','.join(new_str)
# print(new_new_str)


# Задача 3.3
# Условие
# Дано имя файла. Необходимо вывести его расширение.
# def name_file(name):
#     part= name.split('.')
#     print(part[-1:])
#
# name_file('buho.py')



# Задача 3.4
# Условие
# Сложите цифры целого числа.

# n=236
#
# def sum_num(num):
#     sum=0
#     if num%2==0:
#         for i in str(num):
#             sum=sum+int(i)
#     print(sum)
# sum_num(n)


# Задача 3.5
# Условие
# Замените заданное количество вхождений подстроки.???????
#
# STR = '01101011101011'
#
# # Тесты
# if __name__ == '__main__':
#     # Заменяем 1 ноль на единицу
#     print(STR.replace('1', '0', 1))
#     # Заменяем 5 нулей на единицы
#     print(STR.replace('1', '0', 5))
#     # Заменяем все нули на единицы(значение по-умолчанию)
#     print(STR.replace('1', '0'))
#     # Заменяем 9 нулей на единицы(все присутствующие единицы)
#     print(STR.replace('1', '0', 9))
#     # Заменяем 10 нулей на единицы(количество единиц больше, чем есть в строке)
#     print(STR.replace('1', '0', 10))


# Задача 3.6
# Условие
# Выяснить, является ли строка палиндромом.
# w='abcdba'
#
# print(w==''.join(reversed(w)))

# Задача 3.7
# Условие
# Дана строка из двух слов. Поменяйте слова местами.
# str='hello world'
#
# new_str=' '.join(reversed(str.split()))
# print(new_str)

# ////////////////////////////////////////////////////
# 4. Модули и пакеты
#
# Задание 4.1
# Условие
# Изучите содержимое и импортируйте модуль this.py

# Задание 4.2
# Условие
# 1. Найдите пакет http(относится к Стандартной библиотеке), изучите модули, из которых он состоит.
# 2. Импортируйте модуль client из пакета http
# 3. Воспользуйтесь функционалом импортированного модуля:
#     1. Создайте HTTP соединение по адресу www.google.com
#     2. Отправьте GET запрос по адресу выше
#     3. Проверьте ответ на отправленный запрос
# import http
# from http import client
# help('http')
# if __name__ == '__main__':
#     # 3.1. Создаем соединение по адресу 'www.google.com'
#     # Для этого обращаемся к модулю client
#     # И вызываем конструктор класса HTTPConnection()
#     connection = client.HTTPConnection('www.google.com')
#     # 3.2. Отправляем GET запрос к корневой странице веб-сервера
#     connection.request('GET', '/')
#     # 3.3. Получаем ответ на наш запрос
#     res = connection.getresponse()
#     # Из полного ответа достаем интересующую нас веб-страницу(ее HTML код)
#     page = res.read()
#     print(page)
#
# Задание 4.3
# Условие
# Выполните следующие действия:
# 1. Изучите сайт репозитория пакетов PyPI (https://pypi.org/)
# 2. Запустите менеджер пакетов pip, изучите уже установленные модули.
# 3. Создайте виртуальное окружение через консоль.
# 4. Активируйте созданное окружение, установите любой из пакетов(например, requests), деактивируйте окружение.
# 5. Создайте виртуальное окружение через PyCharm.
# 6. Активируйте созданное окружение, установите пакет wget.
# 7. Воспользуйтесь функционалом пакета wget:
#     1) Импортируйте данный пакет
#     2) Скачайте с его помощью файл
#
#
# Задание 4.4
# Условие
# Стандартная библиотека. Модуль calendar.
#
# Выполните следующие действия:
#    1. Изучите справку для модуля calendar
#    2. Импортируйте модуль calendar
#    3. Найдите расположение файла модуля calendar и изучите его содержимое
#    4. Получите список доступных атрибутов модуля calendar
#    5. С помощью модуля calendar узнайте, является ли 2027 год високосным
#    6. С помощью модуля calendar узнайте, каким днем недели был день 25 июня 1995 года
#    7. Выведите в консоль календарь на 2023 год
#
#
# Задание 4.5
# Условие
# Задание 2
# Репозиторий PyPI. Пакет FuzzyWuzzy.
#
# Пакет FuzzyWuzzy - это библиотека для нечеткого сравнения строк. Нечеткое сравнение строк позволяет не просто сказать - одинаковые строки или нет, а определить степень их похожести. В текущем задании предлагаем вам поработать с данной библиотекой:
#
# 1. Изучите документацию для пакета fuzzywuzzy на https://pypi.org/
# 2. Установите его с помощью менеджера пакетов pip
# 3. Определите, какие модули включает пакет fuzzywuzzy
# 4. Изучите модуль для базового сравнения строк fuzz(входит в пакет), получите список доступных атрибутов.
# 5. Изучите синтаксис метода для базового нечеткого сравнения строк ratio() (входит в состав модуля fuzz).
# Прим.: Данный метод возвращает индекс схожести 2 срок
# 6. Воспользуйтесь методом ratio() для сравнения следующих срок:
#    1) 'Плохой код на самом деле не плохой.' и 'Его просто не так поняли.'
#    2) 'Работает? Не трогай.' и 'Работает? Не трогай.'
#    3) 'Работает? Не трогай.' и 'Работает? Не трогай!

# ////////////////////////////////////////////////////


#
# 6. ООП. Классы и объекты.
#
# Задание 6.1. Алфавит
# Описание классовой структуры
# Есть Алфавит, характеристиками которого являются:
# 1. Язык
# 2. Список букв
#
# Для Алфавита можно:
# 1. Напечатать все буквы алфавита
# 2. Посчитать количество букв
#
# Так же есть Английский алфавит, который обладает следующими свойствами:
# 1. Язык
# 2. Список букв
# 3. Количество букв
#
# Для Английского алфавита можно:
# 1. Посчитать количество букв
# 2. Определить, относится ли буква к английскому алфавиту
# 3. Получить пример текста на английском языке
# Задание
# Класс Alphabet
# 1. Создайте класс Alphabet
# 2. Создайте метод __init__(), внутри которого будут определены два динамических свойства: 1) lang - язык и 2) letters - список букв. Начальные значения свойств берутся из входных параметров метода.
# 3. Создайте метод print(), который выведет в консоль буквы алфавита
# 4. Создайте метод letters_num(), который вернет количество букв в алфавите
#
# Класс EngAlphabet
# 1. Создайте класс EngAlphabet путем наследования от класса Alphabet
# 2. Создайте метод __init__(), внутри которого будет вызываться родительский метод __init__().
# В качестве параметров ему будут передаваться обозначение языка(например, 'En') и строка, состоящая из всех букв алфавита
 # (можно воспользоваться свойством ascii_uppercase из модуля string).
# 3. Добавьте приватное статическое свойство __letters_num, которое будет хранить количество букв в алфавите.
# 4. Создайте метод is_en_letter(), который будет принимать букву в качестве параметра и определять, относится ли эта
 # буква к английскому алфавиту.
# 5. Переопределите метод letters_num() - пусть в текущем классе классе он будет возвращать значение свойства __letters_num.
# 6. Создайте статический метод example(), который будет возвращать пример текста на английском языке.

# Тесты:
# 1. Создайте объект класса EngAlphabet
# 2. Напечатайте буквы алфавита для этого объекта
# 3. Выведите количество букв в алфавите
# 4. Проверьте, относится ли буква F к английскому алфавиту
# 5. Проверьте, относится ли буква Щ к английскому алфавиту
# 6. Выведите пример текста на английском языке
#
import string
#
# # Алфавит
# class Alphabet:
#
#     def __init__(self, language, letters_str):
#         self.lang = language
#         self.letters = list(letters_str)
#
#     # Печатаем все буквы алфавита
#     def print(self):
#         print(self.letters)
#
#     # Возвращаем количество букв в алфавите
#     def letters_num(self):
#         len(self.letters)
#
#
# # Английский алфавит
# class EngAlphabet(Alphabet):
#
#     __letters_num = 26
#
#     def __init__(self):
#         super().__init__('En', string.ascii_uppercase)
#
#     # Проверяем, относится ли буква к английскому алфавиту
#     def is_en_letter(self, letter):
#         if letter.upper() in self.letters:
#             return True
#         return False
#
#     # Возвращаем количество букв в алфавите
#     def letters_num(self):
#         return EngAlphabet.__letters_num
#
#     # Печатаем пример текста на английском языке
#     @staticmethod
#     def example():
#         print("English Example:\nDon't judge a book by it's cover.")
#
#
# # Тесты
# if __name__ == '__main__':
#     eng_alphabet = EngAlphabet()
#     eng_alphabet.print()
#     print(eng_alphabet.letters_num())
#     print(eng_alphabet.is_en_letter('F'))
#     print(eng_alphabet.is_en_letter('Щ'))
#     EngAlphabet.example()
#
# Задание 6.2. Садовник и помидоры
# Описание классовой структуры
# Есть Помидор со следующими характеристиками:
# 1. Индекс
# 2. Стадия зрелости(стадии: Отсутствует, Цветение, Зеленый, Красный)
#
# Помидор может:
# 1. Расти (переходить на следующую стадию созревания)
# 2. Предоставлять информацию о своей зрелости
#
# Есть Куст с помидорами, который:
# 1. Содержит список томатов, которые на ней растут
#
# И может:
# 1. Расти вместе с томатами
# 2. Предоставлять информацию о зрелости всех томатов
# 3. Предоставлять урожай
#
# И также есть Садовник, который имеет:
# 1. Имя
# 2. Растение, за которым он ухаживает
#
# И может:
# 1. Ухаживать за растением
# 2. Собирать с него урожай
#
#
# Задание
# Класс Tomato:
# 1. Создайте класс Tomato
# 2. Создайте статическое свойство states, которое будет содержать все стадии созревания помидора
# 3. Создайте метод __init__(), внутри которого будут определены два динамических protected свойства: 1) _index - передается параметром
 # и 2) _state - принимает первое значение из словаря states
# 4. Создайте метод grow(), который будет переводить томат на следующую стадию созревания
# 5. Создайте метод is_ripe(), который будет проверять, что томат созрел (достиг последней стадии созревания)
#
# class Tomato:
#     states={1:'Отсутствует', 2: 'Цветение',3: 'Зеленый',4: 'Красный'}
#
#     def __init__(self, index):
#         self.index= index
#         self.state = 1
#     def grow(self):
#         if self.state<=3:
#             self.state+=1
#             print(f'Tomato {self.index} is {self.states[self.state]}')
#     def is_ripe(self):
#         if self.state==4:
#             print(f'Tomato {self.index} is mature')
#
#     def __repr__(self):
#         return f'{self.index}, {self.state}'
#
#
# # Класс TomatoBush
# # 1. Создайте класс TomatoBush
# # 2. Определите метод __init__(), который будет принимать в качестве параметра количество томатов и на его основе будет создавать список объектов класса
#  # Tomato. Данный список будет храниться внутри динамического свойства tomatoes.
# # 3. Создайте метод grow_all(), который будет переводить все объекты из списка томатов на следующий этап созревания
# # 4. Создайте метод all_are_ripe(), который будет возвращать True, если все томаты из списка стали спелыми
# # 5. Создайте метод give_away_all(), который будет чистить список томатов после сбора урожая
# #
# class TomatoBush:
#     def __init__(self, num):
#         self.tomatoes = [Tomato(index) for index in range(0, num - 1)]
#     def grow_all(self):
#         for tomato in self.tomatoes:
#             tomato.grow()
#     def all_are_ripe(self):
#         return all([tomato.is_ripe() for tomato in self.tomatoes])
#     def give_away_all(self):
#         self.tomatoes=[]
#
#
# # Класс Gardener
# # 1. Создайте класс Gardener
# # 2. Создайте метод __init__(), внутри которого будут определены два динамических свойства: 1) name - передается параметром, является публичным
#  # и 2) _plant - принимает объект класса Tomato, является protected
# # 3. Создайте метод work(), который заставляет садовника работать, что позволяет растению становиться более зрелым
# # 4. Создайте метод harvest(), который проверяет, все ли плоды созрели. Если все - садовник собирает урожай. Если нет - метод печатает предупреждение.
# # 5. Создайте статический метод knowledge_base(), который выведет в консоль справку по садоводству.
# #
# class Gardener:
#     def __init__(self, name, plant):
#         self.name=name
#         self._plant=plant
#     def work(self):
#         print('Gardener is working...')
#         self._plant.grow_all()
#         print('Gardener finished')
#     def harvest(self):
#         print('Gardener is harvesting...')
#         if self._plant.all_are_ripe():
#             self._plant.give_away_all()
#             print('Harvesting is finished')
#         else:
#             print('Too early! Your plant is green and not ripe.')
#     @staticmethod
#     def knowledge_base():
#         print('''Harvest time for tomatoes should ideally occur
#         when the fruit is a mature green and
#         then allowed to ripen off the vine.
#         This prevents splitting or bruising
#         and allows for a measure of control over the ripening process.''')




# Тесты:
# 1. Вызовите справку по садоводству
# 2. Создайте объекты классов TomatoBush и Gardener
# 3. Используя объект класса Gardener, поухаживайте за кустом с помидорами
# 4. Попробуйте собрать урожай
# 5. Если томаты еще не дозрели, продолжайте ухаживать за ними
# 6. Соберите урожай
#
# if __name__ == '__main__':
#     Gardener.knowledge_base()
#     great_tomato_bush=TomatoBush(3)
#     gardener_ivan=Gardener('Ivan', great_tomato_bush)
#     gardener_ivan.work()
#     gardener_ivan.harvest()
#     gardener_ivan.work()
#     gardener_ivan.harvest()
#     gardener_ivan.work()
#     gardener_ivan.harvest()

#
# Задание 6.3. Покупка дома
# Описание классовой структуры
# Есть Человек, характеристиками которого являются:
# 1. Имя
# 2. Возраст
# 3. Наличие денег
# 4. Наличие собственного жилья
#
# Человек может:
# 1. Предоставить информацию о себе
# 2. Заработать деньги
# 3. Купить дом
#
# Также же есть Дом, к свойствам которого относятся:
# 1. Площадь
# 2. Стоимость
#
# Для Дома можно:
# 1. Применить скидку на покупку
#
# Также есть Небольшой Типовой Дом, обязательной площадью 40м2.
# Задание
# Класс Human
#
# 1. Создайте класс Human.
# 2. Определите для него два статических поля: default_name и default_age.
# 3. Создайте метод __init__(), который помимо self принимает еще два параметра: name и age. Для этих параметров задайте значения
 # по умолчанию, используя свойства default_name и default_age. В методе __init__() определите четыре свойства: Публичные - name и age. Приватные - money и house.
# 4. Реализуйте справочный метод info(), который будет выводить поля name, age, house и money.
# 5. Реализуйте справочный статический метод default_info(), который будет выводить статические поля default_name и default_age.
# 6. Реализуйте приватный метод make_deal(), который будет отвечать за техническую реализацию покупки дома: уменьшать количество
 # денег на счету и присваивать ссылку на только что купленный дом. В качестве аргументов данный метод принимает объект дома и его цену.
# 7. Реализуйте метод earn_money(), увеличивающий значение свойства money.
# 8. Реализуйте метод buy_house(), который будет проверять, что у человека достаточно денег для покупки, и совершать сделку.
 # Если денег слишком мало - нужно вывести предупреждение в консоль. Параметры метода: ссылка на дом и размер скидки
#
# class Human:
#     default_name= 'No name'
#     default_age=0
#     def __init__(self, name=default_name, age=default_age):
#         self.name= name
#         self.age= age
#         self.__money=0
#         self.__house=None
#     def info(self):
#         print(f"{self.name} is {self.age} years. His have {self.__money} and  {self.__house}")
#     @staticmethod
#     def default_info():
#         print(Human.default_name)
#         print(Human.default_age)
#     def earn_money(self, salary):
#         self.__money+=salary
#     def buy_house(self, house, discont):
#         price=house.final_price(discont)
#         if self.__money>=price:
#             self.make_deal(house, price)
#         else:
#             print('Not enough money!')
#
#     def make_deal(self, house, price):
#         self.__money=self.__money-price
#         self.__house=house
#
# Класс House
#
# 1. Создайте класс House
# 2. Создайте метод __init__() и определите внутри него два динамических свойства: _area и _price. 3. Свои начальные значения
 # они получают из параметров метода __init__()
# 4. Создайте метод final_price(), который принимает в качестве параметра размер скидки и возвращает цену с учетом данной скидки.

# class House:
#     def __init__(self, area, price):
#         self._area=area
#         self._price=price
#     def final_price(self, discont):
#         self._price=self._price*(100-discont)/100
#         return self._price

#
# # Класс SmallHouse
# #
# # 1. Создайте класс SmallHouse, унаследовав его функционал от класса House
# # 2. Внутри класса SmallHouse переопределите метод __init__() так, чтобы он создавал объект с площадью 40м2
# #
# class SmallHouse(House):
#     default_area=40
#     def __init__(self, price):
#         super().__init__(SmallHouse.default_area, price)
# # Тесты
# #
# # 1. Вызовите справочный метод  default_info() для класса Human()
# # 2. Создайте объект класса Human
# # 3. Выведите справочную информацию о созданном объекте (вызовите метод info()).
# # 4. Создайте объект класса SmallHouse
# # 5. Попробуйте купить созданный дом, убедитесь в получении предупреждения.
# # 6. Поправьте финансовое положение объекта - вызовите метод earn_money()
# # 7. Снова попробуйте купить дом
# # 8. Посмотрите, как изменилось состояние объекта класса Human
# #
# if __name__=='__main__':
#     Human.default_info()
#     new_numan=Human('Ivan', 40)
#     new_numan.info()
#     smal_house=SmallHouse(50000)
#     new_numan.buy_house(smal_house, 15)
#     new_numan.earn_money(60000)
#     new_numan.buy_house(smal_house, 15)
#     new_numan.info()
