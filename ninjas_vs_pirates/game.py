# from classes.ninja import Ninja
# from classes.pirate import Pirate
from classes.characters import Character
from classes.characters import Pirate
from classes.characters import Ninja

michelangelo = Ninja("Michelanglo", 12, 7)

jack_sparrow = Pirate("Jack Sparrow", 14, 4)

# michelangelo.attack(jack_sparrow)
# jack_sparrow.show_stats()

michelangelo.show_stats()

jack_sparrow.show_stats()

print(locals())