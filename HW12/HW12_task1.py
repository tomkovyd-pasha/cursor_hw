# In the homework directory you can find the directory arg_parser_homework where you can find 2020_june_mini.csv file.
#
# 1. Create a script with arguments:
#
# exp; required: false; default: min(exp)
# current_job_exp; required: false; default: max(current_job_exp)
# sex; required: false
# city; required: false
# position; required: false
# age; required: false
# path_to_source_files; required: true;
# destination_path; required: false; default: .
# destination_filename; required: false; default: f"2020_june_mini.csv".
# The script should read the .csv file and get the information based on your input and generate a new .csv
# file with that info
#
# Example of input:
# --exp 3 --sex female --position DevOps --city Kyiv --path_to_source_files . ...


# --exp 3 --sex female --position DevOps --city Kyiv --path_to_source_files D:\PythonProjects\Cursor\cursor_hw\HW12\2020_june_mini.csv
import argparse
import os
import pandas as pd

DEFAULT_SOURCE_DIR_PATH = os.path.dirname(os.path.realpath(__file__)) + '\\'
DEFAULT_SOURCE_FILE_NAME = '2020_june_mini.csv'
DEFAULT_RESULT_FILE_NAME = '2020_june_mini_result.csv'
MIN_EXP = min(pd.read_csv(DEFAULT_SOURCE_DIR_PATH + DEFAULT_SOURCE_FILE_NAME)['exp'])
MAX_CURRENT_JOB_EXP = max(pd.read_csv(DEFAULT_SOURCE_DIR_PATH + DEFAULT_SOURCE_FILE_NAME)['current_job_exp'])

parser = argparse.ArgumentParser(description='task 1 parser')
parser.add_argument('-e', '--exp', default=MIN_EXP)
parser.add_argument('-cj', '--current_job_exp', required=False, default=MAX_CURRENT_JOB_EXP)
parser.add_argument('-s', '--sex', required=False)
parser.add_argument('-c', '--city', required=False)
parser.add_argument('-p', '--position', required=False)
parser.add_argument('-a', '--age', required=False)
parser.add_argument('-pth', '--path_to_source_files', required=True)
parser.add_argument('-dpth', '--destination_path', required=False, default=DEFAULT_SOURCE_DIR_PATH)
parser.add_argument('-df', '--destination_filename', required=False, default=DEFAULT_RESULT_FILE_NAME)

args = parser.parse_args()
args_dict = args.__dict__
conformity_dict = {
    'exp': 'exp',
    'current_job_exp': 'current_job_exp',
    'sex': 'Пол',
    'city': 'Город',
    'position': 'Должность',
    'age': 'Возраст'
}
args_dict_filtered = {x: f'"{y}"' if isinstance(y, str) else y for x, y in args_dict.items() if x not in ('path_to_source_files', 'destination_path', 'destination_filename') and y is not None}
query_list = [f'{conformity_dict[x]} == {y}' for x, y in args_dict_filtered.items()]

data = pd.read_csv(args.path_to_source_files).query(' | '.join(query_list))

with open(args.destination_path + args.destination_filename, 'w', encoding='utf-8') as file_result:
    data.to_csv(file_result, index=False, line_terminator='\n')
