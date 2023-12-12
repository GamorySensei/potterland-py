import random
from classes.Human import Human

class Wizard(Human):
    
    def __init__(self, first_name, last_name, gender, age, spells):
        super().__init__(first_name, last_name, gender, age)
        self.spells = spells
        self.level = 1

    def level_up(self, level = None):
        if level:
            new_level = level
        else:
            new_level = self.xp // 100

        if new_level > self.level:
            self.level = new_level
            self.xp = self.level * 100
            self.health = self.level * 500
            self.armor = self.level * 100

    def attack(self, human):
        if self.health > 0:
            print("\n---------------------- ATTAQUE ----------------------")
            if human.health > 0:
                spell = random.choice(self.spells)
                proba = random.choice([0,0,0,0,1,1,1])
                if proba == 1:
                    print(f"{self.first_name} attaque {human.first_name} : {spell.name} !")
                    total_damage = round((spell.damage * (self.level/100)) + (human.armor * (human.level/100)) + self.health/100, 2)
                    human.health -= total_damage
                    self.xp += spell.xp
                    self.level_up()
                    print(f"XP : {round(self.xp,2)} -> {self.level} DAMAGE: {total_damage}")
                    if human.health > 0:
                        print(f"{self.first_name} inflige {total_damage} de dégâts à {human.first_name} (vie: {round(human.health,2)})")
                    else: # Attaquant gagne
                        print(f"{self.first_name} vient de tuer {human.first_name}.")
                else:
                    print(f"{self.first_name} a loupé son sort ...")

            else:
                print(f"Impossible d'attquer ! {self.first_name} est déja décédé")
            print()


    