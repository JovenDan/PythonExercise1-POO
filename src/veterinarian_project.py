from dog_project import Dog

class Veterinarian:
    """
    Clase Veterinarian: Representa a un veterinario que hace chequeos a los animales.
    """
    def __init__(self, name: str):
        self.name = name

    def checkup(self, animal):
        """
        Realiza un chequeo al animal recibido.
        """
        print(f"El veterinario {self.name} está revisando a {animal.name}.")
        
vet = Veterinarian("Dr. López")
dog = Dog("Rex", 3)
vet.checkup(dog)