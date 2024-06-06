from ..animal import Animal
from ..utils.constants import AnimalType, AnimalCategory
from ..utils.debug import Debug

class Elephant(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, AnimalType.ELEPHANT, AnimalCategory.MAMMAL)
    
    def make_sound(self):
        Debug.log(f"{self.name} the Elephant trumpets")
        print(f"{self.name} the Elephant trumpets")
    
    def move(self):
        Debug.log(f"{self.name} the Elephant lumbers along")
        print(f"{self.name} the Elephant lumbers along")
