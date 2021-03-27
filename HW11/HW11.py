from functools import wraps


# 1. double_result
# This decorator function should return the result of another function multiplied by two
def double_result(func):
    @wraps(func)
    def inner(a, b):
        return func(a, b) * 2
    return inner


@double_result
def add_0(a, b):
    return a + b


print(add_0(5, 5))


# 2. only_odd_parameters
# This decorator function should only allow a function to have odd numbers as parameters,
# otherwise return the string "Please use only odd numbers!"
def only_odd_parameters(func):
    @wraps(func)
    def inner(*args, **kwargs):
        return func(*args) if all((x % 2 != 0 for x in args)) else 'Please use only odd numbers!'
        # return func(a, b) if all((a % 2 != 0, b % 2 != 0)) else 'Please use only odd numbers!'

    return inner


@only_odd_parameters
def add_1(a, b):
    return a + b


print(add_1(5, 5))
print(add_1(4, 4))


# add(5, 5)  # 10
# add(4, 4)  # "Please use only odd numbers!"


@only_odd_parameters
def multiply(a, b, c, d, e):
    return a * b * c * d * e


print(multiply(1, 2, 3, 4, 5))
print(multiply(1, 3, 5, 7, 9))


# 3.* logged
# Write a decorator which wraps functions to log function arguments and the return value on each call.
# Provide support for both positional and named arguments (your wrapper function should take both *args
# and **kwargs and print them both):


def logged(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(f'you called {func.__name__}({args}, {kwargs})\nIt returned {func(*args, **kwargs)}')
        return func(*args, **kwargs)
    return with_logging


@logged
def func(*args, **kwargs):
    return 3 + len(args) + len(kwargs)


func(1, 45, a=1, b=2, c=3)
func(4, 4, 4, a=25)
func(4, 4)
func(a=26)


# # 4. type_check
# # you should be able to pass 1 argument to decorator - type.
# # decorator should check if the input to the function is correct based on type.
# # If it is wrong, it should print(f"Wrong Type: {type}"), otherwise function should be executed.

def type_check(_type):
    def type_decorator(func):
        def inner(arg):
            return func(arg) if type(arg) == _type else f'Wrong type: {arg.__class__.__name__}'
        return inner
    return type_decorator


@type_check(int)
def times2(num):
    return num * 2


@type_check(str)
def first_letter(word):
    return word[0]


print(times2(2))
print(times2('Not A Number'))

print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
