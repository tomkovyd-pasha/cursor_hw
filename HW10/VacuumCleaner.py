import time


class LowBatteryException(BaseException):
    pass


class EmptyBatteryException(BaseException):
    pass


class EmptyWaterAmountException(BaseException):
    pass


class GarbageOverflowException(BaseException):
    pass


def get_number_from_str(str_value):
    try:
        return float(int(str_value[:str_value.find(".")]) + int(str_value[str_value.find(".") + 1:]) * 0.1 ** (
                    len(str_value) - str_value.find(".") - 1)) if '.' in str_value else int(str_value)
    except ValueError:
        return 0
    except TypeError:
        return 0


class VacuumCleaner:
    def __init__(self, charge, garbage_capacity, water_amount):
        self.max_charge = 100
        # self.min_charge = 0
        self.max_garbage_capacity = 80
        # self.min_water_amount = 0
        self._charge = float(charge) if isinstance(charge, (int, float)) else get_number_from_str(charge)
        self._garbage_capacity = float(garbage_capacity) if isinstance(garbage_capacity, (int, float)) else get_number_from_str(garbage_capacity)
        self._water_amount = float(water_amount) if isinstance(water_amount, (int, float)) else get_number_from_str(water_amount)
        self.charge_reduce = 3
        self.water_amount_reduce = 3
        self.garbage_capacity_increase = 4

    @property
    def get_charge(self):
        return self._charge

    @property
    def get_garbage_capacity(self):
        return self._garbage_capacity

    @property
    def get_water_amount(self):
        return self._water_amount

    def move(self, count_iters: int=None):
        iter_for_end = 3
        while True:
            time.sleep(1)
            try:
                self.vacuum_cleaner()
            except LowBatteryException as error:
                iter_for_end -= 1
                print('заряд < 20%')
                if iter_for_end == 0:
                    print('Занесіть мене на зарядку')
                    break
            except EmptyBatteryException as error:
                print('Занесіть мене на зарядку')
                break
            except GarbageOverflowException as error:
                print('Почистіть мене')
                break
            try:
                self.wash()
            except EmptyWaterAmountException as error:
                print('к-сть води = 0')
            print('move')
            self._charge = max(self._charge - self.charge_reduce, 0)  # if self._charge - self.charge_reduce > 0 else 0
            self._water_amount = max(self._water_amount - self.water_amount_reduce, 0)  # if self._water_amount - self.water_amount_reduce > 0 else 0
            self._garbage_capacity = min(self._garbage_capacity + self.garbage_capacity_increase, self.max_garbage_capacity)
            print(f'Заряд = {self._charge}, вода = {self._water_amount}, к-сть сміття = {self._garbage_capacity}')
            # print(self._charge, self._water_amount, self._garbage_capacity)
            # print(iter_for_end)
            if count_iters is not None:
                if count_iters > 1:
                    count_iters -= 1
                else:
                    print('cleaning finished because it was last iteration')
                    break

    def wash(self):
        if self._water_amount <= 0:
            raise EmptyWaterAmountException
        print('wash')

    def vacuum_cleaner(self):
        if self._charge > 0:
            print('vacuum_cleaner')
        else:
            raise EmptyBatteryException
        if self._garbage_capacity >= self.max_garbage_capacity:
            raise GarbageOverflowException
        if self._charge < self.max_charge * 0.2:
            raise LowBatteryException


# a = VacuumCleaner('a', 0, 20)
# a.move()
