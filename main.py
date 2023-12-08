
from classes.Spell import Spell
from classes.Wizard import Wizard

harry = Wizard(
    first_name="Harry",
    last_name="POTTER",
    gender="Male",
    age=11,
    spells=[
        Spell(name="lumos", damage=0, buff=0),
        Spell(name="wingardium leviosa", damage=5, buff=0),
    ]
)

ron = Wizard(
    first_name="Ron",
    last_name="Wesley",
    gender="Male",
    age=11,
    spells=[
        Spell(name="lumos", damage=0, buff=0),
        Spell(name="wingardium leviosa", damage=5, buff=0),
    ]
)

harry.say_hello(ron)
ron.say_hello(harry)

while harry.health > 0:
    harry.attack(ron,1)
    ron.attack(harry,0)
    ron.attack(harry,1)