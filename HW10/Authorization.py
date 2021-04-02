# from __future__ import annotations
import names
import random
import string
import uuid


def password_generator(psw_lenght):
    allowed_char = string.ascii_letters + string.digits + '_.@-'
    return_value = ''
    for i in range(psw_lenght):
        return_value += random.choice(allowed_char)
    return return_value


class EmailIncorrect(BaseException):
    pass


class PasswordIncorrect(BaseException):
    pass


EMAILS = ('@gmail.com', '@yahoo.com', '@onmicrosoft.com', '@examplemail.com')

DATABASE_USERS_EMAILS = {
    x.replace(' ', '_') + random.choice(EMAILS): password_generator(random.randrange(6, 26)) for x in {names.get_full_name(random.choice(('male', 'female'))) for x in range(100)}
}
DATABASE_USERS_EMAILS['Pasha@gmail.com'] = 'DCQrZq_JUOSwkLDw'
DATABASE_USERS_EMAILS['Pasha2@gmail.com'] = 'DCQrZq_JUOSwkLDw2'


class UserToken:
    def __init__(self, uu_id):
        self.uu_id = uu_id

    def __str__(self):
        return self.uu_id


class Authorization:
    def __init__(self, password, email):
        self._email = email
        self._password = password
        if self.user_email_exist_check(self.get_email):
            if self.password_correct_check(self.get_password):
                self.authorization_token = UserToken(uuid.uuid4())
            else:
                raise PasswordIncorrect
        else:
            raise EmailIncorrect

    @property
    def get_email(self):
        return self._email

    @property
    def get_password(self):
        return self._password

    @staticmethod
    def password_correct_check(pswd: str):
        return pswd in DATABASE_USERS_EMAILS.values()

    @staticmethod
    def user_email_exist_check(user_name_email: str):
        return user_name_email in DATABASE_USERS_EMAILS.keys()


# reg_instance_0 = Register('Pasha', 'DCQrZq_JUOSwkLDw', 'Pasha@gmail.com')
# reg_instance_1 = Register('Pasha', 'DCQrZq_w__inc', 'Pasha_2@gm?ail.com')
# reg_instance_2 = Register('Pasha', '?///#^&__12', 'Pasha_2@gmail.com')
# reg_instance_3 = Register('Pasha', 'psaje', 'Pasha_2@gmail.com')
