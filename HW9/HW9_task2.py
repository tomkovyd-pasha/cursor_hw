import time


class LowBatteryException(BaseException):
    pass


class EmptyBatteryException(BaseException):
    pass


class EmptyWaterAmountException(BaseException):
    pass


class GarbageOverflowException(BaseException):
    pass


class VacuumCleaner:
    def __init__(self, charge, garbage_capacity, water_amount):
        self.max_charge = charge
        # self.min_charge = 0
        self.max_garbage_capacity = 80
        # self.min_water_amount = 0
        self._charge = charge
        self._garbage_capacity = garbage_capacity
        self._water_amount = water_amount
        self.charge_reduce = 3
        self.water_amount_reduce = 3
        self.garbage_capacity_increase = 4

    def move(self):
        iter_for_end = 3
        while True:
            time.sleep(1)
            try:
                self.wash()
            except EmptyWaterAmountException as error:
                print('к-сть води = 0')
            except GarbageOverflowException as error:
                print('Почистіть мене')
            try:
                self.vacuum_cleaner()
            except LowBatteryException as error:
                iter_for_end -= 1
                print('заряд < 20%')
                if iter_for_end == 0:
                    break
            except EmptyBatteryException as error:
                print('Занесіть мене на зарядку')
            print('move')
            self._charge -= self.charge_reduce
            self._water_amount -= self.water_amount_reduce
            self._garbage_capacity += self.garbage_capacity_increase
            print(f'Заряд = {self._charge}, вода = {self._water_amount}, к-сть сміття = {self._garbage_capacity}')
            # print(self._charge, self._water_amount, self._garbage_capacity)
            # print(iter_for_end)

    def wash(self):
        if self._water_amount <= 0:
            raise EmptyWaterAmountException
        if self._garbage_capacity > self.max_garbage_capacity:
            raise GarbageOverflowException
        print('wash')

    def vacuum_cleaner(self):
        if self._charge < self.max_charge * 0.2:
            raise LowBatteryException
        if self._charge <= 0:
            raise EmptyBatteryException
        print('vacuum_cleaner')


a = VacuumCleaner(50, 0, 50)
a.move()
