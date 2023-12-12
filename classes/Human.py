class Human:
    def __init__(self, first_name, last_name, gender, age):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
        self.health = 500
        self.speed = 1
        self.armor = 0
        self.xp = 100

    def say_hello(self, human):
        print(f"{self.first_name} dit : Salut  {human.first_name} !")

    def drink(self):
        pass

    def eat(self):
        pass
