import random

class Trainer:
  def __init__(self, trainerClass, pkmn1 = None, pkmn2 = None, pkmn3 = None, pkmn4 = None, pkmn5 = None, pkmn6 = None):
    self.trainerClass = trainerClass
    self.party = {1 : pkmn1, 2 : pkmn2, 3 : pkmn3, 4 : pkmn4, 5 : pkmn5, 6 : pkmn6}
    self.pkmnInBattle = None
  def sendOutMon(self, whichMon = None):
    if not whichMon:
      whichMon = self.firstConsciousMon()
    self.pkmnInBattle = whichMon
    if not whichMon:
      print(self.trainerClass + " sent out " + whichMon.name + '!')
  def firstConsciousMon(self):
    for i in range(1,7):
      if self.party[i].status != "FNT":
        return self.party[i]
    return None
  def printParty(self):
    for i in range(1,7):
      thisMon = self.party[i]
      if thisMon != None and i == 1:
        print('(' + str(i) + ") " + thisMon.name + ", Level " + str(thisMon.level) + ", HP: " + str(thisMon.currentHP) + '/' + str(thisMon.stats["HP"]))
      else:
        return
  def moveChoice(self):
    for i in range(1,5):
      if self.pkmnInBattle.moveset[i] != None:
        i += 1
      else:
        break
    return random.randint(1,i)