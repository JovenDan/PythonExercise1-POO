"""
Este archivo define la clase Fish
"""

class Fish:
    def __init__(self, name: str, age: int, species: str):
        self.name = name
        self.age = age
        self.species = species
        print(f"Se ha creado un pez de especie {self.species} llamado {self.name} de {self.age} años.")
        
    def swim(self):
        print(f"{self.name} está nadando")
        
if __name__ == "__main__":
    fish1 = Fish("Marcos", 2, "Globo")
    fish2 = Fish("Polo", 4, "Gato")
    
    fish1.swim()
    fish2.swim()