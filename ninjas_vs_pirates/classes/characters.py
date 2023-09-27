class Character:
    def __init__( self , name, strength, speed):
        self.name = name
        self.strength = strength
        self.speed = speed
        self.health = 100

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

class Pirate (Character):
    def __init__( self , name, strength, speed):
        super().__init__( name, strength, speed)
        self.ship = "Black Pearl"

    def attack ( self , ninja ):
        ninja.health -= self.strength
        return self

class Ninja (Character):
    def __init__( self , name, strength, speed):
        super().__init__( name,  strength, speed)
        self.dojo = "NYC Sewers"

    def attack( self , pirate ):
        pirate.health -= self.strength
        return self