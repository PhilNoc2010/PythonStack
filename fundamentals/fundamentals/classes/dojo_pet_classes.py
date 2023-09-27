class Ninja:

    def __init__(self, first_name, last_name ):
        self.first_name = first_name
        self.last_name = last_name
        # self.pet = Pet()
        self.pets = []
        self.treats = ""
        self.pet_food = ""

    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        self.pet.eat()
        return self

    def bathe(self):
        self.pet.noise()
        return self

    def get_new_pet(self):
        pet_type = input("What type of pet are you getting (Duck or Rat)?")
        if pet_type.lower() == "duck":
            pet_name = input(f"What is your pet {pet_type}'s Name?")
            self.pets.append(Duck(pet_name))
        elif pet_type.lower() == "rat":
            pet_name = input(f"What is your pet {pet_type}'s Name?")
            self.pets.append(Rat(pet_name))
        else:
            print("Those pets are illegal in Michigan.")
            return self

    def show_pets(self):
        for pet in self.pets:
            print(f"{pet.name} the {pet.type}")

class Pet:
    def __init__(self, name):
        self.name = name
        self.type = ""
        self.tricks = ""
        self.health = 0
        self.energy = 0

    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        self.health += 5
        return self

    def noise(self):
        print("the sound of one hand clapping")
        return self

    def display_stats(self):
        print(f"\nPet Name: {self.name}\nPet Health {self.health}\nPet Energy {self.energy}")
        return self

class Duck (Pet):
    def __init__(self, name):
        super().__init__(name)
        self.tricks = "flight"
        self.type = "Duck"

    def noise(self):
        print("quack")
        return self

class Rat (Pet):
    def __init__(self, name):
        super().__init__(name)
        self.tricks = "eat cheese"
        self.type = "Rat"

    def noise(self):
        print ("squeak")
        return self

