from bird_project import Bird, Eagle

class Owner:
    """
    Clase Owner: Representa a un dueño que puede tener múltiples animales (Bird u otros).
    """
    def __init__(self, name: str):
        self.name = name
        self.pets = []  # Lista para guardar los animales del dueño

    def add_pet(self, pet):
        """
        Agrega un animal a la lista de mascotas del dueño.
        """
        self.pets.append(pet)
        print(f"{self.name} ahora es dueño de {pet.name} ({pet.species}).")

    def feed_all(self):
        """
        Alimenta a todas las mascotas del dueño.
        """
        if not self.pets:
            print(f"{self.name} no tiene animales para alimentar.")
            return
        
        for pet in self.pets:
            print(f"{self.name} alimenta a {pet.name} ({pet.species}).")