import numpy as np
from numpy.core.defchararray import lower

#Ex1
#================================
# a = int(input("First number: "))
# b = int(input("Second number: "))
# x= np.gcd(a, b)
# print(x)
#=================================

#Ex2
#======================================
# input_string = input("Enter a word: ")
# vowels = set("AEIOUaeiou")
# vowel_count = 0
#
# # Loop through the characters in the input string
# for char in input_string:
#     if char in vowels:
#         vowel_count += 1
# print(vowel_count)
#=======================================

#Ex3
#======================================
# s1 = input("First string: ")
# s2 = input("Second string: ")
#
# #number of occurences
# occ=0
# start=0
# while True:
#     start =s2.find(s1,start)
#     if start == -1:
#         break
#     occ  += 1
#     start += 1
# print(occ)
#========================================

#Ex4
#======================================
# s = input("Word to split: ")
# s2 =""
#
# for char in s:
#     if char.isupper():
#         if s2:
#             s2 = s2 + "_"
#         s2 = s2 + char.lower()
#     else:
#             s2 = s2 + char
#
# print(s2)
#======================================

#Ex5
#=====================================
# def spiral_order(matrix):
#     result = []
#     while matrix:
#         # Traverse the first row
#         result.extend(matrix[0])
#         # Remove the first row
#         matrix.pop(0)
#
#         if matrix:
#             # Traverse the right column
#             result.extend(row[-1] for row in matrix)
#             # Remove the right column
#             matrix = [row[:-1] for row in matrix]
#
#         if matrix:
#             # Traverse the last row in reverse
#             result.extend(matrix[-1][::-1])
#             # Remove the last row
#             matrix.pop(-1)
#
#         if matrix:
#             # Traverse the left column
#             result.extend(row[0] for row in matrix)
#             # Remove the left column
#             matrix = [row[1:] for row in matrix]
#
#     return ''.join(result)
#
# matrix = [
#     ['f', 'i', 'r', 's'],
#     ['n', '_', 'l', 't'],
#     ['o', 'b', 'a', '_'],
#     ['h', 't', 'y', 'p']
# ]
#
# result_string = spiral_order(matrix)
# print(result_string)
#=============================================

#Ex6
#===================================
# x=input("Enter a number")
# if x == x[::-1]:
#     print(f"{x} is palindrome")
# else:
#     print(f"{x} is not a palindrome")
#===================================

#Ex7
#=====================================
# def extract_first_number(text):
#     number = ""
#     found_number = False
#
#     for char in text:
#         if char.isdigit():
#             number += char
#             found_number = True
#         elif found_number:
#             break  # Stop once a non-digit character is encountered
#
#     if number:
#         return int(number)
#     else:
#         return None
#
# # Example usage:
# text1 = "An apple is 123 USD"
# number1 = extract_first_number(text1)
# print(number1)  # Output: 123
#
# text2 = "abc123abc"
# number2 = extract_first_number(text2)
# print(number2)  # Output: 123
#==========================================================

#Ex8
#============================================================
# def count_set_bits(number):
#     # Initialize a variable to keep track of the count
#     count = 0
#
#     # Continue until the number becomes 0
#     while number:
#         # Increment the count if the least significant bit is 1
#         count += number & 1
#         # Right shift the number by 1 to check the next bit
#         number >>= 1
#
#     return count
#
#
# # Example usage:
# number = 24
# bit_count = count_set_bits(number)
# print(f"Number of set bits in {number}: {bit_count}")
# print(bin(12))
#========================================================================

#Ex9
#==================================================================
# def most_common_letter(text):
#     # Convert the text to lowercase to ignore casing
#     text = text.lower()
#     # Initialize a dictionary to store letter counts
#     letter_count = {}
#
#     for char in text:
#         if char.isalpha():  # Check if the character is a letter
#             if char in letter_count:
#                 letter_count[char] += 1
#             else:
#                 letter_count[char] = 1
#
#     # Find the most common letter
#     most_common = max(letter_count, key=letter_count.get)
#
#     return most_common, letter_count[most_common]
#
#
# text = "an apple is not a tomato"
# common_letter, count = most_common_letter(text)
# print(f"The most common letter is '{common_letter}' with {count} occurrences.")
#====================================================================================

#Ex10
#===========================================================================
# def count_words(text):
#     # Split the text into words using a single space as the delimiter
#     words = text.split()
#     return len(words)
#
# text = "I have Python exam"
# word_count = count_words(text)
# print(f"The text has {word_count} words.")
#=======================================================================


