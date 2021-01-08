import math
import json
import random

with open("mons.json", "r") as mons:
  mons = json.load(mons)
with open("moves.json", "r") as moves:
  moves = json.load(moves)

class Move:
  def __init__(self, name):
    self.__name = name
    self.__type = moves[name].get("type")
    self.__power = moves[name].get("power")
    self.__accuracy = moves[name].get("accuracy")

  def get_name(self):
    return self.__name
  def get_type(self):
    return self.__type
  def get_power(self):
    return self.__power
  def get_accuracy(self):
    return self.__accuracy

class Pkmn:
  def __init__(self, const, level):
    index = const.value
    self.__name = mons[index]["name"]
    self.__level = level
    self.__type = mons[index]["type"]

    # base stats
    self.__atk_base = mons[index]["atk"]
    self.__def_base = mons[index]["def"]
    self.__spc_base = mons[index]["spc"]
    self.__spd_base = mons[index]["spd"]
    self.__hp_base = mons[index]["hp"]

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
    self.__hp_current = self.__hp

    self.__learnset = mons[index]["learnset"]
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

  def __generate_moveset(self):
    moveset = {}
    movesetPos = 1 # cycles through 1-4
    for lvl in range(self.__level+1):
      if self.__learnset.get(str(lvl)) != None:
        for move in self.__learnset[str(lvl)]:
          moveset[movesetPos] = Move(move)
          movesetPos += 1
          if movesetPos > 4:
            movesetPos = 1 # after learning move 4, back to move 1
    self.__moveset = moveset
  
  def damage_hp(self, damage):
    self.__hp_current -= damage
    self.__hp_current = max(self.__hp_current, 0)

  def set_status(self, status):
    self.__status = status

  def get_name(self):
    return self.__name
  def get_level(self):
    return self.__level
  def get_type(self):
    return self.__type

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
  # https://bulbapedia.bulbagarden.net/wiki/Statistic#In_battle
  def get_eff_atk(self):
    return self.__atk
  def get_eff_def(self):
    return self.__def
  def get_eff_spd(self):
    return self.__spd