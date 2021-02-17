from trainer import Trainer

from battle import battle_player_vs_ai

def starter():
  choice = int(input("Welcome to the Pokémon Battle Sim! Please make a selection:\n1. Player vs AI\n2. AI vs AI\n"))

  if choice == 1 :
    #Let them pick a challenger #TODO
    # Build the trainer1 (Player object) as well as their opponent trainer2(AI)
    player_name = input("What is your name?\n")
    rival_name = input("What is my grandson's name?\n")
    
    starter_choice = int(input("Pick a Pokémon! Your choices are (1) Bulbasaur (2) Squirtle (3) Charmander:\n"))

    player = ""
    rival1 = ""

    if starter_choice == 1:
      player = Trainer(player_name, [5, "Bulbasaur"])
      rival1 = Trainer(rival_name, [5, "Charmander"])
    elif starter_choice == 2:
      player = Trainer(player_name, [5, "Squirtle"])
      rival1 = Trainer(rival_name, [5, "Bulbasaur"])
    elif starter_choice == 3:
      player = Trainer(player_name, [5, "Charmander"])
      rival1 = Trainer(rival_name, [5, "Squirtle"])
    else:
      print("That's not a choice!")
      return

    battle_player_vs_ai(player, rival1)
  elif choice == 2:
    #Let them pick 2 AIs # TODO
    #Build trainer1 and trainer2 with their given AI specs
    pass
  