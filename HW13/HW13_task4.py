# 4. Divide the work between 2 methods: print_cube that returns the cube of number
# and print_square that returns the square of number. These two methods should be executed by using 2 different processes.
import multiprocessing as Mp


def cube(x):
    return x ** 3


def square(x):
    return x ** 2


if __name__ == '__main__':
    value = int(input('Please input your number: '))
    p_1 = Mp.Process(target=print(f'Cube is - {cube(value)}'))
    p_2 = Mp.Process(target=print(f'Square is - {square(value)}'))
    for x in p_1, p_2:
        x.start()
        x.join()
