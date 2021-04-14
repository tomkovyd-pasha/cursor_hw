# 3. Use Pool.apply() to get the row wise common items in list_a and list_b.
# list_a = [[1, 2, 3], [5, 6, 7, 8], [10, 11, 12], [20, 21]]
# list_b = [[2, 3, 4, 5], [6, 9, 10], [11, 12, 13, 14], [21, 24, 25]]


import multiprocessing


list_a = [[1, 2, 3], [5, 6, 7, 8], [10, 11, 12], [20, 21]]
list_b = [[2, 3, 4, 5], [6, 9, 10], [11, 12, 13, 14], [21, 24, 25]]


def get_common(l1, l2):
    return list(map(lambda x, y: set(x).intersection(y), l1, l2))


if __name__ == '__main__':
    with multiprocessing.Pool(2) as pool:
        list_of_common_items = pool.apply(get_common, args=(list_a, list_b))
        print(list_of_common_items)
