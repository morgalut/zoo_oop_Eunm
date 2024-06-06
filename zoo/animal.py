from .utils.constants import AnimalType, AnimalCategory
from .utils.debug import Debug

class Animal:
    def __init__(self, name, age, animal_type, category):
        self.name = name
        self.age = age
        self.animal_type = animal_type
        self.category = category
        Debug.log(f"Creating {self.animal_type.name} named {self.name}")

    def make_sound(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def move(self):
        raise NotImplementedError("Subclass must implement abstract method")
