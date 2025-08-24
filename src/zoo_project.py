"""
Este archivo define la clase Zoo
"""
from cat_project import Cat
from dog_project import Dog
from bird_project import Bird

class Zoo:
    def __init__(self):
        self.animals = []  # Lista vacía para animales
    
    def add_animal(self, animal):
        self.animals.append(animal)
    
    def show_animals(self):
        print("Animales en el zoológico:")
        for animal in self.animals:
            print("-", animal)


if __name__ == "__main__":
    
    cat1 = Cat("Michi")
    dog1 = Dog("Firulais")
    bird1 = Bird("Piolín")

    zoo = Zoo()

    zoo.add_animal(cat1)
    zoo.add_animal(dog1)
    zoo.add_animal(bird1)

    zoo.show_animals()