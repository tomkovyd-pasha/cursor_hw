# 1.
# class Laptop:
#     """
#     Make the class with composition.
#     """
# class Battery:
#     """
#     Make the class with composition.
#     """
import dataclasses
import collections


class Laptop:
    def __init__(self):
        self.battery = Battery(2600)

    def __str__(self):
        return f'laptop object - {self.__repr__()}'


class Battery:
    def __init__(self, capacity: int):
        """

        :param capacity: mAh
        """
        self.capacity = capacity

    def __str__(self):
        return f'battery object - {self.__repr__()}'


laptop_instance_0 = Laptop()
print(laptop_instance_0, laptop_instance_0.battery, sep='\n')
del laptop_instance_0
print('laptop_instance_0 deleted')

try:
    print(laptop_instance_0)
except NameError:
    print('laptop_instance_0 isn\'t exist')

try:
    print(laptop_instance_0.battery)
except NameError:
    print('laptop_instance_0.battery isn\'t exist')


# 2.
# class Guitar:
#     """
#     Make the class with aggregation
#     """
# class GuitarString:
#     """
#     Make the class with aggregation
#     """
class GuitarString:
    def __init__(self):
        pass

    def __str__(self):
        return f'guitar_string object - {self.__repr__()}'


class Guitar:
    def __init__(self, guitar_string: GuitarString):
        self.guitar_string = guitar_string

    def __str__(self):
        return f'guitar object - {self.__repr__()}'


guitar_string_instance_0 = GuitarString()
guitar_instance_0 = Guitar(guitar_string_instance_0)
print(guitar_instance_0, guitar_string_instance_0, sep='\n')

del guitar_instance_0

try:
    print(guitar_instance_0)
except NameError:
    print('guitar_instance_0 isn\'t exist')

try:
    print(guitar_string_instance_0)
except NameError:
    print('guitar_string_instance_0 isn\'t exist')


# 3
# class Calc:
#     """
#     Make class with one method "add_nums" with 3 parameters, which returns sum of these parameters.
#     Note: this method should not take instance as first parameter.
#     """
class Calc:

    @staticmethod
    def add_nums(first_arg, second_arg, third_arg):
        return sum((first_arg, second_arg, third_arg))


print(f'sum of {1, 5, 7} - {Calc.add_nums(1, 5, 7)}')


# 4*.
# class Pasta:
#     """
#     Make class which takes 1 parameter on init - list of ingredients and defines instance attribute ingredients.
#     It should have 2 methods:
#     carbonara (['forcemeat', 'tomatoes']) and bolognaise (['bacon', 'parmesan', 'eggs'])
#     which should create Pasta instances with predefined list of ingredients.
#     Example:
#         pasta_1 = Pasta(["tomato", "cucumber"])
#         pasta_1.ingredients will equal to ["tomato", "cucumber"]
#         pasta_2 = Pasta.bolognaise()
#         pasta_2.ingredients will equal to ['bacon', 'parmesan', 'eggs']
#     """
class Pasta:
    def __init__(self, ingredients: list):
        self.ingredients = ingredients

    @classmethod
    def carbonara(cls):
        """
        create Pasta object with ingredients from list - ['forcemeat', 'tomatoes']
        :return: Pasta object
        """
        return Pasta(['forcemeat', 'tomatoes'])

    @classmethod
    def bolognaise(cls):
        """
        create Pasta object with ingredients from list - ['bacon', 'parmesan', 'eggs']
        :return: Pasta object
        """
        return Pasta(['bacon', 'parmesan', 'eggs'])


pasta_1 = Pasta(["tomato", "cucumber"])
print(f'ingredients of pasta_1 - {pasta_1.ingredients}')  # will equal to ["tomato", "cucumber"]
pasta_2 = Pasta.bolognaise()
print(f'ingredients of pasta_2 - {pasta_2.ingredients}')  # will equal to ['bacon', 'parmesan', 'eggs']


# 5*.
# class Concert:
#     """
#     Make class, which has max_visitors_num attribute and its instances will have visitors_count attribute.
#     In case of setting visitors_count - max_visitors_num should be checked,
#     if visitors_count value is bigger than max_visitors_num - visitors_count should be assigned with max_visitors_num.
#     Example:
#         Concert.max_visitor_num = 50
#         concert = Concert()
#         concert.visitors_count = 1000
#         print(concert.visitors_count)  # 50
#     """
class Concert:
    max_visitors_num = 0

    def __init__(self):
        self._visitors_count = 0

    def set_visitors_count(self, visitors_count):
        self._visitors_count = visitors_count if visitors_count < self.max_visitors_num else self.max_visitors_num

    def get_visitors_count(self):
        return self._visitors_count

    visitors_count = property(fget=get_visitors_count, fset=set_visitors_count)


Concert.max_visitors_num = 50
concert = Concert()
concert.visitors_count = 1000
print(f'concert visitors - {concert.visitors_count}')  # 50


# 6.
# class AddressBookDataClass:
#     """
#     Create dataclass with 7 fields - key (int), name (str), phone_number (str), address (str), email (str),
#     birthday (str), age (int)
#     """
@dataclasses.dataclass()
class AddressBookDataClass:
    key: int
    name: str
    phone_number: str
    address: str
    email: str
    birthday: str
    age: int


address_book_instance_0 = AddressBookDataClass(key=0, name='Pasha', phone_number='354', address='Lviv',
                                               email='Pasha@354.com', birthday='1997-08-01', age=23)

# 7. Create the same class (6) but using NamedTuple
AddressBookDataClass_ = collections.namedtuple('AddressBookDataClass', ['key', 'name', 'phone_number', 'address',
                                                                        'email', 'birthday', 'age'])

address_book_instance_1 = AddressBookDataClass_(key=1, name='Pasha', phone_number='354', address='Lviv',
                                                email='Pasha@354.com', birthday='1997-08-01', age=23)

print(f'address_book_instance_0 (dataclass) - {address_book_instance_0}')
print(f'address_book_instance_1 (namedtuple) - {address_book_instance_1}')


# 8.
# class AddressBook:
#     """
#     Create regular class taking 7 params on init - key, name, phone_number, address, email, birthday, age
#     Make its str() representation the same as for AddressBookDataClass defined above.
#     """
class AddressBook:
    def __init__(self, key, name, phone_number, address, email, birthday, age):
        self.key = key
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age

    def __str__(self):
        return f'AddressBookDataClass(key={self.key}, name={self.name}, phone_number={self.phone_number}, ' \
                f'address={self.address}, email={self.email}, birthday={self.birthday}, age={self.age})'


address_book_instance_2 = AddressBook(key=2, name='Pasha', phone_number='354', address='Lviv',
                                      email='Pasha@354.com', birthday='1997-08-01', age=23)

print(f'address_book_instance_2 (regular class) - {address_book_instance_2}')


# 9.
# class Person:
#     """
#     Change the value of the age property of the person object
#     """
#     name = "John"
#     age = 36
#     country = "USA"
#
class Person:
    name = "John"
    age = 36
    country = "USA"


person_instance_0 = Person()
print(f'person_instance_0 age before change - {person_instance_0.age}')
person_instance_0.age += 1
print(f'person_instance_0 age after change - {person_instance_0.age}')


# 10.
# class Student:
#     """
#     Add an 'email' attribute of the object student and set its value
#     Assign the new attribute to 'student_email' variable and print it by using getattr
#     """
#     id = 0
#     name = ""
#
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name
class Student:
    student_id = 0
    name = ''

    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name


student_instance_0 = Student(1234, 'Pasha')
setattr(student_instance_0, 'email', f'{student_instance_0.name}{student_instance_0.student_id}' + '@university.com')
print(f'email of student {student_instance_0.name} (id - {student_instance_0.student_id}) - '
      f'{getattr(student_instance_0, "email")}')


# 11*.
# class Celsius:
#     """
#     By using @property convert the celsius to fahrenheit
#     Hint: (temperature * 1.8) + 32)
#     """
#     def __init__(self, temperature=0):
#         self._temperature = temperature
#
#
# # create an object
# {obj} = ...
#
# print({obj}.temperature)
class Celius:
    def __init__(self, temperature=0):
        self._temperature = temperature

    @property
    def temperature(self):
        return self._temperature * 1.8 + 32


temperature_instance_0 = Celius()
print(f'temperature - {temperature_instance_0.temperature}')
