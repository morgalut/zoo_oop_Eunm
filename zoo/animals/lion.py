from ..animal import Animal
from ..utils.constants import AnimalType, AnimalCategory
from ..utils.debug import Debug

class Lion(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, AnimalType.LION, AnimalCategory.MAMMAL)
    
    def make_sound(self):
        Debug.log(f"{self.name} the Lion roars")
        print(f"{self.name} the Lion roars")
    
    def move(self):
        Debug.log(f"{self.name} the Lion stalks its prey")
        print(f"{self.name} the Lion stalks its prey")
