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

    def test_vacuum_cleaner(self):

        # EmptyBatteryException
        with self.assertRaises(Vc.EmptyBatteryException):
            self.vc_instance = Vc.VacuumCleaner(0, 11, 40).vacuum_cleaner()
        with self.assertRaises(Vc.EmptyBatteryException):
            self.vc_instance = Vc.VacuumCleaner(-2, 11, 40).vacuum_cleaner()
        self.vc_instance_0 = Vc.VacuumCleaner(20, 14, 25)
        for i in range(20):
            self.vc_instance_0._charge -= i
        with self.assertRaises(Vc.EmptyBatteryException):
            self.vc_instance_0.vacuum_cleaner()

        # GarbageOverflowException
        with self.assertRaises(Vc.GarbageOverflowException):
            self.vc_instance = Vc.VacuumCleaner(50, 80, 40).vacuum_cleaner()
        with self.assertRaises(Vc.GarbageOverflowException):
            self.vc_instance = Vc.VacuumCleaner(50, 1000, 40).vacuum_cleaner()
        self.vc_instance_1 = Vc.VacuumCleaner(20, 60, 25)
        for i in range(21):
            self.vc_instance_1._garbage_capacity += i
        with self.assertRaises(Vc.GarbageOverflowException):
            self.vc_instance_1.vacuum_cleaner()

        # LowBatteryException
        self.vc_instance_2 = Vc.VacuumCleaner(10, 14, 25)
        for i in range(3):
            self.vc_instance_2._charge -= 3
        with self.assertRaises(Vc.LowBatteryException):
            self.vc_instance_2.vacuum_cleaner()

        self.vc_instance_3 = Vc.VacuumCleaner(20, 14, 25)
        for i in range(16):
            self.vc_instance_3._charge -= 1
        with self.assertRaises(Vc.LowBatteryException):
            self.vc_instance_3.vacuum_cleaner()

    def test_wash(self):
        with self.assertRaises(Vc.EmptyWaterAmountException):
            self.vc_instance = Vc.VacuumCleaner(10, 14, 0).wash()

        with self.assertRaises(Vc.EmptyWaterAmountException):
            self.vc_instance = Vc.VacuumCleaner(10, 14, -5).wash()

        self.vc_instance_4 = Vc.VacuumCleaner(20, 14, 10)
        for i in range(10):
            self.vc_instance_4._water_amount -= 1
        with self.assertRaises(Vc.EmptyWaterAmountException):
            self.vc_instance_4.wash()
