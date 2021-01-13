import math
import random

from consts import *

from mons import mons
from moves import moves, type_id_to_name

class Move:
  def __init__(self, id):
    self.__name = moves[id][MOVE_NAME]
    self.__effect = moves[id][EFFECT]
    self.__power = moves[id][POWER]
    self.__type = moves[id][MOVE_TYPE]
    self.__accuracy = math.floor(2.55 * moves[id][ACCURACY])
    self.__pp = moves[id][PP]
    # accuracies are stored as fractions out of 256
    # to convert from percentage to /256, multiply by 2.55 and round down
    # to convert from /256 to percentage, divide by 2.56 and round up

  def get_name(self):
    return self.__name
  def get_effect(self):
    return self.__effect
  def get_power(self):
    return self.__power
  def get_type(self):
    return self.__type
  def get_type_name(self):
    return type_id_to_name[self.__type]
  def get_accuracy(self):
    return self.__accuracy
  def get_accuracy_100(self):
    return math.ceil(self.__accuracy / 2.56)

class Pkmn:
  def __init__(self, id, level):
    self.__name = mons[id][MON_NAME]
    self.__level = level
    self.__type = mons[id][MON_TYPE]

    # base stats
    self.__atk_base = mons[id][ATK]
    self.__def_base = mons[id][DEF]
    self.__spc_base = mons[id][SPC]
    self.__spd_base = mons[id][SPD]
    self.__hp_base = mons[id][HP]

    # generate IVs
    # https://bulbapedia.bulbagarden.net/wiki/Individual_values#Generation_I_and_II
    self.__atk_iv = random.randint(0, 15)
    self.__def_iv = random.randint(0, 15)
    self.__spc_iv = random.randint(0, 15)
    self.__spd_iv = random.randint(0, 15)
    self.__hp_iv = (self.__atk_iv % 2) * (2**3) + (self.__def_iv % 2) * (2**2) + (self.__spd_iv % 2) * 2 + (self.__spc_iv % 2)

    # initialize EVs
    # in Gen I and II, EVs given in battle are equal to the base stats of defeated mon
    self.__atk_ev = 0
    self.__def_ev = 0
    self.__spc_ev = 0
    self.__spd_ev = 0
    self.__hp_ev = 0

    self.__generate_stats()
    
    # initialize stats that will be modified in battle
    self.__hp_current = self.__hp
    self.__atk_stage = 0
    self.__def_stage = 0
    self.__spc_stage = 0
    self.__spd_stage = 0

    self.__learnset = mons[id][LEARNSET]
    self.__generate_moveset()
    self.__usable_moves = self.__moveset
    
    self.__status = None

  def __generate_stats(self):
    self.__atk = self.__calc_stat(self.__atk_base, self.__atk_iv, self.__atk_ev, self.__level)
    self.__def = self.__calc_stat(self.__def_base, self.__def_iv, self.__def_ev, self.__level)
    self.__spc = self.__calc_stat(self.__spc_base, self.__spc_iv, self.__spc_ev, self.__level)
    self.__spd = self.__calc_stat(self.__spd_base, self.__spd_iv, self.__spd_ev, self.__level)
    self.__hp = self.__calc_stat(self.__hp_base, self.__hp_iv, self.__hp_ev, self.__level, True) # HP is determined by a slightly different formula
  
  def __calc_stat(self, base, iv, ev, level, hp = False):
    # https://bulbapedia.bulbagarden.net/wiki/Statistic#In_Generations_I_and_II
    if hp:
      return math.floor(((base + iv) * 2 + math.floor(math.ceil(math.sqrt(ev)) / 4)) * level / 100) + level + 10
    else:
      return math.floor(((base + iv) * 2 + math.floor(math.ceil(math.sqrt(ev)) / 4)) * level / 100) + 5

  # https://bulbapedia.bulbagarden.net/wiki/Statistic#Stage_multipliers
  def mod_current_hp(self, mod):
    self.__hp_current += mod
    self.__hp_current = max(self.__hp_current, 0)
    self.__hp_current = min(self.__hp_current, self.__hp)
  def mod_atk_stage(self, mod):
    num_stages = 6
    self.__atk_stage += mod
    self.__atk_stage = max(self.__atk_stage, -num_stages)
    self.__atk_stage = min(self.__atk_stage, num_stages)
  def mod_def_stage(self, mod):
    num_stages = 6
    self.__def_stage += mod
    self.__def_stage = max(self.__def_stage, -num_stages)
    self.__def_stage = min(self.__def_stage, num_stages)
  def mod_spc_stage(self, mod):
    num_stages = 6
    self.__spc_stage += mod
    self.__spc_stage = max(self.__spc_stage, -num_stages)
    self.__spc_stage = min(self.__spc_stage, num_stages)
  def mod_spd_stage(self, mod):
    num_stages = 6
    self.__spd_stage += mod
    self.__spd_stage = max(self.__spd_stage, -num_stages)
    self.__spd_stage = min(self.__spd_stage, num_stages)

  def __generate_moveset(self):
    moveset = {}
    moveset_pos = 1 # cycles through 1-4
    for entry in self.__learnset:
      if entry[0] <= self.__level:
        for move in entry[1:]:
          moveset[moveset_pos] = Move(move)
          moveset_pos += 1
          if moveset_pos > 4:
            moveset_pos = 1 # after learning move 4, back to move 1
      else:
        break
    self.__moveset = moveset

  def set_status(self, status):
    self.__status = status

  def get_name(self):
    return self.__name
  def get_level(self):
    return self.__level
  def get_type(self):
    return self.__type
  def get_type_name(self):
    return type_id_to_name[self.__type]

  def get_hp(self):
    return self.__hp
  def get_hp_current(self):
    return self.__hp_current
  def get_moveset(self):
    return self.__moveset
  def get_usable_moves(self):
    return self.__usable_moves
  def get_status(self):
    return self.__status

  # TO-DO: have "effective" stats
  # i.e. after increased/decreased with in-battle multipliers
  # https://bulbapedia.bulbagarden.net/wiki/Statistic#Stage_multipliers
  def get_eff_atk(self):
    if self.__atk_stage >= 0:
      mult = (2 + self.__atk_stage) / 2
    else:
      mult = 2 / (2 - self.__atk_stage)
    return math.floor(mult * self.__atk)
  def get_eff_def(self):
    if self.__def_stage >= 0:
      mult = (2 + self.__def_stage) / 2
    else:
      mult = 2 / (2 - self.__def_stage)
    return math.floor(mult * self.__def)
  def get_eff_spd(self):
    if self.__spd_stage >= 0:
      mult = (2 + self.__spd_stage) / 2
    else:
      mult = 2 / (2 - self.__spd_stage)
    return math.floor(mult * self.__spd)
  def get_eff_spc(self):
    if self.__spc_stage >= 0:
      mult = (2 + self.__spc_stage) / 2
    else:
      mult = 2 / (2 - self.__spc_stage)
    return math.floor(mult * self.__spc)