class Character:
    def __init__( self , name):
        self.name = name
        self.strength = 15
        self.speed = 3
        self.health = 100

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

class Pirate (Character):
    def __init__( self , name):
        super().__init__(name)
        self.ship = "Black Pearl"

    def attack ( self , ninja ):
        ninja.health -= self.strength
        return self

class Ninja (Character):
    def __init__( self , name):
        super().__init__(name)
        self.dojo = "NYC Sewers"

    def attack( self , pirate ):
        pirate.health -= self.strength
        return self

michelangelo = Ninja("Michelanglo")

jack_sparrow = Pirate("Jack Sparrow")

print(michelangelo)
print(jack_sparrow)