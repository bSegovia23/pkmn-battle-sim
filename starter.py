from consts import PLAYER, RIVAL1, trainer_id_to_name
from mons import BULBASAUR, SQUIRTLE, CHARMANDER
from trainer import Trainer

from battle import battle_player_vs_ai

def starter():
  player_name = input("What is your name?\n")
  rival_name = input("What is my grandson's name?\n")
  trainer_id_to_name[PLAYER] = player_name
  trainer_id_to_name[RIVAL1] = rival_name
  starter_choice = int(input("Pick a Pokémon! Your choices are (1) Bulbasaur (2) Squirtle (3) Charmander:\n"))

  if starter_choice == 1:
    player = Trainer(PLAYER, [5, BULBASAUR])
    rival1 = Trainer(RIVAL1, [5, CHARMANDER])
  elif starter_choice == 2:
    player = Trainer(PLAYER, [5, SQUIRTLE])
    rival1 = Trainer(RIVAL1, [5, BULBASAUR])
  elif starter_choice == 3:
    player = Trainer(PLAYER, [5, CHARMANDER])
    rival1 = Trainer(RIVAL1, [5, SQUIRTLE])
  else:
    print("That's not a choice!")

  battle_player_vs_ai(player, rival1)