# save Pokémon species, move pointers, and status conditions as numerical constants, e.g. BULBASAUR = 1

# use an auto() function to make all these constants unique so we don't have to assign them ourselves and we can trivially add on to existing constants
def auto():
  global counter
  counter += 1
  return counter

# mons navigation constants
counter = -1
MON_NAME = auto()
MON_TYPE = auto()
HP = auto()
ATK = auto()
DEF = auto()
SPD = auto()
SPC = auto()
LEARNSET = auto()

# moves navigation constants
counter = -1
MOVE_NAME = auto()
EFFECT = auto()
POWER = auto()
MOVE_TYPE = auto()
ACCURACY = auto()
PP = auto()

# Pokémon species constants
counter = 0
BULBASAUR = auto()
CHARMANDER = auto()
SQUIRTLE = auto()

# type constants
counter = -1
# physical
NORMAL = auto()
POISON = auto()
# special
FIRE = auto()
WATER = auto()
GRASS = auto()

type_id_to_name = [
  "Normal",
  "Poison",
  "Fire",
  "Water",
  "Grass"
]

# move constants
counter = -1
TACKLE = auto()
SCRATCH = auto()
GROWL = auto()
TAIL_WHIP = auto()

move_lookup_table = {
  "tackle" : TACKLE,
  "scratch" : SCRATCH,
  "growl" : GROWL,
  "tail_whip" : TAIL_WHIP
}

# move effect constants
counter = -1
NO_ADDITIONAL_EFFECT = auto()
ATTACK_DOWN1_EFFECT = auto()
DEFENSE_DOWN1_EFFECT = auto()

# status condition constants
counter = -1
BRN = auto()
FRZ = auto()
PAR = auto()
PSN = auto()
SLP = auto()
FNT = auto()
