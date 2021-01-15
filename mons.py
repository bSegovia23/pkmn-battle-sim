import consts
from consts import auto, NUM_MON_DATA_FIELDS, MON_NAME, MON_TYPE, HP, ATK, DEF, SPD, SPC, LEARNSET
from moves import *

# Pokémon species constants
NUM_MONS = 151
consts.counter = 0
BULBASAUR = auto()
CHARMANDER = auto()
SQUIRTLE = auto()

# initialize mon table
mon_table = []
# construct initial mon table
for i in range(NUM_MONS):
  mon_table.append([])
  for j in range(NUM_MON_DATA_FIELDS):
    mon_table[i].append([])

mon_table[BULBASAUR][MON_NAME] = "Bulbasaur"
mon_table[BULBASAUR][MON_TYPE] = [GRASS, POISON]
mon_table[BULBASAUR][HP] = 45
mon_table[BULBASAUR][ATK] = 49
mon_table[BULBASAUR][DEF] = 49
mon_table[BULBASAUR][SPD] = 45
mon_table[BULBASAUR][SPC] = 65
mon_table[BULBASAUR][LEARNSET] = [
  [1, TACKLE, GROWL]
]

mon_table[CHARMANDER][MON_NAME] = "Charmander"
mon_table[CHARMANDER][MON_TYPE] = [FIRE, FIRE]
mon_table[CHARMANDER][HP] = 39
mon_table[CHARMANDER][ATK] = 52
mon_table[CHARMANDER][DEF] = 43
mon_table[CHARMANDER][SPD] = 65
mon_table[CHARMANDER][SPC] = 50
mon_table[CHARMANDER][LEARNSET] = [
  [1, SCRATCH, GROWL]
]

mon_table[SQUIRTLE][MON_NAME] = "Squirtle"
mon_table[SQUIRTLE][MON_TYPE] = [GRASS, GRASS]
mon_table[SQUIRTLE][HP] = 44
mon_table[SQUIRTLE][ATK] = 48
mon_table[SQUIRTLE][DEF] = 65
mon_table[SQUIRTLE][SPD] = 43
mon_table[SQUIRTLE][SPC] = 50
mon_table[SQUIRTLE][LEARNSET] = [
  [1, TACKLE, TAIL_WHIP]
]