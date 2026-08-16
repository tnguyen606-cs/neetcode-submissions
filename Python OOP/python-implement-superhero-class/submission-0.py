class SuperHero:
    """
    A class to represent a superhero.

    Attributes:
        name (str): The superhero's name
        power (str): The superhero's main superpower
        health (int): The superhero's health points
    """

    def __init__(self, name: str, power: str, health: int):
        # TODO: Initialize the superhero's attributes here
        self.name = name
        self.power = power
        self.health = health


# TODO: Create Superhero instances
superHero1 = SuperHero("Batman", "Intelligence", 100)
superHero2 = SuperHero("Superman", "Strength", 150)

# TODO: Print out the attributes of each superhero
print(superHero1.name)
print(superHero1.power)
print(superHero1.health)
print(superHero2.name)
print(superHero2.power)
print(superHero2.health)
