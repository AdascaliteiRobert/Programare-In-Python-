import numpy as np

#Ex1
# def generate_fibonacci(n):
#     if n <= 0:
#         return []
#     elif n == 1:
#         return [0]
#     elif n == 2:
#         return [0, 1]
#
#     fibonacci_sequence = [0, 1]
#     while len(fibonacci_sequence) < n:
#         next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
#         fibonacci_sequence.append(next_number)
#
#     return fibonacci_sequence
#
# n = 10
# fibonacci_numbers = generate_fibonacci(n)
# print(fibonacci_numbers)


#Ex2
# def primeNumbers(numbers):
#     primeNumbersList = []
#
#     for number in numbers:
#         if number <= 1:
#             continue  # Skip 0 and 1
#         elif number == 2:
#             primeNumbersList.append(number)
#         else:
#             is_prime = True
#             for i in range(2, int(number ** 0.5) + 1):
#                 if number % i == 0:
#                     is_prime = False
#                     break
#             if is_prime:
#                 primeNumbersList.append(number)
#
#     return primeNumbersList
#
#
# print(primeNumbers([1, 2, 3, 4, 5 , 6 , 7 , 8]))


#Ex3
# def twoLists ( listA , listB):
#     reunited = listA + listB
#     intersected =[]
#     a_b = []
#     b_a = []
#     for number in listA:
#         if number in listB:
#             intersected.append(number)
#         else: a_b.append(number)
#     for number in listB:
#         if number not  in listA:
#                 b_a.append(number)
#     return  reunited , intersected , a_b , b_a
#
# A= [1, 2, 3 , 4, 5]
# B= [5,6,7,8,9,10]
# print(twoLists(A,B))


#Ex4

# def compose(notes, moves, start_position):
#     song = []
#     position = start_position
#     song.append(notes[start_position])
#     for move in moves:
#         position += move
#         position = position % len(notes)
#         song.append(notes[position])
#
#     return song
#
# notes = ["do", "re", "mi", "fa", "sol"]
# moves = [1, -3, 4, 2]
# start_position = 4
#
# result = compose(notes, moves, start_position)
# print(result)

#Ex5

# def replace_below_diagonal_with_zeros(matrix):
#     num_rows = len(matrix)
#     num_cols = len(matrix[0])
#
#     for row in range(num_rows):
#         for col in range(num_cols):
#             if row > col:
#                 matrix[row][col] = 0
#
#     return matrix
#
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# result = replace_below_diagonal_with_zeros(matrix)
# for row in result:
#     print(row)

#Ex6

# def findInList(lists, x):
#     combined_list = []
#
#     for lst in lists:
#         combined_list.extend(lst)
#
#     frequency = {}
#
#     for item in combined_list:
#         if item in frequency:
#             frequency[item] += 1
#         else:
#             frequency[item] = 1
#
#     x_times_list = [item for item, count in frequency.items() if count == x]
#
#     return x_times_list
#
#
# lists = [[1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"]]
# x = 2
#
# result = findInList(lists, x)
# print(result)

#Ex7

# def palindrome_tuple (num_list):
#     max_palindrome=0
#     count=0
#     for numbers in num_list:
#         number_str = str(numbers)
#         if number_str == number_str[::-1]:
#             count+=1
#         if  int(number_str) > max_palindrome:
#             max_palindrome=max(int(number_str) , max_palindrome)
#     return count , max_palindrome
#
#
# num_list = [11 , 20 , 22 , 54 , 67 , 2002 , 100001 , 44 , 404, 55, 1000000001]
# print(palindrome_tuple(list))

#Ex8

# def process_strings(x=1, string_list=[], flag=True):
#     result_if_true = []
#     result_if_false = []
#     for s in string_list:
#         char_list_if_true = []
#         char_list_if_false =[]
#
#         for char in s:
#             ascii_code = ord(char)
#
#             if (ascii_code % x == 0):
#                 char_list_if_true.append(char)
#             else:
#                 char_list_if_false.append(char)
#         result_if_true.append(char_list_if_true)
#         result_if_false.append(char_list_if_false)
#
#     if flag:
#         return result_if_true
#     else:
#         return result_if_false

# x = 2
# string_list = ["test", "hello", "lab002"]
# flag = False
# output = process_strings(x, string_list, flag)
# print(output)

#Ex9

# def Field (matrix):
#  row = len(matrix)
#  col = len(matrix[0])
#  seats = []
#  for i in range(row):
#     for j in range(col):
#         for k in range(i+1,row):
#          if matrix[i][j] >= matrix[k][j]:
#             seat = k, j
#             seats.append(seat)
#          else:
#              break
#
#  return seats
#
# matrix = [[1, 2, 3, 2, 1, 1],
#
# [2, 4, 4, 3, 7, 2],
#
# [5, 5, 2, 5, 6, 4],
#
# [6, 6, 7, 6, 7, 5]]
#
# print(Field(matrix))

#Ex10

# def combine_lists(*lists):
#     combined = list(zip(*lists))
#     return combined
#
# list1 = [1, 2, 3]
# list2 = [5, 6, 7]
# list3 = ["a", "b", "c"]
#
# result = combine_lists(list1, list2, list3)
# print(result)

#Ex11

# def order_tuples_by_third_character(tuples):
#     def custom_key(item):
#         if len(item[1]) >= 3: # verificam daca al doilea element are lungimea mai mare decat 3
#             return item[1][2]
#         else:
#             return ''  # in caz contrar returnam un string gol
#
#     return sorted(tuples, key=custom_key)
#
# # Example usage:
# tuples = [('abc', 'bcd'), ('abc', 'zza')]
# result = order_tuples_by_third_character(tuples)
# print(result)

#Ex12

# def group_by_rhyme(words):
#     rhyme_groups = {}
#
#     for word in words:
#         rhyme = word[-2:]
#         if rhyme in rhyme_groups:
#             rhyme_groups[rhyme].append(word)
#         else:
#             rhyme_groups[rhyme] = [word]
#
#     return list(rhyme_groups.values())
#
#
# # Example usage:
# words = ['ana', 'banana', 'carte', 'arme', 'parte']
# result = group_by_rhyme(words)
# print(result)