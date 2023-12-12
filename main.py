
from time import sleep
from os import system
from classes.Game import Game
from classes.Wizard import Wizard
from classes.spells.AvadaKedavra import AvadaKedavra
from classes.spells.Bombarda import Bombarda
from classes.spells.Endoloris import Endoloris

# harry = Wizard(
#     first_name="Harry",
#     last_name="POTTER",
#     gender="Male",
#     age=11,
#     spells=[
#         AvadaKedavra(),
#         Endoloris(),
#         Bombarda(),
#     ]
# )

# ron = Wizard(
#     first_name="Ron",
#     last_name="Wesley",
#     gender="Male",
#     age=11,
#     spells=[
#         AvadaKedavra(),
#         Endoloris(),
#         Bombarda(),
#     ]
# )


# while harry.health > 0 and ron.health > 0:
#     harry.attack(ron)
#     ron.attack(harry)
#     sleep(0.8)
#     system('cls')

game = Game()
game.start()