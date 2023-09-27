
class User():
    def __init__(self, first_name, last_name, email, age ) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_members = False
        self.gold_card_points = 0
    def display_info(self):
        print(self.first_name, self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_members)
        print(self.gold_card_points, "points")
        return self
    def enroll(self):
        if ( self.is_rewards_members == False):
            self.is_rewards_members = True
            self.gold_card_points += 200
            print("now a member")
        else:
            print("already a member!")
        return self
    def spend_points(self, amount):
        if (amount > self.gold_card_points):
            print(f"Not enough Points!! You only have {self.gold_card_points} points to spend")
        else:
            self.gold_card_points -= amount
            print(f"You have {self.gold_card_points} points remaining")
        return self


mprince = User("Martin", "Prince", "prince@springfieldelem.org", "23")
bsimpson = User("Bart", "Simpson", "simpson@springfieldelem.org", "27")
hsimpson = User("Homer", "Simpson", "hsimpson23@springfieldnuke.org", "53")

mprince.display_info().enroll().spend_points(50).display_info()

bsimpson.display_info().enroll().spend_points(80).display_info()

hsimpson.display_info().spend_points(30).display_info()

