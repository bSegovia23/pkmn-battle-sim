import math
import json
import random

with open("pkmn.json", "r") as mons:
  mons = json.load(mons)
with open("moves.json", "r") as moves:
  moves = json.load(moves)

class Move:
  def __init__(self, name):
    self.name = name
    self.moveType = moves[name]["moveType"]
    self.power = moves[name].get("power")
    self.accuracy = moves[name]["accuracy"]

class Pkmn:
  def __init__(self, name, level):
    self.name = name
    self.level = level
    self.baseStats = mons[name]["baseStats"]
    self.IVs = self.__generateIVs()
    self.stats = self.calcStats()
    self.learnset = mons[name]["learnset"]
    self.moveset = self.__generateMoveset()
    self.currentHP = self.stats["HP"]
    self.status = None
  
  def __generateIVs(self):
    atkIV = random.randint(0,15)
    defIV = random.randint(0,15)
    speIV = random.randint(0,15)
    spcIV = random.randint(0,15)
    hpIV = (atkIV % 2) * (2**3) + (defIV % 2) * (2**2) + (speIV % 2) * 2 + (spcIV % 2)
    return {"HP" : hpIV, "Atk" : atkIV, "Def" : defIV, "Spe" : speIV, "Spc" : spcIV}
  
  def calcStats(self):
    level = self.level
    stats = ["HP", "Atk", "Def", "Spe", "Spc"]
    statValues = {}
    for stat in stats:
      base = self.baseStats[stat]
      IV = self.IVs[stat]
      if stat == "HP":
        statValue = math.floor(((base + IV)*2)*level/100) + level + 10
      else:
        statValue = math.floor(((base + IV)*2)*level/100) + 5
      statValues[stat] = statValue
    return statValues
    
  def __generateMoveset(self):
    moveset = {}
    movesetPos = 1 # cycles through 1-4
    learnset = self.learnset
    for lvl in range(self.level):
      if learnset.get(str(lvl)) != None:
        for move in learnset[str(lvl)]:
          moveset[movesetPos] = Move(move)
          movesetPos += 1
          if movesetPos > 4:
            movesetPos = 1 # after learning move 4, back to move 1
    return moveset