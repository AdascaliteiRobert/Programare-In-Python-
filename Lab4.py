from _collections import deque

#Ex1
# class Stack:
#     def __init__(self):
#         self.stack = []
#
#     def push(self, item):
#         self.stack.append(item)
#
#     def pop(self):
#         if len(self.stack) > 0:
#             return self.stack.pop()
#         else:
#             return None
#
#     def peek(self):
#         if len(self.stack) > 0:
#             return self.stack[-1]
#         else:
#             return None
#
#     def empty(self):
#         self.stack = []
#
# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)
#
#
# print(stack.stack)
#
# popped_item = stack.pop()
# print(f"Popped item: {popped_item}")
#
#
# top_item = stack.peek()
# print(f"Top item: {top_item}")
#
# stack.empty()
# print(stack.stack)
#
# popped_item = stack.pop()
# print(f"Popped item: {popped_item}")
#
# top_item = stack.peek()
# print(f"Top item: {top_item}")


#Ex2

# class Queue:
#     def __init__(self):
#         self.queue = deque()
#
#     def push(self ,item):
#         self.queue.append(item)
#
#     def pop(self):
#         if self.queue:
#             return self.queue.popleft()
#         else:
#             return None
#
#     def peek(self):
#        if self.queue:
#            return self.queue[0]
#        else:
#            return None
#
#     def empty(self):
#         self.queue = deque()
#
#
#
# queue = Queue()
# queue.push(1)
# queue.push(2)
# queue.push(3)
#
# print(queue.queue)
#
# popped_item = queue.pop()
# print(f"Popped item: {popped_item}")
#
# first_item = queue.peek()
# print(f"First item: {first_item}")
#
# queue.empty()
# print(queue.queue)
#
# popped_item = queue.pop()
# print(f"Popped item: {popped_item}")
#
# first_item = queue.peek()
# print(f"First item: {first_item}")


#Ex3

# class Matrix:
#     def __init__(self, rows, columns):
#         self.rows = rows
#         self.columns = columns
#         self.data = [[0] * columns for _ in range(rows)]
#
#     def get(self, row, col):
#         if 0 <= row < self.rows and 0 <= col < self.columns:
#             return self.data[row][col]
#         else:
#             raise IndexError("Row or column index out of bounds")
#
#     def set(self, row, col, value):
#         if 0 <= row < self.rows and 0 <= col < self.columns:
#             self.data[row][col] = value
#         else:
#             raise IndexError("Row or column index out of bounds")
#
#     def transpose(self):
#         transposed = Matrix(self.columns, self.rows)
#         for i in range(self.rows):
#             for j in range(self.columns):
#                 transposed.data[j][i] = self.data[i][j]
#         return transposed
#
#     def multiply(self, other_matrix):
#         if self.columns != other_matrix.rows:
#             raise ValueError("Matrix dimensions are incompatible for multiplication")
#
#         result = Matrix(self.rows, other_matrix.columns)
#         for i in range(self.rows):
#             for j in range(other_matrix.columns):
#                 for k in range(self.columns):
#                     result.data[i][j] += self.data[i][k] * other_matrix.data[k][j]
#         return result
#
#     def apply(self, func):
#         for i in range(self.rows):
#             for j in range(self.columns):
#                 self.data[i][j] = func(self.data[i][j])
#
#     def __str__(self):
#         return "\n".join([" ".join(map(str, row)) for row in self.data])
#
#
# matrix = Matrix(2, 3)
# matrix.set(0, 0, 1)
# matrix.set(0, 1, 2)
# matrix.set(0, 2, 3)
# matrix.set(1, 0, 4)
# matrix.set(1, 1, 5)
# matrix.set(1, 2, 6)
#
# print("Original Matrix:")
# print(matrix)
#
# transposed_matrix = matrix.transpose()
# print("\nTransposed Matrix:")
# print(transposed_matrix)
#
# identity_matrix = Matrix(3, 3)
# identity_matrix.set(0, 0, 1)
# identity_matrix.set(1, 1, 1)
# identity_matrix.set(2, 2, 1)
#
# result = matrix.multiply(identity_matrix)
# print("\nMatrix Multiplication Result:")
# print(result)
#
# matrix.apply(lambda x: x * 2)
# print("\nMatrix after applying transformation (multiply by 2):")
# print(matrix)
