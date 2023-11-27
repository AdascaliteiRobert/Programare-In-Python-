import sys
import os


#Ex1

#
# def read_and_print_files(directory_path, file_extension):
#     try:
#
#         if not os.path.isdir(directory_path):
#             raise ValueError("Invalid directory path")
#
#         if not file_extension.startswith("."):
#             raise ValueError("File extension should start with '.'")
#
#         files = [f for f in os.listdir(directory_path) if f.endswith(file_extension)]
#
#         for file_name in files:
#             file_path = os.path.join(directory_path, file_name)
#             try:
#                 with open(file_path, 'r') as file:
#                     content = file.read()
#                     print(f"Contents of {file_name}:\n{content}\n{'='*30}")
#             except Exception as e:
#                 print(f"Error reading file {file_name}: {e}")
#
#     except ValueError as ve:
#         print(f"Error: {ve}")
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")
#
# if __name__ == "__main__":
#
#     if len(sys.argv) != 3:
#
#         print("Correct usage: python Lab6.py <directory_path> <file_extension>")
#     else:
#         directory_path = sys.argv[1]
#         file_extension = sys.argv[2]
#         read_and_print_files(directory_path, file_extension)

#Ex2

# def rename_files_with_sequence(directory_path):
#     try:
#         if not os.path.isdir(directory_path):
#             raise ValueError("Invalid directory path")
#
#         files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
#
#         for i, file_name in enumerate(files, start=1):
#             old_path = os.path.join(directory_path, file_name)
#             new_name = f"file{i}{os.path.splitext(file_name)[1]}"
#             new_path = os.path.join(directory_path, new_name)
#             os.rename(old_path, new_path)
#
#             print(f"Renamed: {file_name} -> {new_name}")
#
#     except ValueError as ve:
#         print(f"Error: {ve}")
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")
#
# if __name__ == "__main__":
#
#     if len(sys.argv) != 2:
#         print("Incorrect number of arguments")
#         print("Correct usage: python Lab6.py <directory_path>")
#     else:
#         directory_path = sys.argv[1]
#         rename_files_with_sequence(directory_path)

#Ex3

# def calculate_total_size(directory_path):
#     try:
#         if not os.path.isdir(directory_path):
#             raise ValueError("Invalid directory path")
#
#         total_size = 0
#
#         for foldername, subfolders, filenames in os.walk(directory_path):
#             for filename in filenames:
#                 file_path = os.path.join(foldername, filename)
#                 try:
#                     file_size = os.path.getsize(file_path)
#                     total_size += file_size
#                 except Exception as e:
#                     print(f"Error accessing file {file_path}: {e}")
#
#         print(f"Total size of all files in {directory_path}: {total_size} bytes")
#
#     except ValueError as ve:
#         print(f"Error: {ve}")
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")
#
# if __name__ == "__main__":
#     if len(sys.argv) != 2:
#        print("Incorrect number of arguments")
#        print("Correct usage: python Lab6.py <directory_path>")
#     else:
#         directory_path = sys.argv[1]
#         calculate_total_size(directory_path)

#Ex4

#
# def count_files_by_extension(directory_path):
#     try:
#         if not os.path.isdir(directory_path):
#             raise ValueError("Invalid directory path")
#
#         files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
#
#         extension_counts = {}
#
#
#         for file_name in files:
#             _, file_extension = os.path.splitext(file_name)
#             extension = file_extension.lower()
#             extension_counts[extension] = extension_counts.get(extension, 0) + 1
#
#         if extension_counts:
#             print("File counts by extension:")
#             for extension, count in extension_counts.items():
#                 print(f"{extension}: {count} files")
#         else:
#             print("No files found in the directory.")
#
#     except ValueError as ve:
#         print(f"Error: {ve}")
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")
#
# if __name__ == "__main__":
#     if len(sys.argv) != 2:
#        print("Incorrect number of arguments")
#        print("Correct usage: python Lab6.py <directory_path>")
#     else:
#         directory_path = sys.argv[1]
#         count_files_by_extension(directory_path)
