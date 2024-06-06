import argparse
from .animal import Animal
from .animals.lion import Lion
from .animals.elephant import Elephant
from .utils.debug import Debug
from .database.db_helper import DatabaseHelper

def main(debug, list_animals):
    Debug.enable_debug(debug)
    
    zoo_animals = [
        Lion(name="Simba", age=5),
        Elephant(name="Dumbo", age=10)
    ]

    db_helper = DatabaseHelper()
    db_helper.setup()

    for animal in zoo_animals:
        animal.make_sound()
        animal.move()
        db_helper.add_animal(animal)

    if list_animals:
        counts = db_helper.count_animal_categories()
        for category, count in counts.items():
            print(f"{category}: {count}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Zoo Management System")
    parser.add_argument('--debug', action='store_true', help="Enable debug mode")
    parser.add_argument('--list-animals', action='store_true', help="List animal counts by category")
    args = parser.parse_args()
    
    main(args.debug, args.list_animals)
