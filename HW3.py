# 1. Define the id of next variables:
#
# int_a = 55
# str_b = 'cursor'
# set_c = {1, 2, 3}
# lst_d = [1, 2, 3]
# dict_e = {'a': 1, 'b': 2, 'c': 3}
# import inspect


import inspect
import functools


def retrieve_name(var):  # класна штука, яку знайшов в інтернетах :)
    callers_local_vars = inspect.currentframe().f_back.f_locals.items()
    return [var_name for var_name, var_val in callers_local_vars if var_val is var]


int_a, str_b, set_c, lst_d, dict_e = 55, 'cursor', {1, 2, 3}, [1, 2, 3], {'a': 1, 'b': 2, 'c': 3}
list_for_example = [int_a, str_b, set_c, lst_d, dict_e]

for first_example_variables in list_for_example:
    print(f'id of variable {retrieve_name(first_example_variables)[0].__repr__()} = {id(first_example_variables)}')

# 2. Append 4 and 5 to the lst_d and define the id one more time.

lst_d.extend([4, 5])
print(f'id of lst_d = {id(lst_d)}')

# 3. Define the type of each object from step 1.
for third_example_variables in list_for_example:
    print(f'type of variable {retrieve_name(third_example_variables)[0].__repr__()} = {type(third_example_variables)}')

# 4*. Check the type of the objects by using isinstance.
print(
    f'is type of int_a = int - {isinstance(int_a, int)}'
    , f'is type of str_b = str - {isinstance(str_b, str)}'
    , f'is type of set_c = set - {isinstance(set_c, set)}'
    , f'is type of lst_d = lst - {isinstance(lst_d, list)}'
    , f'is type of dict_e = dict - {isinstance(dict_e, dict)}'
    , sep='\n'
)

# String formatting:
# Replace the placeholders with a value:
# "Anna has ___ apples and ___ peaches."

apples_count = 5
peaches_count = 8

# 5. With .format and curly braces {}
print('Anna has {} apples and {} peaches.'.format(apples_count, peaches_count))

# 6. By passing index numbers into the curly braces.
print('Anna has {1} apples and {0} peaches.'.format(peaches_count, apples_count))

# 7. By using keyword arguments into the curly braces.
print('Anna has {apples} apples and {peaches} peaches.'.format(apples=apples_count, peaches=peaches_count))

# 8*. With indicators of field size (5 chars for the first and 3 for the second)
print('Anna has {0:5} apples and {0:3} peaches.'.format(peaches_count, apples_count))

# 9. With f-strings and variables
print(f'Anna has {apples_count} apples and {peaches_count} peaches.')

# 10. With % operator
print('Anna has %s apples and %s peaches.' % (apples_count, peaches_count))

# 11*. With variable substitutions by name (hint: by using dict)
apples_peaches_dict = {'apples': apples_count, 'peaches': peaches_count}
print('Anna has %(apples)s apples and %(peaches)s peaches.' % apples_peaches_dict)

# Comprehensions:
# (1)
# lst = []
# for num in range(10):
#     if num % 2 == 1:
#         lst.append(num ** 2)
#     else:
#         lst.append(num ** 4)
# print(lst)
#
# (2)
# list_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]
#
# 12. Convert (1) to list comprehension
comprehension_list_from_regular = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]
print(f'comprehension_list_from_regular = {comprehension_list_from_regular}')

# 13. Convert (2) to regular for with if-else
regular_list_from_comprehension = []
for num in range(10):
    if num % 2 == 0:
        regular_list_from_comprehension.append(num // 2)
    else:
        regular_list_from_comprehension.append(num * 10)
print(f'regular_list_from_comprehension = {regular_list_from_comprehension}')

# (3)
# d = {}
# for num in range(1, 11):
#     if num % 2 == 1:
#         d[num] = num ** 2
# print(d)
#
# (4)
# d = {}
# for num in range(1, 11):
#     if num % 2 == 1:
#         d[num] = num ** 2
#     else:
#         d[num] = num // 0.5
# print(d)
#
# (5)
# dict_comprehension = {x: x**3 for x in range(10) if x**3 % 4 == 0}
#
# (6)
# dict_comprehension = {x: x**3 if x**3 % 4 == 0 else x for x in range(10)}
#
# 14. Convert (3) to dict comprehension.
first_comprehension_dict_from_regular = {num: num ** 2 for num in range(1, 11) if num % 2 == 1}
print(f'first_comprehension_dict_from_regular = {first_comprehension_dict_from_regular}')

# 15*. Convert (4) to dict comprehension.
second_comprehension_dict_from_regular = {num: num ** 2 if num % 2 == 1 else num // 0.5 for num in range(1, 11)}
print(f'second_comprehension_dict_from_regular = {second_comprehension_dict_from_regular}')

# 16. Convert (5) to regular for with if.
first_regular_dict_from_comprehension = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        first_regular_dict_from_comprehension[x] = x ** 3
print(f'first_regular_dict_from_comprehension = {first_regular_dict_from_comprehension}')

# 17*. Convert (6) to regular for with if-else.
second_regular_dict_from_comprehension = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        second_regular_dict_from_comprehension[x] = x ** 3
    else:
        second_regular_dict_from_comprehension[x] = x
print(f'second_regular_dict_from_comprehension = {second_regular_dict_from_comprehension}')

# Lambda:
#
# (7)
# def foo(x, y):
#     if x < y:
#         return x
#     else:
#         return y
#
# (8)
# foo = lambda x, y, z: z if y < x and x > z else y
#
# 18. Convert (7) to lambda function
foo = lambda x, y: x if x < y else y
print(f'lambda function from def = {foo(2, 10)}')

# 19*. Convert (8) to regular function


def def_from_foo(x, y, z):
    if y < x > z:
        return z
    else:
        return y


print(f'def from lambda function = {def_from_foo(4, 7, 5)}')

lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
# 20. Sort lst_to_sort from min to max
lst_to_sort.sort()
print(f'sorted list from min to max = {lst_to_sort}')

# 21. Sort lst_to_sort from max to min
lst_to_sort.sort(reverse=True)
print(f'sorted list from max to min = {lst_to_sort}')

# 22. Use map and lambda to update the lst_to_sort by multiply each element by 2
lst_to_sort = list(map(lambda x: x * 2, lst_to_sort))
print(f'updated list by multiplied each element by 2 = {lst_to_sort}')

# 23*. Raise each list number to the corresponding number on another list:
list_A = [2, 3, 4]
list_B = [5, 6, 7]
list_C = list(map(lambda x, y: x * y, list_A, list_B))
print(f'raised each list number by corresponding Number on another list = {list_C}')

# 24. Use reduce and lambda to compute the numbers of a lst_to_sort.
sum_of_lst_to_sort_values = functools.reduce(lambda x, y: x + y, lst_to_sort)
print(f'sum of all lst_to_sort values = {sum_of_lst_to_sort_values}')

# 25. Use filter and lambda to filter the number of a lst_to_sort with elem % 2 == 1.
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]  # в мене цей список змінювався, тому добавляю ще раз
lst_to_sort_with_only_odd_numbers = list(filter(lambda x: x % 2 == 1, lst_to_sort))
print(f'only odd numbers in lst_to_sort = {lst_to_sort_with_only_odd_numbers}')

# 26. Considering the range of values: b = range(-10, 10), use the function filter to return only negative numbers.
list_of_only_negative_numbers = list(filter(lambda x: x < 0, range(-10, 10)))
print(f'only negative numbers in range(-10, 10) = {list_of_only_negative_numbers}')

# 27*. Using the filter function, find the values that are common to the two lists:
list_1 = [1, 2, 3, 5, 7, 9]
list_2 = [2, 3, 5, 6, 7, 8]
list_of_common_values = list(filter(lambda x: x in list_1, list_2))
print(f'the values that are common to the two lists = {list_of_common_values}')


