import random
from consts import FNT
from pkmn import Pkmn

class Trainer:
  def __init__(self, class_, party_data):
    self.__class_ = class_
    self.__party = []
    # if party_data[0] != -1, then
      # party_data[0] is level (of all pkmn on this team)
      # all the next entries are species
    # if party_data[0] == -1, then
      # party_data[0] is -1 (obviously)
      # every next two entries are a level and species
    if party_data[0] != -1:
      for i in range(1, len(party_data)):
        self.__party.append(Pkmn(party_data[i], party_data[0]))
    else:
      for i in range(1, len(party_data), 2):
        self.__party.append(Pkmn(party_data[i+1], party_data[i]))

  def send_out_mon(self, which_mon = None):
    if not which_mon:
      which_mon = self.first_conscious_mon()
    self.mon_in_battle = which_mon
    print(self.__class_, "sent out", which_mon.get_name() + '!')
  def first_conscious_mon(self):
    for mon in self.__party:
      if mon.get_status() != FNT:
        return mon
    return None
  def print_party(self):
    for i in range(len(self.__party)):
      print('(' + str(i) + ')', self.__party[i].get_name() + ", Level", str(self.__party[i].get_level()) + ", HP:", str(self.__party[i].get_hp_current()) + '/' + str(self.__party[i].get_hp()))
  def move_choice(self, is_player = False):
    # https://github.com/pret/pokered/blob/master/engine/battle/trainer_ai.asm
    #TODO, set up dictionary call/JSON for each trainer AI
    if is_player:
      return self.get_mon_in_battle().get_moveset()[int(input())-1]
    else:
      return self.mon_in_battle.get_usable_moves()[random.randint(0, len(self.mon_in_battle.get_usable_moves())-1)]
  
  def get_class_(self):
    return self.__class_
  def get_name(self):
    return self.__class_
  def get_mon_in_battle(self):
    return self.mon_in_battle
  def set_mon_in_battle(self, mon):
    self.mon_in_battle = mon