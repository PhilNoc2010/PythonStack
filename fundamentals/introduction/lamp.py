
class Lamp:
    manufacturer = "Tyler"
    all_lamps = []

    def __init__(self, name):
        self.name = name
        Lamp.all_lamps.append(self)

    def info(self):
        print(self.name)
        return self

    def change_name(self, new_name):
        self.name = new_name
        return self

    # class methods target the class and all instances of a class
    @classmethod
    def change_manufacturer(cls, new_name):
        cls.manufacturer = new_name

    @staticmethod
    def say_the_name(name):
        print(f"the name is {name}")


lamp1 = Lamp("jonny")
lamp2 = Lamp("Jimmy")

print(lamp1.manufacturer)

Lamp.change_manufacturer("Johns")

print(lamp1.manufacturer)