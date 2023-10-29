
#Ex1

# def list_to_set(a, b):
#     list_of_sets =[]
#     a = set(a)
#     b = set(b)
#     a_union_b = a.union(b)
#     a_intersection_b = a.intersection(b)
#     a_minus_b = a.difference(b)
#     b_minus_a = b.difference(a)
#     list_of_sets.append(a_union_b)
#     list_of_sets.append(a_intersection_b)
#     list_of_sets.append(a_minus_b)
#     list_of_sets.append(b_minus_a)
#     return list_of_sets
# a = [ 1 ,2 ,3 ,4 ,5]
# b = [ 4 , 5, 6, 7]
# print(list_to_set(a,b))

#Ex2

# def dict_keys (str):
#     dct = {}
#     for char in str:
#         dct[char] = str.count(char)
#     return dct
#
#
# str = "Ana has apples"
#
# print(dict_keys(str))

#Ex3

# def recursive_dict_compare(dict1, dict2):
#     if type(dict1) is not type(dict2):
#         return False
#
#     if isinstance(dict1, dict):
#         if set(dict1.keys()) != set(dict2.keys()):
#             return False
#
#         for key in dict1:
#             if not recursive_dict_compare(dict1[key], dict2[key]):
#                 return False
#
#     elif isinstance(dict1, (list, set, tuple)):
#         if len(dict1) != len(dict2):
#             return False
#
#         for item1, item2 in zip(sorted(dict1), sorted(dict2)):
#             if not recursive_dict_compare(item1, item2):
#                 return False
#
#     else:
#         if dict1 != dict2:
#             return False
#
#     return True
#
# # Test dictionaries
# dict1 = {
#     'A': 1,
#     'B': 2,
#     'C':3
# }
#
# dict2 = {
#     'A': 1,
#     'B': 2,
#     'C':3
# }
#
# dict3 = {
#     'A': 1,
#     'B': 2,
#     'C':4
# }
#
#
# result1 = recursive_dict_compare(dict1, dict2)
# result2 = recursive_dict_compare(dict1, dict3)
#
# print(result1)  # True
# print(result2)  # False

#Ex4

# def build_xml_element(tag, content, **kwargs):
#     attributes = " ".join(f'{key}="{value}"' for key, value in kwargs.items())
#     xml_element = f'<{tag} {attributes}>{content}</{tag}>'
#     return xml_element
#
# # Example usage:
# result = build_xml_element("a", "Hello there", href="http://python.org", _class="my-link", id="someid")
# print(result)

#Ex5

# def validate_dict(rules, dictionary):
#     for key, prefix, middle, suffix in rules:
#         if key in dictionary:
#             value = dictionary[key]
#             if not value.startswith(prefix) or not value.endswith(suffix) or middle not in value:
#                 return False
#
#     # Check if all keys in the dictionary are covered by the rules
#     if set(dictionary.keys()).issubset(set(key for key, _, _, _ in rules)):
#         return True
#
#     return False
#
# # Example usage:
# rules = [("key1", "", "inside", ""), ("key2", "start", "middle", "winter")]
# data = {"key1": "come inside, it's too cold out", "key3": "this is not valid"}
#
# result = validate_dict(rules, data)
# print(result)

#Ex6

# def count_unique_and_duplicates(lst):
#     unique_elements = set()
#     duplicate_elements = set()
#
#     for item in lst:
#
#         if item in unique_elements:
#             duplicate_elements.add(item)
#             unique_elements.remove(item)
#         else:
#             unique_elements.add(item)
#
#
#     return len(unique_elements), len(duplicate_elements)
#
#
# my_list = [1, 2, 2, 3, 4, 4, 5]
# unique_count, duplicate_count = count_unique_and_duplicates(my_list)
# print(f"Number of unique elements: {unique_count}")
# print(f"Number of duplicate elements: {duplicate_count}")

#Ex7
from itertools import combinations

# def set_operations(*args):
#     result_dict = {}
#
#     for set1, set2 in combinations(args, 2):
#
#         union_result = set1 | set2
#         intersection_result = set1 & set2
#         difference1_result = set1 - set2
#         difference2_result = set2 - set1
#
#         union_key = f"{set1} | {set2}"
#         intersection_key = f"{set1} & {set2}"
#         difference1_key = f"{set1} - {set2}"
#         difference2_key = f"{set2} - {set1}"
#
#         result_dict[union_key] = union_result
#         result_dict[intersection_key] = intersection_result
#         result_dict[difference1_key] = difference1_result
#         result_dict[difference2_key] = difference2_result
#
#     return result_dict
#
# set1 = {1, 2}
# set2 = {2, 3}
# result = set_operations(set1, set2)
#
# for key, value in result.items():
#     print(f"{key}: {value}")

# Ex8

# def loop(mapping):
#     visited = set()
#     result = []
#     current_key = 'start'
#
#     while current_key not in visited and current_key in mapping:
#         visited.add(current_key)
#         result.append(mapping[current_key])
#         current_key = mapping[current_key]
#
#     return result
#
# mapping = {'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}
# result = loop(mapping)
# print(result)

#Ex9
# def count_matching_args(*args, **key_value):
#     matching_count = 0
#
#     for arg in args:
#         if arg in key_value.values():
#             matching_count += 1
#
#     return matching_count
#
# result = count_matching_args(1, 2, 3, 4, x=1, y=2, z=3, w=5)
# print(result)

