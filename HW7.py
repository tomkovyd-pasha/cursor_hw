import pickle
from statistics import mean


with open('task1.txt', 'r') as task_1_file:
    task_1_file_content = task_1_file.readlines()

lst_keys = list(map(lambda y: y.replace('\n', ''), [x for x in task_1_file_content if task_1_file_content.index(x) % 2 == 0]))
lst_values = list(map(lambda y: y.replace('\n', ''), [x for x in task_1_file_content if task_1_file_content.index(x) % 2 != 0]))
task_1_dict = dict(zip(lst_keys, lst_values))

print(task_1_dict)


def create_str_from_list(lst_to_str: list) -> str:
    """
    create and return string, which return all values from list
    :param lst_to_str: must be list type
    :return: return str
    """
    return ''.join(map(lambda x: ' ' + x, lst_to_str)).strip()


with open('task_1_result.txt', 'w') as task_1_result_file:
    task_1_result_file.write(create_str_from_list(lst_values))


# 2
with open('task2', 'rb') as task_2_file:
    task_2_file_content = pickle.load(task_2_file)
    print(f'Average of task2 file values - {round(mean(task_2_file_content), 2)}')



