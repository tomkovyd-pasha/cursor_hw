import logging
import datetime as datetime


# context manager
class OpenFile:
    def __init__(self, file_name: str, mode: str):
        try:
            __tmp_file = open(file_name, 'r')
            self.__tmp_file_content = __tmp_file.read()
            __tmp_file.close()
        except FileNotFoundError:
            __tmp_file = open(file_name, 'w')
            __tmp_file.close()
        self.__tmp_filename = file_name
        self.file_obj = open(file_name, mode)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file_obj.close()
        if exc_type is None:
            return True
        tmp_file = open(self.__tmp_filename, 'w')
        tmp_file.write(self.__tmp_file_content + '\naa')
        tmp_file.close()
        return True

    def __enter__(self):
        return self.file_obj


with OpenFile('HW9.log', 'r') as file:
    file.read()


log_template = '%(asctime)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.DEBUG, filename='HW9.log', filemode='a', format=log_template)


operations = {'add': '+', 'subtract': '-', 'divide': '/',
              'multiply': '*', 'pow': '** n', 'root': '** (1/n)', 'percentage': '/ n * 100'}


def get_number_from_str(str_value):
    try:
        return float(int(str_value[:str_value.find(".")]) + int(str_value[str_value.find(".") + 1:]) * 0.1 ** (len(str_value) - str_value.find(".") - 1)) if '.' in str_value else int(str_value)
    except ValueError:
        logging.error(f'user failed data entry - {str_value}')
        return get_number_from_str(input('you input bad value, reinput value (must be int or float or str with base 10) '))


def get_operator_from_str(str_value):
    if str_value in operations:
        return operations.get(str_value)
    else:
        logging.error(f'user choose incorrect operator - {str_value}')
        return get_operator_from_str(input(
            f'you input bad value, reinput value from list ({"".join([str(x + ", ") for x in operations.keys()])[:-2]}) '))


def result_calc_value(first_value, second_value, __operator):
    try:
        return eval(f'({first_value}) {__operator.replace("n", str(second_value))}') if __operator in ('** n', '** (1/n)', '/ n * 100') else eval(f'({first_value}) {__operator} ({second_value})')
    except ZeroDivisionError:
        logging.error(f'user tried to divide by zero')
        return 0


def calc():
    logging.info(f'user try to insert first number')
    a = get_number_from_str(input('please input first value (must be int or float or str with base 10) '))
    logging.info(f'user inserted first number as "{a}"')
    logging.info(f'user try to insert second number')
    b = get_number_from_str(input('please input second value (must be int or float or str with base 10) '))
    logging.info(f'user inserted second number as "{b}"')
    c = get_operator_from_str(input(f'please input operator value from list ({"".join([str(x + ", ") for x in operations.keys()])[:-2]}) '))
    while c == '** (1/n)' and a < 0:
        logging.info(f'user select bad first value and operator. there is no root for negative numbers')
        a = get_number_from_str(input('please reinput first value (must be int or float or str with base 10 and greater than or equal 0, because operator - root) '))
    logging.info(f'user select operator as "{c}"')
    result = result_calc_value(a, b, c)
    logging.info(f'operation success, result = "{result}"')
    print(f'result = {result}')


while True:
    logging.info('user start calc program')
    calc()
    if input('once more? (yes/no)') == 'yes':
        logging.info('user want to start calc program once more')
        continue
    logging.info('user finished using calc program')
    break
