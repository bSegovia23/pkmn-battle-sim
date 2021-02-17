import json
import math

with open('moves.json') as move_table:
  move_table = json.load(move_table)

class Move:
  def __init__(self, name):
    self.__name = name
    self.__effect = move_table[name]["effect"]
    self.__power = move_table[name]["power"]
    self.__type = move_table[name]["move_type"]
    self.__accuracy = math.floor(2.55 * move_table[name]["accuracy"])
    self.__pp = move_table[name]["pp"]
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
    return self.__type
  def get_accuracy(self):
    return self.__accuracy
  def get_accuracy_100(self):
    return math.ceil(self.__accuracy / 2.56)