class User:
    def __init__ (self, first_name, last_name, email, age):
        self.first_name=first_name
        self.last_name=last_name
        self.email= email
        self.age= age
        self.is_rewards_member= False
        self.gold_card_points=0
    def display_info(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Rewards Member: {self.is_rewards_member}")
        print(f"Points:{self.gold_card_points}")

    def enroll(self):
        self.is_rewards_member=True
        self.gold_card_points=200

    def spend_points(self, amount):
        self.gold_card_points -= amount


ana_user= User("Ana", "Lopez", "anal@gmail.com", 29)
kevin_user= User("Kevin", "Smith","ksmith@gmail.com", 30)


# print(ana_user.first_name)
# print(ana_user.last_name)
# print(ana_user.email)
# print(ana_user.age)
# print(ana_user.is_rewards_member)
# print(ana_user. gold_card_points)
ana_user.display_info()
ana_user.enroll()
ana_user.display_info()
ana_user.spend_points(50)
ana_user.display_info()

kevin_user.enroll()
kevin_user.spend_points(80)
kevin_user.display_info()



