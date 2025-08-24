"""
Proyecto: Ejemplo de herencia en POO con aves.
Este archivo define la clase Bird y la clase Eagle que hereda de Bird.
Incluye logging y comentarios explicativos sobre herencia.
"""
import logging

# Configuración básica del logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class Bird:
    """
    Clase base Bird representa el concepto general de un ave.
    En POO, una clase base puede ser heredada por otras clases más específicas.
    """
    def __init__(self, name: str, age: int, species: str):
        self.name = name
        self.age = age
        self.species = species
        logging.info(f"Se ha creado un ave de especie {self.species} llamada {self.name} de {self.age} años.")

    def sing(self):
        """
        Método que representa el canto del ave.
        """
        logging.info(f"{self.name} está cantando.")
        print(f"{self.name}: ¡Pío pío!")

    def birthday(self):
        """
        Aumenta la edad del ave en 1 año.
        """
        self.age += 1
        logging.info(f"{self.name} ahora tiene {self.age} años.")

    def migrate(self, destination: str):
        """
        Método que representa la migración del ave a otro lugar.
        """
        logging.info(f"{self.name} está migrando hacia {destination}.")
        print(f"{self.name} está migrando hacia {destination}.")


class Eagle(Bird):
    """
    Clase Eagle hereda de Bird.
    Ahora tiene un atributo extra 'altitude' que indica la altura de vuelo.
    """
    def __init__(self, name: str, age: int, altitude: int = 0):
        super().__init__(name, age, "Águila")
        self.altitude = altitude
        logging.info(f"Se ha creado un águila llamada {self.name} con altitud inicial de {self.altitude} metros.")

    def fly(self, increase: int = 10):
        """
        Aumenta la altitud de vuelo del águila.
        """
        self.altitude += increase
        logging.info(f"{self.name} está volando a {self.altitude} metros.")
        print(f"{self.name}: ¡Estoy volando a {self.altitude} metros!")

    def show_altitude(self):
        """
        Muestra la altitud actual de vuelo.
        """
        print(f"{self.name} está volando a {self.altitude} metros.")

if __name__ == "__main__":
    # Crear instancias de Bird y Eagle
    bird1 = Bird("Paco", 2, "Periquito")
    eagle1 = Eagle("Aquila", 5)

    # Llamar métodos de Bird
    bird1.sing()
    bird1.birthday()
    bird1.migrate("Sudamérica")

    # Llamar métodos de Eagle
    eagle1.sing()  # Método heredado de Bird
    eagle1.fly(50)
    eagle1.show_altitude()
    eagle1.birthday()