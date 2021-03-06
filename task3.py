# Python basic (Part -I) [150 exercises with solution]
# [An editor is available at the bottom of the page to write and execute the scripts.]
#
# 1. Write a Python program to print the following string in a specific format (see the output). 
# Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are" Output :
#
# Twinkle, twinkle, little star,
# 	How I wonder what you are!
# 		Up above the world so high,
# 		Like a diamond in the sky.
# Twinkle, twinkle, little star,
# 	How I wonder what you are
#
#
# print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")
# #
# # 2. Write a Python program to get the Python version you are using. 
# import sys
#
# print('Python version')
# print(sys.version)
#
# 3. Write a Python program to display the current date and time.
# Sample Output :
# Current date and time :
# 2014-07-05 14:34:14
# import datetime
# now=datetime.datetime.now()
# print(now.strftime('%Y-%m-%d %H:%M:%S'))
#
#
# 4. Write a Python program which accepts the radius of a circle from the user and compute the area. 
# Sample Output :
# from math import pi
#
# r = 1.1
# # Area = 3.8013271108436504
# #
# radius = pi * r ** 2
# print(radius)
#
# 5. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them. 
#
# f_name = input("Input your First Name : ")
# l_name = input("Input your Last Name : ")
# print(f'({l_name} {f_name} )')
#
# 6. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers. 
# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')
#
# data = input("Input data : ")
# list=list(data.split(','))
# tuple=tuple(data.split(','))
# print(list)
# print(tuple)

#
# 7. Write a Python program to accept a filename from the user and print the extension of that. 
# Sample filename : abc.java
# Output : java
#
# filename=input('Write filename:')
# format=filename.split('.')[-1:]
# print(format)
#
# 8. Write a Python program to display the first and last colors from the following list. 
# color_list = ["Red","Green","White" ,"Black"]
# print(color_list[:1])
# print(color_list[-1:])

#
#
# 9. Write a Python program to display the examination schedule. (extract the date from exam_st_date). 
# exam_st_date = (11, 12, 2014)
# # Sample Output : The examination will start from : 11 / 12 / 2014
# print( "The examination will start from : %i / %i / %i"%exam_st_date)
#
#
# 10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. 
# Sample value of n is 5
# Expected Result : 615
# def num_fun(num):
#     sum=int(str(num))+int(str(num)*2)+int(str(num)*3)
#     return sum
# print(num_fun(5))
#
#
# 11. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
# Sample function : abs()
# Expected Result :
# abs(number) -> number
# Return the absolute value of the argument.
#

# print(abs.__doc__)
#
# 12. Write a Python program to print the calendar of a given month and year.
# Note : Use 'calendar' module.
#
# import calendar
# y = int(input("Input the year : "))
# m = int(input("Input the month : "))
# print(calendar.month(y, m))
#

# 14. Write a Python program to calculate number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days
# from datetime import date
# between= date(2014, 7, 11)-date(2014, 7, 2)
# print(between)
#
# 15. Write a Python program to get the volume of a sphere with radius 6.
# from math import pi
# radius=6
# v = 4/3 * pi * radius**3
# print(v)
# 16. Write a Python program to get the difference between a given number and 17, if the number is greater than 17
# return double the absolute difference.
# def dif_func(num):
#     if num>17:
#         return ( num-17) *2
#     else:
#         return 17 - num
# print(dif_func(14))
# print(dif_func(17))
# print(dif_func(22))

#
#
# 17. Write a Python program to test whether a number is within 100 of 1000 or 2000. 
#
# def near_thousand(n):
#     return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))
#
#
# print(near_thousand(400))
# print(near_thousand(900))
#
# 18. Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum. 
# #
# def sum_prog(a, b, c):
#     if a==b and b==c:
#         return (a+b+c)*3
#     else:
#         return (a + b + c)
# print(sum_prog(7, 8, 12))
# print(sum_prog(7, 7, 7))

# 19. Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given
# string already begins with "Is" then return the string unchanged.

# def str_pr(string):
#     if string[:2] == "Is":
#
#         return string
#     else:
#         return 'Is '+string
# print(str_pr('khbkblb yfiyv hjvi'))
# print(str_pr('Is khbkblb yfiyv hjvi'))

#
# 20. Write a Python program to get a string which is n (non-negative integer) copies of a given string. 
#
# def larger_string(str, n):
#    result = ""
#    for i in range(n):
#       result = result + str
#    return result
#
# print(larger_string('abc', 2))
# print(larger_string('.py', 3))
#
# 21. Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user. 
#
# def check(num):
#     if num%2==0:
#         return "Number is even"
#     else:
#         return "Number is odd"
# print(check(7))
# print(check(4))
# print(check(-7))
# print(check(0))

#
# 22. Write a Python program to count the number 4 in a given list.

# list=[1, 4, 6, 4, 9, 34, 4, 8, 2, 4]
# print(list.count(4))
#
# 23. Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string.
# Return the n copies of the whole string if the length is less than 2.
# def substring_copy(str, n):
#     flen = 2
#     if flen > len(str):
#         flen = len(str)
#     substr = str[:flen]
#
#     result = ""
#     for i in range(n):
#         result = result + substr
#     return result
#
#
# print(substring_copy('abcdef', 2))
# print(substring_copy('p', 3));
#
# 24. Write a Python program to test whether a passed letter is a vowel or not. 
#
# def is_vowel(char):
#     all_vowels = 'aeiou'
#     return char in all_vowels
# print(is_vowel('c'))
# print(is_vowel('e'))

#
# 25. Write a Python program to check whether a specified value is contained in a group of values. 
# Test Data :
# 3 -> [1, 5, 8, 3] : True
# -1 -> [1, 5, 8, 3] : False
# list=[1, 5, 8, 3]
# def num_list(list, num):
#     return num in list
# print(num_list(list, 5))
# print(num_list(list, 9))
#
#
# 26. Write a Python program to create a histogram from a given list of integers. 
#
# list = [1, 5, 8, 3, 4, 12, 6, 8, 2, 3, 8, 5, 2]
#
# def histogram( items ):
#     for n in items:
#         output = ''
#         times = n
#         while( times > 0 ):
#           output += '*'
#           times = times - 1
#         print(output)
#
# histogram(list)
#
# 27. Write a Python program to concatenate all elements in a list into a string and return it. 
# def conc_num(list):
#     string=''
#     for i in list:
#         string=string+str(i)
#     return string
# print(conc_num([2, 6, 9, 4, 56]))

#
# 28. Write a Python program to print all even numbers from a given numbers list in the same order and stop the printing if any numbers that come after 237 in the sequence. 
# Sample numbers list :
#
# numbers = [
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
#     958,743, 527
#     ]
# #
# def even_num(list):
#     new_list=[]
#     for i in list:
#         if i==237:
#             break
#         if i%2==0:
#             new_list.append((i))
#     return new_list
# print(even_num(numbers))
#
# 29. Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2. 
# Test Data :
# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])
# # Expected Output :
# # {'Black', 'White'}
# #
# print(color_list_1.difference(color_list_2))
# print(color_list_2.difference(color_list_1))

# 30. Write a Python program that will accept the base and height of a triangle and compute the area. 
#
#
# def area(base, height):
#     area=1/2*base*height
#     return area
# print(area(6, 5))
# 31. Write a Python program to compute the greatest common divisor (GCD) of two positive integers. 
#
# def gcd(x, y):
#     gcd = 1
#
#     if x % y == 0:
#         return y
#
#     for k in range(int(y / 2), 0, -1):
#         if x % k == 0 and y % k == 0:
#             gcd = k
#             break
#     return gcd
#
#
# print(gcd(12, 17))
# print(gcd(4, 6))
#
# 32. Write a Python program to get the least common multiple (LCM) of two positive integers. 
#
# def lcm(x, y):
#    if x > y:
#        z = x
#    else:
#        z = y
#
#    while(True):
#        if((z % x == 0) and (z % y == 0)):
#            lcm = z
#            break
#        z += 1
#
#    return lcm
# print(lcm(4, 6))
# print(lcm(15, 17))
#
# 33. Write a Python program to sum of three given integers. However, if two values are equal sum will be zero. 
#
# def sumator(a, b, c):
#     if a==b or b==c or c==a:
#         return 0
#     else:
#         return a+b+c
# print(sumator(7, 3, 2))
# print(sumator(2, 3, 2))
#
# 34. Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20. 
#
#
# def sumator(a, b):
#     sum=a+b
#     if sum>=15 and sum<=20:
#         return 20
#     else:
#         return sum
# print(sumator(5, 11))
# print(sumator(5, 4))


# 35. Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5. 
#
# def prog(a, b):
#
#     if a==b or abs(a-b)==5 or a+b==5:
#         return True
#     else:
#         return False
#
# print(prog(3, 7))
# print(prog(5, 5))
# print(prog(5, 10))
# print(prog(3, 2))
#
# 36. Write a Python program to add two objects if both objects are an integer type. 
#
# def add_numbers(a, b):
#     if not (isinstance(a, int) and isinstance(b, int)):
#          raise TypeError("Inputs must be integers")
#     return a + b
#
# print(add_numbers(10, 20))
#
# 37. Write a Python program to display your details like name, age, address in three different lines. 
#
# name=input('You name:')
# age=input('You age:')
# address=input('You address:')
# print(f'{name}\n {age}\n {address}\n')
#
# 38. Write a Python program to solve (x + y) * (x + y). 
# Test Data : x = 4, y = 3
# Expected Output : (4 + 3) ^ 2) = 49
#
# x=4
# y=3
# def solve(x,y):
#     result=(x+y)**2
#     print(f'({x}+{y})^2 = {result}')
# #
# solve(x, y)
# 39. Write a Python program to compute the future value of a specified principal amount, compounded annually. 
# Test Data : amt = 10000, int = 3.5, years = 7
# Expected Output : 12722.79
#
# amt = 10000
# int = 3.5
# years = 7
# def amount(amt, int, years):
#     sum=amt*((1+(int/100))**years)
#     return sum
# print(amount(amt, int, years))
#
# 40. Write a Python program to compute the distance between the points (x1, y1) and (x2, y2). 
#
# import math
# p1 = [4, 0]
# p2 = [6, 6]
# distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )
#
# print(distance)
#
# 41. Write a Python program to check whether a file exists. 

# import os.path
# open('abc.txt', 'w')
# print(os.path.isfile('abc.txt'))

# 48. Write a Python program to parse a string to Float or Integer. 
#
# n = "246.2458"
# print(float(n))
# print(int(float(n)))
#
# 50. Write a Python program to print without newline or space. 
#
# for i in range(1, 10):
#     print('*', end='')
#
# 52. Write a Python program to print to stderr. 
#
# from sys import stderr
#
# print(stderr)
#
# 58. Write a python program to find the sum of the first n positive integers. 
#

# def sum(count):
#     sum =0
#     for i in range(1, count+1):
#         sum=sum+i
#     return sum
# print(sum(5))
#
# 59. Write a Python program to convert height (in feet and inches) to centimeters. 
#
# print("Input your height: ")
# h_ft = int(input("Feet: "))
# h_inch = int(input("Inches: "))
#
# h_inch += h_ft * 12
# h_cm = round(h_inch * 2.54, 1)
#
# print("Your height is : %d cm." % h_cm)
#
# 60. Write a Python program to calculate the hypotenuse of a right angled triangle. 
#
#
# 61. Write a Python program to convert the distance (in feet) to inches, yards, and miles. 
#
#
# 62. Write a Python program to convert all units of time into seconds. 
#
#
# 63. Write a Python program to get an absolute file path. 
#
#
# 64. Write a Python program to get file creation and modification date/times. 
#
#
# 65. Write a Python program to convert seconds to day, hour, minutes and seconds. 
#
#
# 66. Write a Python program to calculate body mass index. 
#
#
# 67. Write a Python program to convert pressure in kilopascals to pounds per square inch, a millimeter of mercury (mmHg) and atmosphere pressure. 
#
#
# 68. Write a Python program to calculate the sum of the digits in an integer. 
#
#
# 69. Write a Python program to sort three integers without using conditional statements and loops. 
#
#
# 70. Write a Python program to sort files by date. 
#
#
# 71. Write a Python program to get a directory listing, sorted by creation date. 
#
#
# 72. Write a Python program to get the details of math module. 
#
#
# 73. Write a Python program to calculate midpoints of a line. 
#
#
# 74. Write a Python program to hash a word. 
#
#
# 75. Write a Python program to get the copyright information. 
#
#
# 76. Write a Python program to get the command-line arguments (name of the script, the number of arguments, arguments) passed to a script. 
#
#
# 77. Write a Python program to test whether the system is a big-endian platform or little-endian platform. 
#
#
# 78. Write a Python program to find the available built-in modules. 
#
#
# 79. Write a Python program to get the size of an object in bytes. 
#
#
# 80. Write a Python program to get the current value of the recursion limit. 
#
#
# 81. Write a Python program to concatenate N strings. 
#
#
# 82. Write a Python program to calculate the sum over a container. 
#
#
# 83. Write a Python program to test whether all numbers of a list is greater than a certain number. 
#
#
# 84. Write a Python program to count the number occurrence of a specific character in a string. 
#
#
# 85. Write a Python program to check whether a file path is a file or a directory. 
#
#
# 86. Write a Python program to get the ASCII value of a character. 
#
#
# 87. Write a Python program to get the size of a file. 
#
#
# 88. Given variables x=30 and y=20, write a Python program to print "30+20=50". 
#
#
# 89. Write a Python program to perform an action if a condition is true. 
# Given a variable name, if the value is 1, display the string "First day of a Month!" and do nothing if the value is not equal.
#
#
# 90. Write a Python program to create a copy of its own source code. 
#
#
# 91. Write a Python program to swap two variables. 
#
#
# 92. Write a Python program to define a string containing special characters in various forms. 
#
#
# 93. Write a Python program to get the identity of an object. 
#
#
# 94. Write a Python program to convert a byte string to a list of integers. 
#
#
# 95. Write a Python program to check whether a string is numeric. 
#
#
# 96. Write a Python program to print the current call stack. 
#
#
# 97. Write a Python program to list the special variables used within the language. 
#
#
# 98. Write a Python program to get the system time. 
#
# Note : The system time is important for debugging, network information, random number seeds, or something as simple as program performance.
#
#
# 99. Write a Python program to clear the screen or terminal. 
#
#
# 100. Write a Python program to get the name of the host on which the routine is running. 
#
#
# 101. Write a Python program to access and print a URL's content to the console. 
#
#
# 102. Write a Python program to get system command output. 
#
#
# 103. Write a Python program to extract the filename from a given path. 
#
#
# 104. Write a Python program to get the effective group id, effective user id, real group id, a list of supplemental group ids associated with the current process. 
# Note: Availability: Unix.
#
#
# 105. Write a Python program to get the users environment. 
#
#
# 106. Write a Python program to divide a path on the extension separator. 
#
#
# 107. Write a Python program to retrieve file properties. 
#
#
# 108. Write a Python program to find path refers to a file or directory when you encounter a path name. 
#
#
# 109. Write a Python program to check if a number is positive, negative or zero. 
#
#
# 110. Write a Python program to get numbers divisible by fifteen from a list using an anonymous function. 
#
#
# 111. Write a Python program to make file lists from current directory using a wildcard. 
#
#
# 112. Write a Python program to remove the first item from a specified list. 
#
#
# 113. Write a Python program to input a number, if it is not a number generate an error message. 
#
#
# 114. Write a Python program to filter the positive numbers from a list. 
#
#
# 115. Write a Python program to compute the product of a list of integers (without using for loop). 
#
#
# 116. Write a Python program to print Unicode characters. 
#
#
# 117. Write a Python program to prove that two string variables of same value point same memory location. 
#
#
# 118. Write a Python program to create a bytearray from a list. 
#
#
# 119. Write a Python program to display a floating number in specified numbers. 
#
#
# 120. Write a Python program to format a specified string to limit the number of characters to 6. 
#
#
# 121. Write a Python program to determine whether variable is defined or not. 
#
#
# 122. Write a Python program to empty a variable without destroying it. 
#
# Sample data: n=20
# d = {"x":200}
# Expected Output : 0
# {}
#
#
#
# 123. Write a Python program to determine the largest and smallest integers, longs, floats. 
#
#
# 124. Write a Python program to check whether multiple variables have the same value. 
#
#
# 125. Write a Python program to sum of all counts in a collections.
#
#
# 126. Write a Python program to get the actual module object for a given object. 
#
#
# 127. Write a Python program to check whether an integer fits in 64 bits. 
#
#
# 128. Write a Python program to check whether lowercase letters exist in a string. 
#
#
# 129. Write a Python program to add trailing and leading zeroes to a string. 
#
#
# 130. Write a Python program to use double quotes to display strings. 
#
#
# 131. Write a Python program to split a variable length string into variables. 
#
#
# 132. Write a Python program to list home directory without absolute path. 
#
#
# 133. Write a Python program to calculate the time runs (difference between start and current time) of a program. 
#
#
# 134. Write a Python program to input two integers in a single line. 
#
#
# 135. Write a Python program to print a variable without spaces between values. 
# Sample value : x =30
# Expected output : Value of x is "30"
#
#
# 136. Write a Python program to find files and skip directories of a given directory. 
#
#
# 137. Write a Python program to extract single key-value pair of a dictionary in variables. 
#
#
# 138. Write a Python program to convert true to 1 and false to 0. 
#
#
# 139. Write a Python program to valid a IP address. 
#
#
# 140. Write a Python program to convert an integer to binary keep leading zeros. 
# Sample data : x=12
# Expected output : 00001100
# 0000001100
#
#
# 141. Write a python program to convert decimal to hexadecimal. 
# Sample decimal number: 30, 4
# Expected output: 1e, 04
#
#
# 142. Write a Python program to find the operating system name, platform and platform release date. 
# Operating system name:
# posix
# Platform name:
# Linux
# Platform release:
# 4.4.0-47-generic
#
#
# 143. Write a Python program to determine if the python shell is executing in 32bit or 64bit mode on operating system. 
#
#
# 144. Write a Python program to check whether variable is of integer or string. 
#
#
# 145. Write a Python program to test if a variable is a list or tuple or a set. 
#
#
# 146. Write a Python program to find the location of Python module sources. 
#
#
# 147. Write a Python function to check whether a number is divisible by another number. Accept two integers values form the user. 
#
#
# 148. Write a Python function to find the maximum and minimum numbers from a sequence of numbers. 
# Note: Do not use built-in functions.
#
#
# 149. Write a Python function that takes a positive integer and returns the sum of the cube of all the positive integers smaller than the specified number. 
#
#
# 150. Write a Python function to find a distinct pair of numbers whose product is odd from a sequence of integer values. 
