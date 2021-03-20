from __future__ import annotations
import random
import uuid
from abc import ABC, abstractmethod
from typing import Dict, Any
import time


class Animals(ABC):
    @abstractmethod
    def __init__(self, power: int, speed: int):
        self._id = uuid.uuid4()
        self._max_power = power
        self._current_power = power
        self._speed = speed

    @abstractmethod
    def eat(self, forest: Forest):
        raise NotImplementedError


class Predators(Animals):
    def __init__(self, power: int, speed: int):
        Animals.__init__(self, power, speed)

    def eat(self, forest: Forest):
        random_animal = forest[random.choice(range(0, len(forest.animals)))]
        print(f'random animal selected by predator {self}')
        if len(forest.animals) == 1:
            forest.remove_animal(self)  # last predator dies because no food exist
        elif random_animal.id == self.id:
            print(f'predator pulled himself out')
            return
        elif all((self.speed > random_animal.speed, self.current_power > random_animal.current_power)):
            self.current_power = self.current_power + self.max_power * 0.5
            print(f'random animal eaten by {self}')
            forest.remove_animal(random_animal)
            return
        self.current_power = self.current_power - self.max_power * 0.3
        random_animal.current_power = random_animal.current_power - self.max_power * 0.3
        print(f'predator failed hunting, power of {self} - {self.current_power}')

    def set_current_power(self, current_power):
        set_value = min(self.max_power, current_power)
        self._current_power = set_value if set_value > 0 else 0

    def get_current_power(self):
        return self._current_power

    current_power = property(fget=get_current_power, fset=set_current_power)

    def set_speed(self, speed):
        self._speed = speed

    def get_speed(self):
        return self._speed

    speed = property(fget=get_speed, fset=set_speed)

    def get_max_power(self):
        return self._max_power

    max_power = property(fget=get_max_power)

    def get_id(self):
        return self._id

    id = property(fget=get_id)

    def __str__(self):
        return f'predator_instance_{self.id}'

    def __repr__(self):
        return f'Predators(power={self.current_power}, speed={self.speed})'


class Herbivores(Animals):
    def __init__(self, power: int, speed: int):
        Animals.__init__(self, power, speed)

    def eat(self, forest: Forest):
        self.current_power = self.current_power + self.max_power * 0.5

    def set_current_power(self, current_power):
        set_value = min(self.max_power, current_power)
        self._current_power = set_value if set_value > 0 else 0

    def get_current_power(self):
        return self._current_power

    current_power = property(fget=get_current_power, fset=set_current_power)

    def set_speed(self, speed):
        self._speed = speed

    def get_speed(self):
        return self._speed

    speed = property(fget=get_speed, fset=set_speed)

    def get_max_power(self):
        return self._max_power

    max_power = property(fget=get_max_power)

    def get_id(self):
        return self._id

    id = property(fget=get_id)

    def __str__(self):
        return f'herbivore_instance_{self.id}'

    def __repr__(self):
        return f'Herbivores(power={self.current_power}, speed={self.speed})'


AnyAnimal: Any[Herbivores, Predators]


class Forest:
    def __init__(self):
        self.animals: Dict[str, AnyAnimal] = dict()
        self.number: int = -1
        self.count_animals = 0

    def add_animal(self, animal: AnyAnimal):
        self.animals.update({str(animal): animal})

    # def __iter__(self):
    #     return self

    def __getitem__(self, item):
        return self.animals[list(self.animals.keys())[item]]

    # def __next__(self):
    #     self.number += 1
    #     # if self.number < 10:
    #     #     self.number += 1
    #     # else:
    #     #     self.number = -1
    #     if self.number <= len(self.animals) - 1:
    #         return self.animals[list(self.animals.keys())[self.number]]
    #         # return list(self.animals.keys())[self.number]
    #     raise StopIteration

    def remove_animal(self, animal: AnyAnimal):
        for key, val in self.animals.items():
            if val == animal:
                print(f'{val} deleted')
                self.animals.pop(key)
                # del self.animals[key]
                break

    def any_predator_left(self):
        return any(isinstance(x, Predators) for x in self.animals.values())


def animal_generator():
    while True:
        animal_object = random.choice(
            (
                Herbivores(random.randrange(25, 100), random.randrange(25, 100)),
                Predators(random.randrange(25, 100), random.randrange(25, 100))
            )
        )
        yield animal_object


nature = animal_generator()
forest = Forest()
for i in range(10):
    animal = next(nature)
    forest.add_animal(animal)


while True:
    if not forest.any_predator_left():
        print('game end')
        break

    for animal in forest:
        if isinstance(animal, Predators):
            print(f'{animal} selected')
        animal.eat(forest=forest)
    for animal in forest:
        if animal.current_power == 0:
            print(f'{animal} died because power = {animal.current_power}')
            forest.remove_animal(animal)

    print(f'count of predators - {len(list(x for x in forest.animals.values() if isinstance(x, Predators)))}')
    print(forest.animals)
    time.sleep(1)

