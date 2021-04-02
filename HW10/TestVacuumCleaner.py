# Task1 Напишіть тести до класу робота пилососа приклад тестів:
# робот стартує з критичними значеннями заряду батареї, наповненості баку сміття і води
# добавте аргумент час роботи (кількість ітерацій головного циклу),
# протестує чи зможе робот з певними вхідними даними закінчити прибирання можете придумати свої тести
import VacuumCleaner as Vc
import unittest


class TestVacuumCleaner(unittest.TestCase):
    def setUp(self) -> None:
        self.params = [
            # charge, garbage_capacity, water_amount
            (15, 100, 0),
            ('22', 0, 20),
            (0, 0, 20),
            (-1, 100, -1),
            (20, 14, -1),
            (4, 2, 17),
            (30, 200, -100),
            (0, 100, 20),
            (20, 1000, 20),
            (100, 0, 100),
            (None, 0, 20),
            (12, 'a', 20)
        ]
        self.vacuum_cleaner_instances = [Vc.VacuumCleaner(charge, garbage_capacity, water_amount)
                                         for charge, garbage_capacity, water_amount in self.params]

        with self.assertRaises(NameError):
            self.vc_instance = Vc.VacuumCleaner(46, 11, a)
        with self.assertRaises(NameError):
            self.vc_instance = Vc.VacuumCleaner(a, 11, 46)
        with self.assertRaises(NameError):
            self.vc_instance = Vc.VacuumCleaner(46, a, 11)

    def test_move(self):
        for vacuum_cleaner_instance in self.vacuum_cleaner_instances:
            print(f'\n{"-" * 10}        Test{vacuum_cleaner_instance}{"-" * 10}')
            print(f'{vacuum_cleaner_instance} '
                  f' with charge = {vacuum_cleaner_instance.get_charge}'
                  f' with garbage_amount = {vacuum_cleaner_instance.get_garbage_capacity}'
                  f' with water_amount = {vacuum_cleaner_instance.get_water_amount}'
                  )
            vacuum_cleaner_instance.move(7)
            print(f'{"-" * 10}FinishedTest{vacuum_cleaner_instance}{"-" * 10}\n')




