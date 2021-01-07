import time

from Pkmn import Pkmn
from Trainer import Trainer

playerName = input("What is your name?\n")
rivalName = input("What is my grandson's name?\n")
starterChoice = int(input("Pick a Pokémon! Your choices are (1) Bulbasaur (2) Squirtle (3) Charmander:\n"))

if starterChoice == 1:
  player = Trainer(playerName, Pkmn("Bulbasaur", 5))
  rival = Trainer(rivalName, Pkmn("Charmander", 5))
elif starterChoice == 2:
  player = Trainer(playerName, Pkmn("Squirtle", 5))
  rival = Trainer(rivalName, Pkmn("Bulbasaur", 5))
elif starterChoice == 3:
  player = Trainer(playerName, Pkmn("Charmander", 5))
  rival = Trainer(rivalName, Pkmn("Squirtle", 5))

def displayMonState(mon):
  print(mon.name)
  print(":L" + mon.level)
  print("HP: " + mon.currentHP + " / " + mon.stats["HP"])

def displayMoveset(mon):
  moveset = mon.moveset
  for i in range(1,5):
    thisMove = moveset.get(i)
    if thisMove != None:
      print('(' + str(i) + ") " + thisMove.name + ", Type / " + thisMove.moveType + ", Power / " + str(thisMove.power) + ", Accuracy / " + str(thisMove.accuracy))
    else:
      return

def displayGameState(playerMon, opponentMon):
  print("Foe Pkmn:")
  displayMonState(opponentMon)
  print("Player Pkmn:")
  displayMonState(playerMon)
  displayMoveset(playerMon)  

def checkGameOver(player, opponent):
  if not player.pkmnInBattle and not player.firstConsciousMon():
    print(player.name + " is out of usable Pokémon!")
    return True
  elif not opponent.pkmnInBattle and not opponent.firstConsciousMon():
    print(player.name + " defeated " + opponent.name + "!")
    return True
  else:
    if not opponent.pkmnInBattle:
      opponent.sendOutMon()
    if not player.pkmnInBattle:
      player.sendOutMon()
    return False  

def battlePlayerVsAI(player, opponent):
  print(opponent.trainerClass + " would like to fight!")
  #time.sleep(2)
  gameOver = False
  while not gameOver:
    checkGameOver(player, opponent)
    displayGameState(player.pkmnInBattle, opponent.pkmnInBattle)

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



    

battlePlayerVsAI(player, rival)