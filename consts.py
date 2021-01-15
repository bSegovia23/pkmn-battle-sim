# save Pokémon species, move pointers, and status conditions as numerical constants, e.g. BULBASAUR = 1

# use an auto() function to make all these constants unique so we don't have to assign them ourselves and we can trivially add on to existing constants
def auto():
  global counter
  counter += 1
  return counter - 1

# mons navigation constants
NUM_MON_DATA_FIELDS = 8
counter = 0
MON_NAME = auto()
MON_TYPE = auto()
HP = auto()
ATK = auto()
DEF = auto()
SPD = auto()
SPC = auto()
LEARNSET = auto()

# move data constants
NUM_MOVE_DATA_FIELDS = 6
counter = 0
MOVE_NAME = auto()
EFFECT = auto()
POWER = auto()
MOVE_TYPE = auto()
ACCURACY = auto()
PP = auto()

# status condition constants
counter = 0
BRN = auto()
FRZ = auto()
PAR = auto()
PSN = auto()
SLP = auto()
FNT = auto()

# trainer class constants
NUM_TRAINERS = 46 # not counting UnusedJuggler
counter = 0
PLAYER = auto()
YOUNGSTER = auto()
BUG_CATCHER = auto()
LASS = auto()
SAILOR = auto()
JR_TRAINER_M = auto()
JR_TRAINER_F = auto()
POKEMANIAC = auto()
SUPER_NERD = auto()
HIKER = auto()
BIKER = auto()
BURGLAR = auto()
ENGINEER = auto()
FISHER = auto()
SWIMMER = auto()
CUE_BALL = auto()
GAMBLER = auto()
BEAUTY = auto()
PSYCHIC = auto()
ROCKER = auto()
JUGGLER = auto()
TAMER = auto()
BIRD_KEEPER = auto()
BLACKBELT = auto()
RIVAL1 = auto()
PROF_OAK = auto()
SCIENTIST = auto()
GIOVANNI = auto()
ROCKET = auto()
COOLTRAINER_F = auto()
COOLTRAINER_M = auto()
BRUNO = auto()
BROCK = auto()
MISTY = auto()
LT_SURGE = auto()
ERIKA = auto()
KOGA = auto()
BLAINE = auto()
SABRINA = auto()
GENTLEMAN = auto()
RIVAL2 = auto()
RIVAL3 = auto()
LORELEI = auto()
CHANNELER = auto()
AGATHA = auto()
LANCE = auto()

trainer_id_to_name = []
for i in range(NUM_TRAINERS):
  trainer_id_to_name.append('')
trainer_id_to_name[YOUNGSTER] = "Youngster"
trainer_id_to_name[BUG_CATCHER] = "Bug Catcher"
trainer_id_to_name[LASS] = "Lass"
trainer_id_to_name[SAILOR] = "Sailor"
trainer_id_to_name[JR_TRAINER_M] = "Jr. Trainer♂"
trainer_id_to_name[JR_TRAINER_F] = "Jr. Trainer♀"
trainer_id_to_name[POKEMANIAC] = "PokéManiac"
trainer_id_to_name[SUPER_NERD] = "Super Nerd"
trainer_id_to_name[HIKER] = "Hiker"
trainer_id_to_name[BIKER] = "Biker"
trainer_id_to_name[BURGLAR] = "Burglar"
trainer_id_to_name[ENGINEER] = "Engineer"
trainer_id_to_name[FISHER] = "Fisher"
trainer_id_to_name[SWIMMER] = "Swimmer"
trainer_id_to_name[CUE_BALL] = "Cue Ball"
trainer_id_to_name[GAMBLER] = "Gambler"
trainer_id_to_name[BEAUTY] = "Beauty"
trainer_id_to_name[PSYCHIC] = "Psychic"
trainer_id_to_name[ROCKER] = "Rocker"
trainer_id_to_name[JUGGLER] = "Juggler"
trainer_id_to_name[TAMER] = "Tamer"
trainer_id_to_name[BIRD_KEEPER] = "Bird Keeper"
trainer_id_to_name[BLACKBELT] = "Blackbelt"
trainer_id_to_name[PROF_OAK] = "Prof. Oak"
trainer_id_to_name[SCIENTIST] = "Scientist"
trainer_id_to_name[GIOVANNI] = "Giovanni"
trainer_id_to_name[ROCKET] = "Rocket"
trainer_id_to_name[COOLTRAINER_F] = "Cooltrainer♀"
trainer_id_to_name[COOLTRAINER_M] = "Cooltrainer♂"
trainer_id_to_name[BRUNO] = "Bruno"
trainer_id_to_name[BROCK] = "Brock"
trainer_id_to_name[MISTY] = "Misty"
trainer_id_to_name[LT_SURGE] = "Lt. Surge"
trainer_id_to_name[ERIKA] = "Erika"
trainer_id_to_name[KOGA] = "Koga"
trainer_id_to_name[BLAINE] = "Blaine"
trainer_id_to_name[SABRINA] = "Sabrina"
trainer_id_to_name[GENTLEMAN] = "Gentleman"
trainer_id_to_name[LORELEI] = "Lorelei"
trainer_id_to_name[CHANNELER] = "Channeler"
trainer_id_to_name[AGATHA] = "Agatha"
trainer_id_to_name[LANCE] = "Lance"

# type constants
NUM_TYPES = 16 # we are including BIRD type if we want Missingno later

counter = 0
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

type_id_to_name = []
for i in range(NUM_TYPES):
  type_id_to_name.append('')
type_id_to_name[NORMAL] = "Normal"
type_id_to_name[FIGHTING] = "Fighting"
type_id_to_name[FLYING] = "Flying"
type_id_to_name[POISON] = "Poison"
type_id_to_name[GROUND] = "Ground"
type_id_to_name[ROCK] = "Rock"
type_id_to_name[BIRD] = "Bird"
type_id_to_name[BUG] = "Bug"
type_id_to_name[GHOST] = "Ghost"
type_id_to_name[FIRE] = "Fire"
type_id_to_name[WATER] = "Water"
type_id_to_name[GRASS] = "Grass"
type_id_to_name[ELECTRIC] = "Electric"
type_id_to_name[PSYCHIC_TYPE] = "Psychic"
type_id_to_name[ICE] = "Ice"
type_id_to_name[DRAGON] = "Dragon"

# type matchup constants
NO_EFFECT = 0
NOT_VERY_EFFECTIVE = 0.5
EFFECTIVE = 1
MORE_EFFECTIVE = 1.5
SUPER_EFFECTIVE = 2

# type_matchup[TYPE1][TYPE2] is one of the former four constants
type_matchup = []
# construct initial type chart
for i in range(NUM_TYPES):
  # initialize type_matchup[i]
  type_matchup.append([])
  for j in range(NUM_TYPES):
    # initialize type_matchup[i][j] as EFFECTIVE, may be changed later
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