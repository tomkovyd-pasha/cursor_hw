# 1. Create a Vehicle class with max_speed and mileage instance attributes
class Vehicle:
    def __init__(self, max_speed, mileage):
        """

        :param max_speed: kilometers per hour
        :param mileage: kilometers
        """
        self.max_speed = max_speed
        self.mileage = mileage


# 2. Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
# and will have seating_capacity own method
class Bus(Vehicle):
    def __init__(self, max_speed, mileage, seating_capacity):
        self.__seating_capacity = seating_capacity
        Vehicle.__init__(self, max_speed, mileage)

    def seating_capacity(self):
        return self.__seating_capacity

# 3. Determine which class a given Bus object belongs to (Check type of an object)
School_bus = Bus(160, 100000, 40)
print(f'type of School_bus object - {type(School_bus)}')
print(f'seating capacity of School_bus - {School_bus.seating_capacity()}')


# 4. Determine if School_bus is also an instance of the Vehicle class
print(f'is School_bus is an instance of Vehicle class - {isinstance(School_bus, Vehicle)}')


# 5. Create a new class School with get_school_id and number_of_students instance attributes
class School:
    def __init__(self, school_id, number_of_student):
        self.__school_id = school_id
        self.number_of_student = number_of_student

    def get_school_id(self):
        return self.__school_id


example_school_instance = School(1, 2)
print(f'school_id of example_school_instance object - {example_school_instance.get_school_id()}')


# 6*. Create a new class SchoolBus that will inherit all of the methods from School
# and Bus and will have its own - bus_school_color
class SchoolBus(School, Bus):
    def __init__(self, school_id, number_of_student, max_speed, mileage, seating_capacity, bus_school_color):
        self.bus_school_color = bus_school_color
        School.__init__(self, school_id, number_of_student)
        Bus.__init__(self, max_speed, mileage, seating_capacity)


# 7. Polymorphism: Create two classes: Bear, Wolf.
# Both of them should have make_sound method. Create two instances, one of Bear and one of Wolf,
# make a tuple of it and by using for call their action using the same method.
class Bear:
    def make_sound(self):
        return 'Bear say - aaa'


class Wolf:
    def make_sound(self):
        return 'Wolf say - auf'


wolf_instance = Wolf()
bear_instance = Bear()

animals = (wolf_instance, bear_instance)


def zoo(animals_set: tuple):
    for i in animals_set:
        print(i.make_sound())


zoo(animals)


# Magic methods:
# 8. Create class City with name, population instance attributes, return a new instance only when population > 1500,
# otherwise return message: "Your city is too small".
# 9. Override a printable string representation of the City class and return:
# The population of the city {name} is {population}
class City:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __new__(cls, name, population):
        instance = object.__new__(cls)
        return instance if  population > 1500 else f'Your city ({name}) is too small'

    def __str__(self):
        return f'The population of the city {self.name} is {self.population}'



city_instance_0 = City('City_0', 200)
city_instance_1 = City('City_1', 1501)

print(city_instance_1)


# 10*. Override magic method __add__() to perform the additional action
# as 'multiply' (*) the value which is greater than 10.
# And perform this add (+) of two instances.
class Example_add:
    def __init__(self, value):
        self.value = value
    

    def __add__(self, another_instance):
        return self.value * another_instance.value if any((self.value > 10, another_instance.value > 10)) else self.value + another_instance.value 


Example_add_instance_0 = Example_add(3)
Example_add_instance_1 = Example_add(4)
Example_add_instance_2 = Example_add(12)
print(f'{Example_add_instance_0.value} + {Example_add_instance_1.value} = {Example_add_instance_0 + Example_add_instance_1}')
print(f'{Example_add_instance_0.value} + {Example_add_instance_2.value} = {Example_add_instance_0 + Example_add_instance_2}')
print(f'{Example_add_instance_1.value} + {Example_add_instance_2.value} = {Example_add_instance_1 + Example_add_instance_2}')


# 11. The __call__ method enables Python programmers to write classes where the instances behave like functions
# and can be called like a function.
# Create a new class with __call__ method and define this call to return sum.
class Callable:
    def __init__(self, *args):
        self.sum = sum(*args)

    def __call__(self):
        return self.sum


callable_object_instance = Callable((10, 20, 30))
print(callable_object_instance())


# 12*. Making Your Objects Truthy or Falsey Using __bool__().
# Create class MyOrder with cart and customer instance attributes.
# Override the __bool__magic method considered to be truthy if the length of the cart list is non-zero.
# e.g.:
# order_1 = MyOrder(['a', 'b', 'c'], 'd')
# order_2 = MyOrder([], 'a')
# bool(order_1)
# True
# bool(order_2)
# False
class MyOrder:
    def __init__(self, cart: list, customer: str):
        self.cart = cart
        self.customer = customer

    def __bool__(self):
        return len(self.cart) > 0


order_1 = MyOrder(['a', 'b', 'c'], 'd')
order_2 = MyOrder([], 'a')

print(bool(order_1))
print(bool(order_2))
