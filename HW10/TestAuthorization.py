import Authorization as Au
import unittest
import string


class TestAuthorization(unittest.TestCase):

    def setUp(self) -> None:
        self.params = [
            # password, email
            ('DCQrZq_JUOSwkLDw', 'Pasha@gmail.com'),
            ('DCQrZq_JUOSwkLDw2', 'Pasha2@gmail.com')
        ]
        self.auth_instances = [Au.Authorization(password, email)
                               for password, email in self.params]

    def test_init(self):
        with self.assertRaises(Au.EmailIncorrect):
            self.reg_instance_1 = Au.Authorization('DCQrZq_JUOSwkLDw', 'Pasha_333@gmail.com')
        with self.assertRaises(Au.PasswordIncorrect):
            self.reg_instance_2 = Au.Authorization('DCQrZq_JUOSwkLDw2_333', 'Pasha2@gmail.com')

    def test_authorization(self):
        for user_instance in self.auth_instances:
            self.assertTrue(user_instance.authorization_token is not None)
            print(f'token for {user_instance} exist')
