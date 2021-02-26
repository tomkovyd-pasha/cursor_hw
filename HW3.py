# 1. Define the id of next variables:
#
# int_a = 55
# str_b = 'cursor'
# set_c = {1, 2, 3}
# lst_d = [1, 2, 3]
# dict_e = {'a': 1, 'b': 2, 'c': 3}
# import inspect
#

import inspect


def retrieve_name(var):  # класна штука, яку знайшов в інтернетах :)
    callers_local_vars = inspect.currentframe().f_back.f_locals.items()
    return [var_name for var_name, var_val in callers_local_vars if var_val is var]


int_a, str_b, set_c, lst_d, dict_e = 55, 'cursor', {1, 2, 3}, [1, 2, 3], {'a': 1, 'b': 2, 'c': 3}
first_example = [int_a, str_b, set_c, lst_d, dict_e]

for first_example_variables in first_example:
    print(f'id of variable {retrieve_name(first_example_variables)[0].__repr__()} = {id(first_example_variables)}')
