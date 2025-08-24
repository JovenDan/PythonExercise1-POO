from bird_project import Bird

class Parrot(Bird):
    def __init__(self, name):
        super().__init__(name)

    def talk(self, phrase):
        print(f"{self.name} dice: '{phrase}'")


if __name__ == "__main__":

    parrot1 = Parrot("Loro Pepe")

    parrot1.talk("¡Hola, humano!") 