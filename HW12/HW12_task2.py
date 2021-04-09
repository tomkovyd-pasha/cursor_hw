# 2. Create a script with arguments:
#
# source_file_path; required: true;
# start_salary; required: false; help: starting point of salary;
# end_salary; required: false; help: the max point of salary;
# position; required: false; help: position role
# age; required: false; help: Age of person
# language; required: false; help; Programming language
#
# Based on this info generate a new report of average salary.


# -ss 6000 -es 10000 --source_file_path D:\PythonProjects\Cursor\cursor_hw\HW12\2020_june_mini.csv
import argparse
import pandas as pd

parser = argparse.ArgumentParser(description='task 2 parser')
parser.add_argument('-sfp', '--source_file_path', required=True)
parser.add_argument('-ss', '--start_salary', required=False, help='starting point of salary')
parser.add_argument('-es', '--end_salary', required=False, help='the max point of salary')
parser.add_argument('-p', '--position', required=False, help='position role')
parser.add_argument('-a', '--age', required=False, help='Age of person')
parser.add_argument('-l', '--language', required=False, help='Programming language')

args = parser.parse_args()

query_string_start_salary = f'Зарплата_в_месяц >= {args.start_salary}' if args.start_salary is not None else None
query_string_end_salary = f'Зарплата_в_месяц <= {args.end_salary}' if args.end_salary is not None else None
query_string_position = f'Должность == "{args.position}"' if args.position is not None else None
query_string_age = f'Возраст == {args.age}' if args.age is not None else None
query_string_language = f'Язык.программирования == "{args.language}"' if args.position is not None else None

query_tuple = tuple(x for x in (query_string_start_salary, query_string_end_salary, query_string_position, query_string_age, query_string_language) if x is not None)
query_string = ' & '.join(query_tuple)
is_query_tuple_not_empty = len(query_tuple) > 0

data = pd.read_csv(args.source_file_path).query(query_string) if is_query_tuple_not_empty else pd.read_csv(args.source_file_path)

data_group_by_city = data.groupby('Город', as_index=False).agg(AverageSalary=pd.NamedAgg(column='Зарплата_в_месяц', aggfunc=lambda x: round(x.mean(), 2))).rename(columns={'Город': 'City'})
data_group_by_age = data.groupby('Возраст', as_index=False).agg(AverageSalary=pd.NamedAgg(column='Зарплата_в_месяц', aggfunc=lambda x: round(x.mean(), 2))).rename(columns={'Возраст': 'Age'})

for key, value in {'report_by_city.csv': data_group_by_city, 'report_by_age.csv': data_group_by_age}.items():
    with open(key, 'w', encoding='utf-8') as file_result:
        value.to_csv(file_result, index=False, line_terminator='\n')
