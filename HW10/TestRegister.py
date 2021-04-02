# Task2
# Напишіть тести до модуля реєстрації юзера (без фласк АРІ, просто окремий клас)
# тести повинні перевіряти чи відповідає пароль пошта і ім'я вимогам,
# перевіряти чи юзера з таким іменем не має в базі
# якщо юзер створений то назад отримуємо строку "200", інакше модуль реєстрації кидатиме ексепшини
# (ексепшини потрібно написати свої)
# тести до модуля авторизації юзера
# метод авторизації отримує пошту і пароль і звіряє чи є такі в базі данних (за бд можете використати словник)
# якщо дані введені вірно і юзер існує то назад повертаєтсья обєкт класу UserToken (майже пустий клас,
# містить тільки аргумент строку яка задається рандомним набором символів)
# Після написання тестів, реалізуйте ваші методи реєстрації і авторизаії
import Register as Rg
import unittest
import string

NOT_ALLOWED_SYMBOLS = ''.join(set(string.punctuation.__add__(' ')) - {'.', '_', '-', '@'})


class TestRegister(unittest.TestCase):

    def setUp(self) -> None:
        self.params = [
            # name, password, email
            ('Pasha223', 'DCQrZq_J223SwkL', 'Pasha2@gmail.com'),
            ('randomPeople223', 'randpassword', 'randwww@gmail.com')
        ]
        self.reg_instances = [Rg.Register(name, password, email)
                              for name, password, email in self.params]

    def test_init(self):
        with self.assertRaises(Rg.UserExistError):
            self.reg_instance_0 = Rg.Register('Pasha', 'DCQrZq_JUOSwkLDw', 'Pasha@gmail.com')
        with self.assertRaises(Rg.EmailIncorrect):
            self.reg_instance_1 = Rg.Register('Pasha', 'DCQrZq_w__incorrect__', 'Pasha_2@gma?il.com')
        with self.assertRaises(Rg.PasswordIncorrect):
            self.reg_instance_2 = Rg.Register('Pasha', '?///#^&__12', 'Pasha_2@gmail.com')
        with self.assertRaises(Rg.PasswordLengthError):
            self.reg_instance_3 = Rg.Register('Pasha', 'psaje', 'Pasha_2@gmail.com')

    def test_registration(self):
        for user_instance in self.reg_instances:
            user_instance.add_new_user()
            self.assertTrue(len(user_instance.get_password) > 0)
            print(f'{user_instance}')

