# Python basic (Part -I) [150 exercises with solution]
# [An editor is available at the bottom of the page to write and execute the scripts.]
#
# 1. Write a Python program to print the following string in a specific format (see the output). Go to the editor
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
# # 2. Write a Python program to get the Python version you are using. Go to the editor
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
# 4. Write a Python program which accepts the radius of a circle from the user and compute the area. Go to the editor
# Sample Output :
# from math import pi
#
# r = 1.1
# # Area = 3.8013271108436504
# #
# radius = pi * r ** 2
# print(radius)
#
# 5. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them. Go to the editor
#
# f_name = input("Input your First Name : ")
# l_name = input("Input your Last Name : ")
# print(f'({l_name} {f_name} )')
#
# 6. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers. Go to the editor
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
# 7. Write a Python program to accept a filename from the user and print the extension of that. Go to the editor
# Sample filename : abc.java
# Output : java
#
# filename=input('Write filename:')
# format=filename.split('.')[-1:]
# print(format)
#
# 8. Write a Python program to display the first and last colors from the following list. Go to the editor
# color_list = ["Red","Green","White" ,"Black"]
# print(color_list[:1])
# print(color_list[-1:])

#
#
# 9. Write a Python program to display the examination schedule. (extract the date from exam_st_date). Go to the editor
# exam_st_date = (11, 12, 2014)
# # Sample Output : The examination will start from : 11 / 12 / 2014
# print( "The examination will start from : %i / %i / %i"%exam_st_date)
#
#
# 10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
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
# 13. Write a Python program to print the following 'here document'. Go to the editor
# Sample string :
# a string that you "don't" have to escape
# This
# is a ....... multi-line
# heredoc string --------> example
#
#
# 14. Write a Python program to calculate number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days
#
#
# 15. Write a Python program to get the volume of a sphere with radius 6.
#
#
# 16. Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference. Go to the editor
#
#
# 17. Write a Python program to test whether a number is within 100 of 1000 or 2000. Go to the editor
#
#
# 18. Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum. Go to the editor
#
#
# 19. Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged. Go to the editor
#
#
# 20. Write a Python program to get a string which is n (non-negative integer) copies of a given string. Go to the editor
#
#
# 21. Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user. Go to the editor
#
#
# 22. Write a Python program to count the number 4 in a given list. Go to the editor
#
#
# 23. Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2. Go to the editor
#
#
# 24. Write a Python program to test whether a passed letter is a vowel or not. Go to the editor
#
#
# 25. Write a Python program to check whether a specified value is contained in a group of values. Go to the editor
# Test Data :
# 3 -> [1, 5, 8, 3] : True
# -1 -> [1, 5, 8, 3] : False
#
#
#
# 26. Write a Python program to create a histogram from a given list of integers. Go to the editor
#
#
# 27. Write a Python program to concatenate all elements in a list into a string and return it. Go to the editor
#
#
# 28. Write a Python program to print all even numbers from a given numbers list in the same order and stop the printing if any numbers that come after 237 in the sequence. Go to the editor
# Sample numbers list :
#
# numbers = [
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
#     958,743, 527
#     ]
#
#
# 29. Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2. Go to the editor
# Test Data :
# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])
# Expected Output :
# {'Black', 'White'}
#
#
# 30. Write a Python program that will accept the base and height of a triangle and compute the area. Go to the editor
#
#
# 31. Write a Python program to compute the greatest common divisor (GCD) of two positive integers. Go to the editor
#
#
# 32. Write a Python program to get the least common multiple (LCM) of two positive integers. Go to the editor
#
#
# 33. Write a Python program to sum of three given integers. However, if two values are equal sum will be zero. Go to the editor
#
#
# 34. Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20. Go to the editor
#
#
# 35. Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5. Go to the editor
#
#
# 36. Write a Python program to add two objects if both objects are an integer type. Go to the editor
#
#
# 37. Write a Python program to display your details like name, age, address in three different lines. Go to the editor
#
#
# 38. Write a Python program to solve (x + y) * (x + y). Go to the editor
# Test Data : x = 4, y = 3
# Expected Output : (4 + 3) ^ 2) = 49
#
#
# 39. Write a Python program to compute the future value of a specified principal amount, compounded annually. Go to the editor
# Test Data : amt = 10000, int = 3.5, years = 7
# Expected Output : 12722.79
#
#
# 40. Write a Python program to compute the distance between the points (x1, y1) and (x2, y2). Go to the editor
#
#
# 41. Write a Python program to check whether a file exists. Go to the editor
#
#
# 42. Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS. Go to the editor
#
#
# 43. Write a Python program to get OS name, platform and release information. Go to the editor
#
#
# 44. Write a Python program to locate Python site-packages. Go to the editor
#
#
# 45. Write a python program to call an external command in Python. Go to the editor
#
#
# 46. Write a python program to get the path and name of the file that is currently executing. Go to the editor
#
#
# 47. Write a Python program to find out the number of CPUs using. Go to the editor
#
#
# 48. Write a Python program to parse a string to Float or Integer. Go to the editor
#
#
# 49. Write a Python program to list all files in a directory in Python. Go to the editor
#
#
# 50. Write a Python program to print without newline or space. Go to the editor
#
#
# 51. Write a Python program to determine profiling of Python programs. Go to the editor
# Note: A profile is a set of statistics that describes how often and for how long various parts of the program executed. These statistics can be formatted into reports via the pstats module.
#
#
# 52. Write a Python program to print to stderr. Go to the editor
#
#
# 53. Write a python program to access environment variables. Go to the editor
#
#
# 54. Write a Python program to get the current username Go to the editor
#
#
# 55. Write a Python to find local IP addresses using Python's stdlib Go to the editor
#
#
# 56. Write a Python program to get height and width of the console window. Go to the editor
#
#
# 57. Write a Python program to get execution time for a Python method. Go to the editor
#
#
# 58. Write a python program to find the sum of the first n positive integers. Go to the editor
#
#
# 59. Write a Python program to convert height (in feet and inches) to centimeters. Go to the editor
#
#
# 60. Write a Python program to calculate the hypotenuse of a right angled triangle. Go to the editor
#
#
# 61. Write a Python program to convert the distance (in feet) to inches, yards, and miles. Go to the editor
#
#
# 62. Write a Python program to convert all units of time into seconds. Go to the editor
#
#
# 63. Write a Python program to get an absolute file path. Go to the editor
#
#
# 64. Write a Python program to get file creation and modification date/times. Go to the editor
#
#
# 65. Write a Python program to convert seconds to day, hour, minutes and seconds. Go to the editor
#
#
# 66. Write a Python program to calculate body mass index. Go to the editor
#
#
# 67. Write a Python program to convert pressure in kilopascals to pounds per square inch, a millimeter of mercury (mmHg) and atmosphere pressure. Go to the editor
#
#
# 68. Write a Python program to calculate the sum of the digits in an integer. Go to the editor
#
#
# 69. Write a Python program to sort three integers without using conditional statements and loops. Go to the editor
#
#
# 70. Write a Python program to sort files by date. Go to the editor
#
#
# 71. Write a Python program to get a directory listing, sorted by creation date. Go to the editor
#
#
# 72. Write a Python program to get the details of math module. Go to the editor
#
#
# 73. Write a Python program to calculate midpoints of a line. Go to the editor
#
#
# 74. Write a Python program to hash a word. Go to the editor
#
#
# 75. Write a Python program to get the copyright information. Go to the editor
#
#
# 76. Write a Python program to get the command-line arguments (name of the script, the number of arguments, arguments) passed to a script. Go to the editor
#
#
# 77. Write a Python program to test whether the system is a big-endian platform or little-endian platform. Go to the editor
#
#
# 78. Write a Python program to find the available built-in modules. Go to the editor
#
#
# 79. Write a Python program to get the size of an object in bytes. Go to the editor
#
#
# 80. Write a Python program to get the current value of the recursion limit. Go to the editor
#
#
# 81. Write a Python program to concatenate N strings. Go to the editor
#
#
# 82. Write a Python program to calculate the sum over a container. Go to the editor
#
#
# 83. Write a Python program to test whether all numbers of a list is greater than a certain number. Go to the editor
#
#
# 84. Write a Python program to count the number occurrence of a specific character in a string. Go to the editor
#
#
# 85. Write a Python program to check whether a file path is a file or a directory. Go to the editor
#
#
# 86. Write a Python program to get the ASCII value of a character. Go to the editor
#
#
# 87. Write a Python program to get the size of a file. Go to the editor
#
#
# 88. Given variables x=30 and y=20, write a Python program to print "30+20=50". Go to the editor
#
#
# 89. Write a Python program to perform an action if a condition is true. Go to the editor
# Given a variable name, if the value is 1, display the string "First day of a Month!" and do nothing if the value is not equal.
#
#
# 90. Write a Python program to create a copy of its own source code. Go to the editor
#
#
# 91. Write a Python program to swap two variables. Go to the editor
#
#
# 92. Write a Python program to define a string containing special characters in various forms. Go to the editor
#
#
# 93. Write a Python program to get the identity of an object. Go to the editor
#
#
# 94. Write a Python program to convert a byte string to a list of integers. Go to the editor
#
#
# 95. Write a Python program to check whether a string is numeric. Go to the editor
#
#
# 96. Write a Python program to print the current call stack. Go to the editor
#
#
# 97. Write a Python program to list the special variables used within the language. Go to the editor
#
#
# 98. Write a Python program to get the system time. Go to the editor
#
# Note : The system time is important for debugging, network information, random number seeds, or something as simple as program performance.
#
#
# 99. Write a Python program to clear the screen or terminal. Go to the editor
#
#
# 100. Write a Python program to get the name of the host on which the routine is running. Go to the editor
#
#
# 101. Write a Python program to access and print a URL's content to the console. Go to the editor
#
#
# 102. Write a Python program to get system command output. Go to the editor
#
#
# 103. Write a Python program to extract the filename from a given path. Go to the editor
#
#
# 104. Write a Python program to get the effective group id, effective user id, real group id, a list of supplemental group ids associated with the current process. Go to the editor
# Note: Availability: Unix.
#
#
# 105. Write a Python program to get the users environment. Go to the editor
#
#
# 106. Write a Python program to divide a path on the extension separator. Go to the editor
#
#
# 107. Write a Python program to retrieve file properties. Go to the editor
#
#
# 108. Write a Python program to find path refers to a file or directory when you encounter a path name. Go to the editor
#
#
# 109. Write a Python program to check if a number is positive, negative or zero. Go to the editor
#
#
# 110. Write a Python program to get numbers divisible by fifteen from a list using an anonymous function. Go to the editor
#
#
# 111. Write a Python program to make file lists from current directory using a wildcard. Go to the editor
#
#
# 112. Write a Python program to remove the first item from a specified list. Go to the editor
#
#
# 113. Write a Python program to input a number, if it is not a number generate an error message. Go to the editor
#
#
# 114. Write a Python program to filter the positive numbers from a list. Go to the editor
#
#
# 115. Write a Python program to compute the product of a list of integers (without using for loop). Go to the editor
#
#
# 116. Write a Python program to print Unicode characters. Go to the editor
#
#
# 117. Write a Python program to prove that two string variables of same value point same memory location. Go to the editor
#
#
# 118. Write a Python program to create a bytearray from a list. Go to the editor
#
#
# 119. Write a Python program to display a floating number in specified numbers. Go to the editor
#
#
# 120. Write a Python program to format a specified string to limit the number of characters to 6. Go to the editor
#
#
# 121. Write a Python program to determine whether variable is defined or not. Go to the editor
#
#
# 122. Write a Python program to empty a variable without destroying it. Go to the editor
#
# Sample data: n=20
# d = {"x":200}
# Expected Output : 0
# {}
#
#
#
# 123. Write a Python program to determine the largest and smallest integers, longs, floats. Go to the editor
#
#
# 124. Write a Python program to check whether multiple variables have the same value. Go to the editor
#
#
# 125. Write a Python program to sum of all counts in a collections.Go to the editor
#
#
# 126. Write a Python program to get the actual module object for a given object. Go to the editor
#
#
# 127. Write a Python program to check whether an integer fits in 64 bits. Go to the editor
#
#
# 128. Write a Python program to check whether lowercase letters exist in a string. Go to the editor
#
#
# 129. Write a Python program to add trailing and leading zeroes to a string. Go to the editor
#
#
# 130. Write a Python program to use double quotes to display strings. Go to the editor
#
#
# 131. Write a Python program to split a variable length string into variables. Go to the editor
#
#
# 132. Write a Python program to list home directory without absolute path. Go to the editor
#
#
# 133. Write a Python program to calculate the time runs (difference between start and current time) of a program. Go to the editor
#
#
# 134. Write a Python program to input two integers in a single line. Go to the editor
#
#
# 135. Write a Python program to print a variable without spaces between values. Go to the editor
# Sample value : x =30
# Expected output : Value of x is "30"
#
#
# 136. Write a Python program to find files and skip directories of a given directory. Go to the editor
#
#
# 137. Write a Python program to extract single key-value pair of a dictionary in variables. Go to the editor
#
#
# 138. Write a Python program to convert true to 1 and false to 0. Go to the editor
#
#
# 139. Write a Python program to valid a IP address. Go to the editor
#
#
# 140. Write a Python program to convert an integer to binary keep leading zeros. Go to the editor
# Sample data : x=12
# Expected output : 00001100
# 0000001100
#
#
# 141. Write a python program to convert decimal to hexadecimal. Go to the editor
# Sample decimal number: 30, 4
# Expected output: 1e, 04
#
#
# 142. Write a Python program to find the operating system name, platform and platform release date. Go to the editor
# Operating system name:
# posix
# Platform name:
# Linux
# Platform release:
# 4.4.0-47-generic
#
#
# 143. Write a Python program to determine if the python shell is executing in 32bit or 64bit mode on operating system. Go to the editor
#
#
# 144. Write a Python program to check whether variable is of integer or string. Go to the editor
#
#
# 145. Write a Python program to test if a variable is a list or tuple or a set. Go to the editor
#
#
# 146. Write a Python program to find the location of Python module sources. Go to the editor
#
#
# 147. Write a Python function to check whether a number is divisible by another number. Accept two integers values form the user. Go to the editor
#
#
# 148. Write a Python function to find the maximum and minimum numbers from a sequence of numbers. Go to the editor
# Note: Do not use built-in functions.
#
#
# 149. Write a Python function that takes a positive integer and returns the sum of the cube of all the positive integers smaller than the specified number. Go to the editor
#
#
# 150. Write a Python function to find a distinct pair of numbers whose product is odd from a sequence of integer values. Go to the editor
