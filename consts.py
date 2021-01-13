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
FIGHTING = auto()
FLYING = auto()
POISON = auto()
GROUND = auto()
ROCK = auto()
BIRD = auto()
BUG = auto()
GHOST = auto()
# special
FIRE = auto()
WATER = auto()
GRASS = auto()
ELECTRIC = auto()
PSYCHIC_TYPE = auto()
ICE = auto()
DRAGON = auto()

physical_types = [NORMAL, FIGHTING, FLYING, POISON, GROUND, ROCK, BIRD, BUG, GHOST]

type_id_to_name = [
  "Normal", "Fighting", "Flying", "Poison", "Ground", "Rock", "Bird", "Bug", "Ghost", "Fire", "Water", "Grass", "Electric", "Psychic", "Ice", "Dragon"
]

# type matchup constants
NO_EFFECT = 0
NOT_VERY_EFFECTIVE = 0.5
EFFECTIVE = 1
SUPER_EFFECTIVE = 2

NUM_TYPES = 16 # we are including BIRD type if we want Missingno later
# type_matchup[TYPE1][TYPE2] is one of the former four constants
type_matchup = []
# construct default type chart
for i in range(NUM_TYPES):
  # define type_matchup[i]
  type_matchup.append([])
  for j in range(NUM_TYPES):
    # define type_matchup[i][j] as EFFECTIVE, may be changed later
    type_matchup[i].append(EFFECTIVE)
# set up Gen I type matches
type_matchup[WATER][FIRE] = SUPER_EFFECTIVE
type_matchup[FIRE][GRASS] = SUPER_EFFECTIVE
type_matchup[FIRE][ICE] = SUPER_EFFECTIVE
type_matchup[GRASS][WATER] = SUPER_EFFECTIVE
type_matchup[ELECTRIC][WATER] = SUPER_EFFECTIVE
type_matchup[WATER][ROCK] = SUPER_EFFECTIVE
type_matchup[GROUND][FLYING] = NO_EFFECT
type_matchup[WATER][WATER] = NOT_VERY_EFFECTIVE
type_matchup[FIRE][FIRE] = NOT_VERY_EFFECTIVE
type_matchup[ELECTRIC][ELECTRIC] = NOT_VERY_EFFECTIVE
type_matchup[ICE][ICE] = NOT_VERY_EFFECTIVE
type_matchup[GRASS][GRASS] = NOT_VERY_EFFECTIVE
type_matchup[PSYCHIC_TYPE][PSYCHIC_TYPE] = NOT_VERY_EFFECTIVE
type_matchup[FIRE][WATER] = NOT_VERY_EFFECTIVE
type_matchup[GRASS][FIRE] = NOT_VERY_EFFECTIVE
type_matchup[WATER][GRASS] = NOT_VERY_EFFECTIVE
type_matchup[ELECTRIC][GRASS] = NOT_VERY_EFFECTIVE
type_matchup[NORMAL][ROCK] = NOT_VERY_EFFECTIVE
type_matchup[NORMAL][GHOST] = NO_EFFECT
type_matchup[GHOST][GHOST] = SUPER_EFFECTIVE
type_matchup[FIRE][BUG] = SUPER_EFFECTIVE
type_matchup[FIRE][ROCK] = NOT_VERY_EFFECTIVE
type_matchup[WATER][GROUND] = SUPER_EFFECTIVE
type_matchup[ELECTRIC][GROUND] = NO_EFFECT
type_matchup[ELECTRIC][FLYING] = SUPER_EFFECTIVE
type_matchup[GRASS][GROUND] = SUPER_EFFECTIVE
type_matchup[GRASS][BUG] = NOT_VERY_EFFECTIVE
type_matchup[GRASS][POISON] = NOT_VERY_EFFECTIVE
type_matchup[GRASS][ROCK] = SUPER_EFFECTIVE
type_matchup[GRASS][FLYING] = NOT_VERY_EFFECTIVE
type_matchup[ICE][WATER] = NOT_VERY_EFFECTIVE
type_matchup[ICE][GRASS] = SUPER_EFFECTIVE
type_matchup[ICE][GROUND] = SUPER_EFFECTIVE
type_matchup[ICE][FLYING] = SUPER_EFFECTIVE
type_matchup[FIGHTING][NORMAL] = SUPER_EFFECTIVE
type_matchup[FIGHTING][POISON] = NOT_VERY_EFFECTIVE
type_matchup[FIGHTING][FLYING] = NOT_VERY_EFFECTIVE
type_matchup[FIGHTING][PSYCHIC_TYPE] = NOT_VERY_EFFECTIVE
type_matchup[FIGHTING][BUG] = NOT_VERY_EFFECTIVE
type_matchup[FIGHTING][ROCK] = SUPER_EFFECTIVE
type_matchup[FIGHTING][ICE] = SUPER_EFFECTIVE
type_matchup[FIGHTING][GHOST] = NO_EFFECT
type_matchup[POISON][GRASS] = SUPER_EFFECTIVE
type_matchup[POISON][POISON] = NOT_VERY_EFFECTIVE
type_matchup[POISON][GROUND] = NOT_VERY_EFFECTIVE
type_matchup[POISON][BUG] = SUPER_EFFECTIVE
type_matchup[POISON][ROCK] = NOT_VERY_EFFECTIVE
type_matchup[POISON][GHOST] = NOT_VERY_EFFECTIVE
type_matchup[GROUND][FIRE] = SUPER_EFFECTIVE
type_matchup[GROUND][ELECTRIC] = SUPER_EFFECTIVE
type_matchup[GROUND][GRASS] = NOT_VERY_EFFECTIVE
type_matchup[GROUND][BUG] = NOT_VERY_EFFECTIVE
type_matchup[GROUND][ROCK] = SUPER_EFFECTIVE
type_matchup[GROUND][POISON] = SUPER_EFFECTIVE
type_matchup[FLYING][ELECTRIC] = NOT_VERY_EFFECTIVE
type_matchup[FLYING][FIGHTING] = SUPER_EFFECTIVE
type_matchup[FLYING][BUG] = SUPER_EFFECTIVE
type_matchup[FLYING][GRASS] = SUPER_EFFECTIVE
type_matchup[FLYING][ROCK] = NOT_VERY_EFFECTIVE
type_matchup[PSYCHIC_TYPE][FIGHTING] = SUPER_EFFECTIVE
type_matchup[PSYCHIC_TYPE][POISON] = SUPER_EFFECTIVE
type_matchup[BUG][FIRE] = NOT_VERY_EFFECTIVE
type_matchup[BUG][GRASS] = SUPER_EFFECTIVE
type_matchup[BUG][FIGHTING] = NOT_VERY_EFFECTIVE
type_matchup[BUG][FLYING] = NOT_VERY_EFFECTIVE
type_matchup[BUG][PSYCHIC_TYPE] = SUPER_EFFECTIVE
type_matchup[BUG][GHOST] = NOT_VERY_EFFECTIVE
type_matchup[BUG][POISON] = SUPER_EFFECTIVE
type_matchup[ROCK][FIRE] = SUPER_EFFECTIVE
type_matchup[ROCK][FIGHTING] = NOT_VERY_EFFECTIVE
type_matchup[ROCK][GROUND] = NOT_VERY_EFFECTIVE
type_matchup[ROCK][FLYING] = SUPER_EFFECTIVE
type_matchup[ROCK][BUG] = SUPER_EFFECTIVE
type_matchup[ROCK][ICE] = SUPER_EFFECTIVE
type_matchup[GHOST][NORMAL] = NO_EFFECT
type_matchup[GHOST][PSYCHIC_TYPE] = NO_EFFECT
type_matchup[FIRE][DRAGON] = NOT_VERY_EFFECTIVE
type_matchup[WATER][DRAGON] = NOT_VERY_EFFECTIVE
type_matchup[ELECTRIC][DRAGON] = NOT_VERY_EFFECTIVE
type_matchup[GRASS][DRAGON] = NOT_VERY_EFFECTIVE
type_matchup[ICE][DRAGON] = SUPER_EFFECTIVE
type_matchup[DRAGON][DRAGON] = SUPER_EFFECTIVE

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
