import random
import time
import os

from consts import *
from moves import *
from mons import BULBASAUR, SQUIRTLE, CHARMANDER
from trainer import Trainer

player_name = input("What is your name?\n")
rival_name = input("What is my grandson's name?\n")
trainer_id_to_name[PLAYER] = player_name
trainer_id_to_name[RIVAL1] = rival_name
trainer_id_to_name[RIVAL2] = rival_name
trainer_id_to_name[RIVAL3] = rival_name
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

def health_bar(mon):
  ratio = mon.get_hp_current() / mon.get_hp()
  bar = '['
  width = 10
  for i in range(width):
    if i <= ratio * width:
      bar += '|'
    else:
      bar += '_'
  bar += ']'
  return bar

def display_mon_state(mon, buffer = ''):
  print(buffer + mon.get_name())
  print(buffer + ":L" + str(mon.get_level()))
  print(buffer + "HP:", health_bar(mon))
  print(buffer + "   ", mon.get_hp_current(), "/", mon.get_hp())

def display_moveset(mon):
  for i in range(1,len(mon.get_moveset())+1):
    print('(' + str(i) + ")", mon.get_moveset()[i].get_name())
    print("Type / " + mon.get_moveset()[i].get_type_name() + ", Power / " + str(mon.get_moveset()[i].get_power()) + ", Accuracy / " + str(mon.get_moveset()[i].get_accuracy_100()))

def check_game_over(player, enemy, player_fainted, enemy_fainted):
  if player_fainted:
    player_fcm = player.first_conscious_mon()
    if player_fcm:
      player.send_out_mon(player_fcm)
    else:
      print(player.get_name(), "is out of usable Pokémon!")
      return True
  if enemy_fainted:
    enemy_fcm = enemy.first_conscious_mon()
    if enemy_fcm:
      enemy.send_out_mon(enemy_fcm)
    else:
      print(player.get_name(), "defeated", enemy.get_name() + "!")
      return True

def display_game_state(player_mon, enemy_mon):
  display_mon_state(enemy_mon)
  display_mon_state(player_mon, "                        ")
  display_moveset(player_mon)

def first_round_setup(player, enemy):
  print(enemy.get_name(), "wants to fight!")
  enemy.send_out_mon()
  player.send_out_mon()

def clear():
  os.system('cls' if os.name == 'nt' else 'clear')

def battle_msg(string, is_enemy = False):
  prefix = ("Enemy " if is_enemy else '')
  print(prefix + string)

def execute_move(user, target, move, is_enemy = False):
  battle_msg(user.get_name() + " used " + move.get_name() + "!", is_enemy)
  # make sure the target exists/did not faint
  if not target:
    print("But it failed...")
    return False
  # accuracy check
  if move.get_accuracy():
    # https://bulbapedia.bulbagarden.net/wiki/Accuracy
    effective_accuracy = move.get_accuracy()
    if not (random.randint(0,255) < effective_accuracy):
      battle_msg(user.get_name() + " missed!", is_enemy)
      if effective_accuracy == 255:
        print("(In Gen 1, moves with 100% accuracy can still miss 1/256 of the time.)")
      return False
  # do damage if possible
  # TO-DO: implement more modifiers
  if move.get_power():
    # https://bulbapedia.bulbagarden.net/wiki/Damage#Damage_calculation
    if move.get_type() in physical_types:
      atk = user.get_eff_atk()
      dfs = target.get_eff_def()
    else:
      atk = user.get_eff_spc()
      dfs = target.get_eff_spc()
    print(atk, dfs)
    
    rand = random.randint(217,255)
    stab = (MORE_EFFECTIVE if move.get_type() in user.get_type() else EFFECTIVE)
    type_ = type_matchup[move.get_type()][target.get_type()[0]]
    print(target.get_type())
    if target.get_type()[0] != target.get_type()[1]:
      type_ *= type_matchup[move.get_type()][target.get_type()[1]]
    
    # in the 90s, Game Freak didn't want to deal with decimals
    # so every step that would produce a decimal gets rounded down
    # GF did this by making stab and type_ multiples of 10 and using int division
    # we will use int conversion after each / and each * by a non-int

    damage = int((2 * user.get_level()) / 5)
    damage = int((damage + 2) * atk * move.get_power() / dfs)
    damage = int(damage / 50)
    damage = int((damage + 2) * stab)
    damage = int(damage * type_)
    damage = int(damage * rand / 255)

    target.mod_current_hp(-damage)
    battle_msg("Did" + ' ' + str(damage) + " damage!")
    if type_ == NO_EFFECT:
      battle_msg("It had no effect.")
    elif type_ <= NOT_VERY_EFFECTIVE:
      battle_msg("It's not very effective...")
    elif type_ >= SUPER_EFFECTIVE:
      battle_msg("It's super effective!")
  # execute effect
  if move.get_effect():
    if move.get_effect() == ATTACK_DOWN1_EFFECT:
      target.mod_atk_stage(-1)
      battle_msg(target.get_name() +"'s Attack fell!", not is_enemy)
    elif move.get_effect() == DEFENSE_DOWN1_EFFECT:
      target.mod_def_stage(-1)
      battle_msg(target.get_name() +"'s Defense fell!", not is_enemy)

def faint_check(trainer, is_enemy = False):
  if trainer.get_mon_in_battle().get_hp_current() <= 0:
    trainer.get_mon_in_battle().set_status(FNT)
    battle_msg(trainer.get_mon_in_battle().get_name() + " fainted!", is_enemy)
    trainer.set_mon_in_battle(None)
    return True
  return False

def take_turn(trainer, opponent, action, is_enemy = False):
  # TO-DO: allow for more actions in a turn than making a move, e.g. healing
  execute_move(trainer.get_mon_in_battle(), opponent.get_mon_in_battle(), action, is_enemy)

def battle_player_vs_ai(player, enemy):
  game_over = False
  first_round = True
  while not game_over:
    if first_round:
      clear()
      first_round_setup(player, enemy)
      first_round = False
    display_game_state(player.get_mon_in_battle(), enemy.get_mon_in_battle())
    # TO-DO: implement PP check for player
    player_move = player.move_choice()
    clear()
    if player.get_mon_in_battle().get_eff_spd() > enemy.get_mon_in_battle().get_eff_spd() or (player.get_mon_in_battle().get_eff_spd() == enemy.get_mon_in_battle().get_eff_spd() and random.randint(1,2) == 1):
      take_turn(player, enemy, player_move)
      player_fainted = faint_check(player)
      enemy_fainted = faint_check(enemy, True)
      if not enemy_fainted:
        # AI is a cheating bastard in Gen I, takes its move after you do if it's slower
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



    

battle_player_vs_ai(player, rival1)