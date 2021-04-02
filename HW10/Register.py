# from __future__ import annotations
import names
import random
import string


def password_generator(psw_lenght):
    allowed_char = string.ascii_letters + string.digits + '_.@-'
    return_value = ''
    for i in range(psw_lenght):
        return_value += random.choice(allowed_char)
    return return_value


def compare_strings(first_str: str, second_str: str) -> bool:
    """

    :param first_str:
    :param second_str:
    :return: return True if some letter in first_str is in second_str otherwise return False
    """

    return len(''.join(set(first_str).intersection(second_str))) > 0


class UserExistError(BaseException):
    pass


class EmailIncorrect(BaseException):
    pass


class PasswordIncorrect(BaseException):
    pass


class PasswordLengthError(BaseException):
    pass


NOT_ALLOWED_SYMBOLS = ''.join(set(string.punctuation.__add__('? ')) - {'.', '_', '-', '@'})
EMAILS = ('@gmail.com', '@yahoo.com', '@onmicrosoft.com', '@examplemail.com')
# print(string.ascii_letters + string.digits + '_.@-')

DATABASE_USERS_EMAILS = {
    x.replace(' ', '_') + random.choice(EMAILS): password_generator(random.randrange(6, 26)) for x in {names.get_full_name(random.choice(('male', 'female'))) for x in range(100)}
}
DATABASE_USERS_EMAILS['Pasha@gmail.com'] = 'DCQrZq_JUOSwkLDw'


class Register:
    def __init__(self, name, password, email):
        if self.user_exist_check(email) == '200':
            self._name = name
        if self.password_lenght_check(password):
            if self.password_correct_check(password):
                self._password = password
            else:
                raise PasswordIncorrect
        else:
            raise PasswordLengthError
        if self.email_correct_check(email):
            self._email = email
        else:
            raise EmailIncorrect

    def add_new_user(self):
        DATABASE_USERS_EMAILS[self._email] = self._password
        # print(f'user {self.get_name} created with password ({self.get_password}) and email ({self._email})')

    @property
    def get_name(self):
        return self._name

    @property
    def get_password(self):
        return self._password

    @staticmethod
    def password_lenght_check(pswd: str):
        return 25 >= len(pswd) >= 8

    @staticmethod
    def password_correct_check(pswd: str):
        return not compare_strings(pswd, NOT_ALLOWED_SYMBOLS)

    @staticmethod
    def email_correct_check(email: str):
        return not compare_strings(email, NOT_ALLOWED_SYMBOLS)

    @staticmethod
    def user_exist_check(user_name_email: str):
        if user_name_email in DATABASE_USERS_EMAILS.keys():
            raise UserExistError
        return '200'


# reg_instance_0 = Register('Pasha', 'DCQrZq_JUOSwkLDw', 'Pasha@gmail.com')
# reg_instance_1 = Register('Pasha', 'DCQrZq_w__inc', 'Pasha_2@gm?ail.com')
# reg_instance_2 = Register('Pasha', '?///#^&__12', 'Pasha_2@gmail.com')
# reg_instance_3 = Register('Pasha', 'psaje', 'Pasha_2@gmail.com')
