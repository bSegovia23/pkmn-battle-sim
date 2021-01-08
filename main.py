import random
import time
import os

from consts import Pok, Cnd
from trainer import Trainer

player_name = input("What is your name?\n")
rival_name = input("What is my grandson's name?\n")
starter_choice = int(input("Pick a Pokémon! Your choices are (1) Bulbasaur (2) Squirtle (3) Charmander:\n"))

if starter_choice == 1:
  player = Trainer(player_name, [5, Pok.BULBASAUR])
  rival = Trainer(rival_name, [5, Pok.CHARMANDER])
elif starter_choice == 2:
  player = Trainer(player_name, [5, Pok.SQUIRTLE])
  rival = Trainer(rival_name, [5, Pok.BULBASAUR])
elif starter_choice == 3:
  player = Trainer(player_name, [5, Pok.CHARMANDER])
  rival = Trainer(rival_name, [5, Pok.SQUIRTLE])

def display_mon_state(mon, buffer = ''):
  print(buffer + mon.get_name())
  print(buffer + ":L" + str(mon.get_level()))
  print(buffer + "HP:", mon.get_hp_current(), "/", mon.get_hp())

def display_moveset(mon):
  for i in range(1,len(mon.get_moveset())+1):
    print('(' + str(i) + ")", mon.get_moveset()[i].get_name())
    print("Type / " + mon.get_moveset()[i].get_type() + ", Power / " + str(mon.get_moveset()[i].get_power()) + ", Accuracy / " + str(mon.get_moveset()[i].get_accuracy()))

def check_game_over(player, enemy, player_fainted, enemy_fainted):
  if player_fainted:
    player_fcm = player.first_conscious_mon()
    if player_fcm:
      player.send_out_mon(player_fcm)
    else:
      print(player.get_class_(), "is out of usable Pokémon!")
      return True
  if enemy_fainted:
    enemy_fcm = enemy.first_conscious_mon()
    if enemy_fcm:
      enemy.send_out_mon(enemy_fcm)
    else:
      print(player.get_class_(), "defeated", enemy.get_class_() + "!")
      return True

def display_game_state(player_mon, enemy_mon):
  display_mon_state(enemy_mon)
  display_mon_state(player_mon, "                        ")
  display_moveset(player_mon)

def first_round_setup(player, enemy):
  print(enemy.get_class_(), "wants to fight!")
  enemy.send_out_mon()
  player.send_out_mon()

def clear():
  os.system('cls' if os.name == 'nt' else 'clear')

def execute_move(mover, target, move, prefix):
  print(prefix + mover.get_name(), "used", move.get_name() + "!")
  # make sure the target exists/did not faint
  if not target:
    print("But it failed...")
    return
  # accuracy check
  # TO-DO: use accuracy formula with in-battle modifiers
  if move.get_accuracy():
    # https://bulbapedia.bulbagarden.net/wiki/Accuracy
    effective_accuracy = move.get_accuracy()
    if effective_accuracy < random.randint(0,100):
      print(prefix + mover.get_name(), "missed!")
      return
  # do damage if possible
  # TO-DO: implement more modifiers, type effectiveness, physical/special
  if move.get_power():
    # https://bulbapedia.bulbagarden.net/wiki/Damage#Damage_calculation
    # rand = random.randint(217,255) / 255
    rand = 1
    stab = (1.5 if move.get_type() in mover.get_type() else 1)
    type = 1 # type effectiveness to be implemented
    other = 1 # 1 in most cases, other cases to be implemented
    mod = rand * stab * type * other
    damage = (((2 * mover.get_level()) // 5 + 2) * move.get_power() * (mover.get_eff_atk() // target.get_eff_def()) // 50 + 2) * mod
    target.damage_hp(damage)
    print("Did", damage, "damage!")
  # TO-DO: non-damaging effects

def faint_check(trainer, is_enemy = False):
  if trainer.get_mon_in_battle().get_hp_current() <= 0:
    prefix = ("Enemy " if is_enemy == True else '')
    trainer.get_mon_in_battle().set_status(Cnd.FNT)
    print(prefix + trainer.get_mon_in_battle().get_name(), "fainted!")
    trainer.set_mon_in_battle(None)
    return True
  return False

def take_turn(trainer, opponent, action, is_enemy = False):
  # TO-DO: allow for more actions in a turn than making a move, e.g. healing
  prefix = ("Enemy " if is_enemy == True else '')
  execute_move(trainer.get_mon_in_battle(), opponent.get_mon_in_battle(), action, prefix)

def battle_player_vs_ai(player, enemy):
  # TO-DO: make use of clear() function to refresh terminal
  game_over = False
  first_round = True
  while not game_over:
    if first_round:
      first_round_setup(player, enemy)
      first_round = False
    display_game_state(player.get_mon_in_battle(), enemy.get_mon_in_battle())
    # TO-DO: implement PP check for player
    player_move = player.get_mon_in_battle().get_moveset()[int(input())]
    if player.get_mon_in_battle().get_eff_spd() > enemy.get_mon_in_battle().get_eff_spd() or (player.get_mon_in_battle().get_eff_spd() == enemy.get_mon_in_battle().get_eff_spd() and random.randint(1,2) == 1):
      take_turn(player, enemy, player_move)
      player_fainted = faint_check(player)
      enemy_fainted = faint_check(enemy, True)
      if not enemy_fainted:
        take_turn(enemy, player, enemy.move_choice(), True)
        player_fainted = faint_check(player)
        enemy_fainted = faint_check(enemy, True)
    else:
      take_turn(enemy, player, enemy.move_choice(), True)
      player_fainted = faint_check(player)
      enemy_fainted = faint_check(enemy, True)
      if not player_fainted:
        take_turn(player, enemy, player_move)
        player_fainted = faint_check(player)
        enemy_fainted = faint_check(enemy, True)
    game_over = check_game_over(player, enemy, player_fainted, enemy_fainted)


#GameLoop
#1. Display the Current state of the game
#2. Outline the Player's choice (deleted if no player)
#3. Show player's choice
#4. Display the result of their choice
#5. Check if the game is over
#6. Whoever hasn't gone will go
#7. Check if the game is over


#  [########]
# __




#Player1 100HP



    

battle_player_vs_ai(player, rival)