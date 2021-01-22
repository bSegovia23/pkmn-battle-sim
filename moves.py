import consts
from consts import auto, counter, NUM_MOVE_DATA_FIELDS, MOVE_NAME, EFFECT, POWER, MOVE_TYPE, ACCURACY, PP, NORMAL, FIGHTING, FLYING, POISON, GROUND, ROCK, BUG, GHOST, FIRE, WATER, GRASS, ELECTRIC, PSYCHIC_TYPE, ICE, DRAGON

# move constants
NUM_MOVES = 166
consts.counter = 0
NO_MOVE = auto()
POUND = auto()
KARATE_CHOP = auto()
DOUBLESLAP = auto()
COMET_PUNCH = auto()
MEGA_PUNCH = auto()
PAY_DAY = auto()
FIRE_PUNCH = auto()
ICE_PUNCH = auto()
THUNDERPUNCH = auto()
SCRATCH = auto()
VICEGRIP = auto()
GUILLOTINE = auto()
RAZOR_WIND = auto()
SWORDS_DANCE = auto()
CUT = auto()
GUST = auto()
WING_ATTACK = auto()
WHIRLWIND = auto()
FLY = auto()
BIND = auto()
SLAM = auto()
VINE_WHIP = auto()
STOMP = auto()
DOUBLE_KICK = auto()
MEGA_KICK = auto()
JUMP_KICK = auto()
ROLLING_KICK = auto()
SAND_ATTACK = auto()
HEADBUTT = auto()
HORN_ATTACK = auto()
FURY_ATTACK = auto()
HORN_DRILL = auto()
TACKLE = auto()
BODY_SLAM = auto()
WRAP = auto()
TAKE_DOWN = auto()
THRASH = auto()
DOUBLE_EDGE = auto()
TAIL_WHIP = auto()
POISON_STING = auto()
TWINEEDLE = auto()
PIN_MISSILE = auto()
LEER = auto()
BITE = auto()
GROWL = auto()
ROAR = auto()
SING = auto()
SUPERSONIC = auto()
SONICBOOM = auto()
DISABLE = auto()
ACID = auto()
EMBER = auto()
FLAMETHROWER = auto()
MIST = auto()
WATER_GUN = auto()
HYDRO_PUMP = auto()
SURF = auto()
ICE_BEAM = auto()
BLIZZARD = auto()
PSYBEAM = auto()
BUBBLEBEAM = auto()
AURORA_BEAM = auto()
HYPER_BEAM = auto()
PECK = auto()
DRILL_PECK = auto()
SUBMISSION = auto()
LOW_KICK = auto()
COUNTER = auto()
SEISMIC_TOSS = auto()
STRENGTH = auto()
ABSORB = auto()
MEGA_DRAIN = auto()
LEECH_SEED = auto()
GROWTH = auto()
RAZOR_LEAF = auto()
SOLARBEAM = auto()
POISONPOWDER = auto()
STUN_SPORE = auto()
SLEEP_POWDER = auto()
PETAL_DANCE = auto()
STRING_SHOT = auto()
DRAGON_RAGE = auto()
FIRE_SPIN = auto()
THUNDERSHOCK = auto()
THUNDERBOLT = auto()
THUNDER_WAVE = auto()
THUNDER = auto()
ROCK_THROW = auto()
EARTHQUAKE = auto()
FISSURE = auto()
DIG = auto()
TOXIC = auto()
CONFUSION = auto()
PSYCHIC_M = auto()
HYPNOSIS = auto()
MEDITATE = auto()
AGILITY = auto()
QUICK_ATTACK = auto()
RAGE = auto()
TELEPORT = auto()
NIGHT_SHADE = auto()
MIMIC = auto()
SCREECH = auto()
DOUBLE_TEAM = auto()
RECOVER = auto()
HARDEN = auto()
MINIMIZE = auto()
SMOKESCREEN = auto()
CONFUSE_RAY = auto()
WITHDRAW = auto()
DEFENSE_CURL = auto()
BARRIER = auto()
LIGHT_SCREEN = auto()
HAZE = auto()
REFLECT = auto()
FOCUS_ENERGY = auto()
BIDE = auto()
METRONOME = auto()
MIRROR_MOVE = auto()
SELFDESTRUCT = auto()
EGG_BOMB = auto()
LICK = auto()
SMOG = auto()
SLUDGE = auto()
BONE_CLUB = auto()
FIRE_BLAST = auto()
WATERFALL = auto()
CLAMP = auto()
SWIFT = auto()
SKULL_BASH = auto()
SPIKE_CANNON = auto()
CONSTRICT = auto()
AMNESIA = auto()
KINESIS = auto()
SOFTBOILED = auto()
HI_JUMP_KICK = auto()
GLARE = auto()
DREAM_EATER = auto()
POISON_GAS = auto()
BARRAGE = auto()
LEECH_LIFE = auto()
LOVELY_KISS = auto()
SKY_ATTACK = auto()
TRANSFORM = auto()
BUBBLE = auto()
DIZZY_PUNCH = auto()
SPORE = auto()
FLASH = auto()
PSYWAVE = auto()
SPLASH = auto()
ACID_ARMOR = auto()
CRABHAMMER = auto()
EXPLOSION = auto()
FURY_SWIPES = auto()
BONEMERANG = auto()
REST = auto()
ROCK_SLIDE = auto()
HYPER_FANG = auto()
SHARPEN = auto()
CONVERSION = auto()
TRI_ATTACK = auto()
SUPER_FANG = auto()
SLASH = auto()
SUBSTITUTE = auto()
STRUGGLE = auto()

# move effect constants
counter = 0
NO_ADDITIONAL_EFFECT = auto()
EFFECT_01 = auto() # unused
POISON_SIDE_EFFECT1 = auto()
DRAIN_HP_EFFECT = auto()
BURN_SIDE_EFFECT1 = auto()
FREEZE_SIDE_EFFECT = auto()
PARALYZE_SIDE_EFFECT1 = auto()
EXPLODE_EFFECT = auto()
DREAM_EATER_EFFECT = auto()
MIRROR_MOVE_EFFECT = auto()
ATTACK_UP1_EFFECT = auto()
DEFENSE_UP1_EFFECT = auto()
SPEED_UP1_EFFECT = auto()
SPECIAL_UP1_EFFECT = auto()
ACCURACY_UP1_EFFECT = auto()
EVASION_UP1_EFFECT = auto()
PAY_DAY_EFFECT = auto()
SWIFT_EFFECT = auto()
ATTACK_DOWN1_EFFECT = auto()
DEFENSE_DOWN1_EFFECT = auto()
SPEED_DOWN1_EFFECT = auto()
SPECIAL_DOWN1_EFFECT = auto()
ACCURACY_DOWN1_EFFECT = auto()
EVASION_DOWN1_EFFECT = auto()
CONVERSION_EFFECT = auto()
HAZE_EFFECT = auto()
BIDE_EFFECT = auto()
THRASH_PETAL_DANCE_EFFECT = auto()
SWITCH_AND_TELEPORT_EFFECT = auto()
TWO_TO_FIVE_ATTACKS_EFFECT = auto()
EFFECT_1E = auto() # unused
FLINCH_SIDE_EFFECT1 = auto()
SLEEP_EFFECT = auto()
POISON_SIDE_EFFECT2 = auto()
BURN_SIDE_EFFECT2 = auto()
PARALYZE_SIDE_EFFECT2 = auto()
FLINCH_SIDE_EFFECT2 = auto()
OHKO_EFFECT = auto()
CHARGE_EFFECT = auto()
SUPER_FANG_EFFECT = auto()
SPECIAL_DAMAGE_EFFECT = auto()
TRAPPING_EFFECT = auto()
FLY_EFFECT = auto()
ATTACK_TWICE_EFFECT = auto()
JUMP_KICK_EFFECT = auto()
MIST_EFFECT = auto()
FOCUS_ENERGY_EFFECT = auto()
RECOIL_EFFECT = auto()
CONFUSION_EFFECT = auto()
ATTACK_UP2_EFFECT = auto()
DEFENSE_UP2_EFFECT = auto()
SPEED_UP2_EFFECT = auto()
SPECIAL_UP2_EFFECT = auto()
ACCURACY_UP2_EFFECT = auto()
EVASION_UP2_EFFECT = auto()
HEAL_EFFECT = auto()
TRANSFORM_EFFECT = auto()
ATTACK_DOWN2_EFFECT = auto()
DEFENSE_DOWN2_EFFECT = auto()
SPEED_DOWN2_EFFECT = auto()
SPECIAL_DOWN2_EFFECT = auto()
ACCURACY_DOWN2_EFFECT = auto()
EVASION_DOWN2_EFFECT = auto()
LIGHT_SCREEN_EFFECT = auto()
REFLECT_EFFECT = auto()
POISON_EFFECT = auto()
PARALYZE_EFFECT = auto()
ATTACK_DOWN_SIDE_EFFECT = auto()
DEFENSE_DOWN_SIDE_EFFECT = auto()
SPEED_DOWN_SIDE_EFFECT = auto()
SPECIAL_DOWN_SIDE_EFFECT = auto()
CONFUSION_SIDE_EFFECT = auto()
TWINEEDLE_EFFECT = auto()
SUBSTITUTE_EFFECT = auto()
HYPER_BEAM_EFFECT = auto()
RAGE_EFFECT = auto()
MIMIC_EFFECT = auto()
METRONOME_EFFECT = auto()
LEECH_SEED_EFFECT = auto()
SPLASH_EFFECT = auto()
DISABLE_EFFECT = auto()

# initialize move table
move_table = []
# construct initial move table
for i in range(NUM_MOVES):
  move_table.append([])
  for j in range(NUM_MOVE_DATA_FIELDS):
    move_table[i].append('')

move_table[NO_MOVE][MOVE_NAME] = "---"

move_table[POUND][MOVE_NAME] = "Pound"
move_table[POUND][EFFECT] = NO_ADDITIONAL_EFFECT
move_table[POUND][POWER] = 40
move_table[POUND][MOVE_TYPE] = NORMAL
move_table[POUND][ACCURACY] = 100
move_table[POUND][PP] = 35

move_table[KARATE_CHOP][MOVE_NAME] = "Karate Chop"
move_table[KARATE_CHOP][EFFECT] = NO_ADDITIONAL_EFFECT
move_table[KARATE_CHOP][POWER] = 50
move_table[KARATE_CHOP][MOVE_TYPE] = NORMAL
move_table[KARATE_CHOP][ACCURACY] = 100
move_table[KARATE_CHOP][PP] = 25

move_table[DOUBLESLAP][MOVE_NAME] = "Doubleslap"
move_table[DOUBLESLAP][EFFECT] = TWO_TO_FIVE_ATTACKS_EFFECT
move_table[DOUBLESLAP][POWER] = 15
move_table[DOUBLESLAP][MOVE_TYPE] = NORMAL
move_table[DOUBLESLAP][ACCURACY] = 85
move_table[DOUBLESLAP][PP] = 10

move_table[COMET_PUNCH][MOVE_NAME] = "Comet Punch"
move_table[COMET_PUNCH][EFFECT] = TWO_TO_FIVE_ATTACKS_EFFECT
move_table[COMET_PUNCH][POWER] = 18
move_table[COMET_PUNCH][MOVE_TYPE] = NORMAL
move_table[COMET_PUNCH][ACCURACY] = 85
move_table[COMET_PUNCH][PP] = 15

move_table[MEGA_PUNCH][MOVE_NAME] = "Mega Punch"
move_table[MEGA_PUNCH][EFFECT] = NO_ADDITIONAL_EFFECT
move_table[MEGA_PUNCH][POWER] = 80
move_table[MEGA_PUNCH][MOVE_TYPE] = NORMAL
move_table[MEGA_PUNCH][ACCURACY] = 85
move_table[MEGA_PUNCH][PP] = 20

move_table[PAY_DAY][MOVE_NAME] = "Pay Day"
move_table[PAY_DAY][EFFECT] = PAY_DAY_EFFECT
move_table[PAY_DAY][POWER] = 40
move_table[PAY_DAY][MOVE_TYPE] = NORMAL
move_table[PAY_DAY][ACCURACY] = 100
move_table[PAY_DAY][PP] = 20

move_table[FIRE_PUNCH][MOVE_NAME] = "Fire Punch"
move_table[FIRE_PUNCH][EFFECT] = BURN_SIDE_EFFECT1
move_table[FIRE_PUNCH][POWER] = 75
move_table[FIRE_PUNCH][MOVE_TYPE] = FIRE
move_table[FIRE_PUNCH][ACCURACY] = 100
move_table[FIRE_PUNCH][PP] = 15

move_table[ICE_PUNCH][MOVE_NAME] = "Ice Punch"
move_table[ICE_PUNCH][EFFECT] = FREEZE_SIDE_EFFECT
move_table[ICE_PUNCH][POWER] = 75
move_table[ICE_PUNCH][MOVE_TYPE] = ICE
move_table[ICE_PUNCH][ACCURACY] = 100
move_table[ICE_PUNCH][PP] = 15

move_table[THUNDERPUNCH][MOVE_NAME] = "ThunderPunch"
move_table[THUNDERPUNCH][EFFECT] = PARALYZE_SIDE_EFFECT1
move_table[THUNDERPUNCH][POWER] = 75
move_table[THUNDERPUNCH][MOVE_TYPE] = ELECTRIC
move_table[THUNDERPUNCH][ACCURACY] = 100
move_table[THUNDERPUNCH][PP] = 15

move_table[SCRATCH][MOVE_NAME] = "Scratch"
move_table[SCRATCH][EFFECT] = NO_ADDITIONAL_EFFECT
move_table[SCRATCH][POWER] = 40
move_table[SCRATCH][MOVE_TYPE] = NORMAL
move_table[SCRATCH][ACCURACY] = 100
move_table[SCRATCH][PP] = 35

move_table[VICEGRIP][MOVE_NAME] = "Vicegrip"
move_table[VICEGRIP][EFFECT] = NO_ADDITIONAL_EFFECT
move_table[VICEGRIP][POWER] = 55
move_table[VICEGRIP][MOVE_TYPE] = NORMAL
move_table[VICEGRIP][ACCURACY] = 100
move_table[VICEGRIP][PP] = 30

move_table[GUILLOTINE][MOVE_NAME] = "Guillotine"
move_table[GUILLOTINE][EFFECT] = OHKO_EFFECT
move_table[GUILLOTINE][POWER] = 1
move_table[GUILLOTINE][MOVE_TYPE] = NORMAL
move_table[GUILLOTINE][ACCURACY] = 30
move_table[GUILLOTINE][PP] = 5

move_table[RAZOR_WIND][MOVE_NAME] = "Razor Wind"
move_table[RAZOR_WIND][EFFECT] = CHARGE_EFFECT
move_table[RAZOR_WIND][POWER] = 80
move_table[RAZOR_WIND][MOVE_TYPE] = NORMAL
move_table[RAZOR_WIND][ACCURACY] = 75
move_table[RAZOR_WIND][PP] = 10

move_table[SWORDS_DANCE][MOVE_NAME] = "Swords Dance"
move_table[SWORDS_DANCE][EFFECT] = ATTACK_UP2_EFFECT
move_table[SWORDS_DANCE][POWER] = 0
move_table[SWORDS_DANCE][MOVE_TYPE] = NORMAL
move_table[SWORDS_DANCE][ACCURACY] = 100
move_table[SWORDS_DANCE][PP] = 30

move_table[CUT][MOVE_NAME] = "Cut"
move_table[CUT][EFFECT] = NO_ADDITIONAL_EFFECT
move_table[CUT][POWER] = 50
move_table[CUT][MOVE_TYPE] = NORMAL
move_table[CUT][ACCURACY] = 95
move_table[CUT][PP] = 30

move_table[GUST][MOVE_NAME] = "Gust"
move_table[GUST][EFFECT] = NO_ADDITIONAL_EFFECT
move_table[GUST][POWER] = 40
move_table[GUST][MOVE_TYPE] = NORMAL
move_table[GUST][ACCURACY] = 100
move_table[GUST][PP] = 35

move_table[WING_ATTACK][MOVE_NAME] = "Wing Attack"
move_table[WING_ATTACK][EFFECT] = NO_ADDITIONAL_EFFECT
move_table[WING_ATTACK][POWER] = 35
move_table[WING_ATTACK][MOVE_TYPE] = FLYING
move_table[WING_ATTACK][ACCURACY] = 100
move_table[WING_ATTACK][PP] = 35

move_table[WHIRLWIND][MOVE_NAME] = "Whirlwind"
move_table[WHIRLWIND][EFFECT] = SWITCH_AND_TELEPORT_EFFECT
move_table[WHIRLWIND][POWER] = 0
move_table[WHIRLWIND][MOVE_TYPE] = NORMAL
move_table[WHIRLWIND][ACCURACY] = 85
move_table[WHIRLWIND][PP] = 20

move_table[FLY][MOVE_NAME] = "Fly"
move_table[FLY][EFFECT] = FLY_EFFECT
move_table[FLY][POWER] = 70
move_table[FLY][MOVE_TYPE] = FLYING
move_table[FLY][ACCURACY] = 95
move_table[FLY][PP] = 15

move_table[BIND][MOVE_NAME] = "Bind"
move_table[BIND][EFFECT] = TRAPPING_EFFECT
move_table[BIND][POWER] = 15
move_table[BIND][MOVE_TYPE] = NORMAL
move_table[BIND][ACCURACY] = 75
move_table[BIND][PP] = 20

move_table[SLAM][MOVE_NAME] = "Slam"
move_table[SLAM][EFFECT] = NO_ADDITIONAL_EFFECT
move_table[SLAM][POWER] = 80
move_table[SLAM][MOVE_TYPE] = NORMAL
move_table[SLAM][ACCURACY] = 75
move_table[SLAM][PP] = 20

move_table[VINE_WHIP][MOVE_NAME] = "Vine Whip"
move_table[VINE_WHIP][EFFECT] = NO_ADDITIONAL_EFFECT
move_table[VINE_WHIP][POWER] = 35
move_table[VINE_WHIP][MOVE_TYPE] = GRASS
move_table[VINE_WHIP][ACCURACY] = 100
move_table[VINE_WHIP][PP] = 10

move_table[STOMP][MOVE_NAME] = "Stomp"
move_table[STOMP][EFFECT] = FLINCH_SIDE_EFFECT2
move_table[STOMP][POWER] = 65
move_table[STOMP][MOVE_TYPE] = NORMAL
move_table[STOMP][ACCURACY] = 100
move_table[STOMP][PP] = 20

move_table[DOUBLE_KICK][MOVE_NAME] = "Double Kick"
move_table[DOUBLE_KICK][EFFECT] = ATTACK_TWICE_EFFECT
move_table[DOUBLE_KICK][POWER] = 30
move_table[DOUBLE_KICK][MOVE_TYPE] = FIGHTING
move_table[DOUBLE_KICK][ACCURACY] = 100
move_table[DOUBLE_KICK][PP] = 30

move_table[MEGA_KICK][MOVE_NAME] = "Mega Kick"
move_table[MEGA_KICK][EFFECT] = NO_ADDITIONAL_EFFECT
move_table[MEGA_KICK][POWER] = 120
move_table[MEGA_KICK][MOVE_TYPE] = NORMAL
move_table[MEGA_KICK][ACCURACY] = 75
move_table[MEGA_KICK][PP] = 5

move_table[JUMP_KICK][MOVE_NAME] = "Jump Kick"
move_table[JUMP_KICK][EFFECT] = JUMP_KICK_EFFECT
move_table[JUMP_KICK][POWER] = 70
move_table[JUMP_KICK][MOVE_TYPE] = FIGHTING
move_table[JUMP_KICK][ACCURACY] = 95
move_table[JUMP_KICK][PP] = 25

move_table[ROLLING_KICK][MOVE_NAME] = "Rolling Kick"
move_table[ROLLING_KICK][EFFECT] = FLINCH_SIDE_EFFECT2
move_table[ROLLING_KICK][POWER] = 60
move_table[ROLLING_KICK][MOVE_TYPE] = FIGHTING
move_table[ROLLING_KICK][ACCURACY] = 85
move_table[ROLLING_KICK][PP] = 15

move_table[SAND_ATTACK][MOVE_NAME] = "Sand Attack"
move_table[SAND_ATTACK][EFFECT] = ACCURACY_DOWN1_EFFECT
move_table[SAND_ATTACK][POWER] = 0
move_table[SAND_ATTACK][MOVE_TYPE] = NORMAL
move_table[SAND_ATTACK][ACCURACY] = 100
move_table[SAND_ATTACK][PP] = 15

move_table[HEADBUTT][MOVE_NAME] = "Headbutt"
move_table[HEADBUTT][EFFECT] = FLINCH_SIDE_EFFECT2
move_table[HEADBUTT][POWER] = 70
move_table[HEADBUTT][MOVE_TYPE] = NORMAL
move_table[HEADBUTT][ACCURACY] = 100
move_table[HEADBUTT][PP] = 15

move_table[HORN_ATTACK][MOVE_NAME] = "Horn Attack"
move_table[HORN_ATTACK][EFFECT] = NO_ADDITIONAL_EFFECT
move_table[HORN_ATTACK][POWER] = 65
move_table[HORN_ATTACK][MOVE_TYPE] = NORMAL
move_table[HORN_ATTACK][ACCURACY] = 100
move_table[HORN_ATTACK][PP] = 25

move_table[FURY_ATTACK][MOVE_NAME] = "Fury Attack"
move_table[FURY_ATTACK][EFFECT] = TWO_TO_FIVE_ATTACKS_EFFECT
move_table[FURY_ATTACK][POWER] = 15
move_table[FURY_ATTACK][MOVE_TYPE] = NORMAL
move_table[FURY_ATTACK][ACCURACY] = 85
move_table[FURY_ATTACK][PP] = 20

move_table[HORN_DRILL][MOVE_NAME] = "Horn Drill"
move_table[HORN_DRILL][EFFECT] = OHKO_EFFECT
move_table[HORN_DRILL][POWER] = 1
move_table[HORN_DRILL][MOVE_TYPE] = NORMAL
move_table[HORN_DRILL][ACCURACY] = 30
move_table[HORN_DRILL][PP] = 5

move_table[TACKLE][MOVE_NAME] = "Tackle"
move_table[TACKLE][EFFECT] = NO_ADDITIONAL_EFFECT
move_table[TACKLE][POWER] = 35
move_table[TACKLE][MOVE_TYPE] = NORMAL
move_table[TACKLE][ACCURACY] = 95
move_table[TACKLE][PP] = 35

move_table[BODY_SLAM][MOVE_NAME] = "Body Slam"
move_table[BODY_SLAM][EFFECT] = PARALYZE_SIDE_EFFECT2
move_table[BODY_SLAM][POWER] = 85
move_table[BODY_SLAM][MOVE_TYPE] = NORMAL
move_table[BODY_SLAM][ACCURACY] = 100
move_table[BODY_SLAM][PP] = 15

move_table[WRAP][MOVE_NAME] = "Wrap"
move_table[WRAP][EFFECT] = TRAPPING_EFFECT
move_table[WRAP][POWER] = 15
move_table[WRAP][MOVE_TYPE] = NORMAL
move_table[WRAP][ACCURACY] = 85
move_table[WRAP][PP] = 20

move_table[TAKE_DOWN][MOVE_NAME] = "Take Down"
move_table[TAKE_DOWN][EFFECT] = RECOIL_EFFECT
move_table[TAKE_DOWN][POWER] = 90
move_table[TAKE_DOWN][MOVE_TYPE] = NORMAL
move_table[TAKE_DOWN][ACCURACY] = 85
move_table[TAKE_DOWN][PP] = 20

move_table[THRASH][MOVE_NAME] = "Thrash"
move_table[THRASH][EFFECT] = THRASH_PETAL_DANCE_EFFECT
move_table[THRASH][POWER] = 90
move_table[THRASH][MOVE_TYPE] = NORMAL
move_table[THRASH][ACCURACY] = 100
move_table[THRASH][PP] = 20

move_table[DOUBLE_EDGE][MOVE_NAME] = "Double Edge"
move_table[DOUBLE_EDGE][EFFECT] = RECOIL_EFFECT
move_table[DOUBLE_EDGE][POWER] = 100
move_table[DOUBLE_EDGE][MOVE_TYPE] = NORMAL
move_table[DOUBLE_EDGE][ACCURACY] = 100
move_table[DOUBLE_EDGE][PP] = 15

move_table[TAIL_WHIP][MOVE_NAME] = "Tail Whip"
move_table[TAIL_WHIP][EFFECT] = DEFENSE_DOWN1_EFFECT
move_table[TAIL_WHIP][POWER] = 0
move_table[TAIL_WHIP][MOVE_TYPE] = NORMAL
move_table[TAIL_WHIP][ACCURACY] = 100
move_table[TAIL_WHIP][PP] = 30

move_table[POISON_STING][MOVE_NAME] = "Poison Sting"
move_table[POISON_STING][EFFECT] = POISON_SIDE_EFFECT1
move_table[POISON_STING][POWER] = 15
move_table[POISON_STING][MOVE_TYPE] = POISON
move_table[POISON_STING][ACCURACY] = 100
move_table[POISON_STING][PP] = 35

move_table[TWINEEDLE][MOVE_NAME] = "Twineedle"
move_table[TWINEEDLE][EFFECT] = TWINEEDLE_EFFECT
move_table[TWINEEDLE][POWER] = 25
move_table[TWINEEDLE][MOVE_TYPE] = BUG
move_table[TWINEEDLE][ACCURACY] = 100
move_table[TWINEEDLE][PP] = 20

move_table[PIN_MISSILE][MOVE_NAME] = "Pin Missile"
move_table[PIN_MISSILE][EFFECT] = TWO_TO_FIVE_ATTACKS_EFFECT
move_table[PIN_MISSILE][POWER] = 14
move_table[PIN_MISSILE][MOVE_TYPE] = BUG
move_table[PIN_MISSILE][ACCURACY] = 85
move_table[PIN_MISSILE][PP] = 20

move_table[LEER][MOVE_NAME] = "Leer"
move_table[LEER][EFFECT] = DEFENSE_DOWN1_EFFECT
move_table[LEER][POWER] = 0
move_table[LEER][MOVE_TYPE] = NORMAL
move_table[LEER][ACCURACY] = 100
move_table[LEER][PP] = 30

move_table[BITE][MOVE_NAME] = "Bite"
move_table[BITE][EFFECT] = FLINCH_SIDE_EFFECT1
move_table[BITE][POWER] = 60
move_table[BITE][MOVE_TYPE] = NORMAL
move_table[BITE][ACCURACY] = 100
move_table[BITE][PP] = 25

move_table[GROWL][MOVE_NAME] = "Growl"
move_table[GROWL][EFFECT] = ATTACK_DOWN1_EFFECT
move_table[GROWL][POWER] = 0
move_table[GROWL][MOVE_TYPE] = NORMAL
move_table[GROWL][ACCURACY] = 100
move_table[GROWL][PP] = 40

move_table[ROAR][MOVE_NAME] = "Roar"
move_table[ROAR][EFFECT] = SWITCH_AND_TELEPORT_EFFECT
move_table[ROAR][POWER] = 0
move_table[ROAR][MOVE_TYPE] = NORMAL
move_table[ROAR][ACCURACY] = 100
move_table[ROAR][PP] = 20

move_table[SING][MOVE_NAME] = "Sing"
move_table[SING][EFFECT] = SLEEP_EFFECT
move_table[SING][POWER] = 0
move_table[SING][MOVE_TYPE] = NORMAL
move_table[SING][ACCURACY] = 55
move_table[SING][PP] = 15

move_table[SUPERSONIC][MOVE_NAME] = "Supersonic"
move_table[SUPERSONIC][EFFECT] = CONFUSION_EFFECT
move_table[SUPERSONIC][POWER] = 0
move_table[SUPERSONIC][MOVE_TYPE] = NORMAL
move_table[SUPERSONIC][ACCURACY] = 55
move_table[SUPERSONIC][PP] = 20

move_table[SONICBOOM][MOVE_NAME] = "Sonicboom"
move_table[SONICBOOM][EFFECT] = SPECIAL_DAMAGE_EFFECT
move_table[SONICBOOM][POWER] = 1
move_table[SONICBOOM][MOVE_TYPE] = NORMAL
move_table[SONICBOOM][ACCURACY] = 90
move_table[SONICBOOM][PP] = 20

move_table[DISABLE][MOVE_NAME] = "Disable"
move_table[DISABLE][EFFECT] = DISABLE_EFFECT
move_table[DISABLE][POWER] = 0
move_table[DISABLE][MOVE_TYPE] = NORMAL
move_table[DISABLE][ACCURACY] = 55
move_table[DISABLE][PP] = 20

move_table[ACID][MOVE_NAME] = "Acid"
move_table[ACID][EFFECT] = DEFENSE_DOWN_SIDE_EFFECT
move_table[ACID][POWER] = 40
move_table[ACID][MOVE_TYPE] = POISON
move_table[ACID][ACCURACY] = 100
move_table[ACID][PP] = 30

move_table[EMBER][MOVE_NAME] = "Ember"
move_table[EMBER][EFFECT] = BURN_SIDE_EFFECT1
move_table[EMBER][POWER] = 40
move_table[EMBER][MOVE_TYPE] = FIRE
move_table[EMBER][ACCURACY] = 100
move_table[EMBER][PP] = 25

move_table[FLAMETHROWER][MOVE_NAME] = "Flamethrower"
move_table[FLAMETHROWER][EFFECT] = BURN_SIDE_EFFECT1
move_table[FLAMETHROWER][POWER] = 95
move_table[FLAMETHROWER][MOVE_TYPE] = FIRE
move_table[FLAMETHROWER][ACCURACY] = 100
move_table[FLAMETHROWER][PP] = 15

move_table[MIST][MOVE_NAME] = "Mist"
move_table[MIST][EFFECT] = MIST_EFFECT
move_table[MIST][POWER] = 0
move_table[MIST][MOVE_TYPE] = ICE
move_table[MIST][ACCURACY] = 100
move_table[MIST][PP] = 30

move_table[WATER_GUN][MOVE_NAME] = "Water Gun"
move_table[WATER_GUN][EFFECT] = NO_ADDITIONAL_EFFECT
move_table[WATER_GUN][POWER] = 40
move_table[WATER_GUN][MOVE_TYPE] = WATER
move_table[WATER_GUN][ACCURACY] = 100
move_table[WATER_GUN][PP] = 25

move_table[HYDRO_PUMP][MOVE_NAME] = "Hydro Pump"
move_table[HYDRO_PUMP][EFFECT] = NO_ADDITIONAL_EFFECT
move_table[HYDRO_PUMP][POWER] = 120
move_table[HYDRO_PUMP][MOVE_TYPE] = WATER
move_table[HYDRO_PUMP][ACCURACY] = 80
move_table[HYDRO_PUMP][PP] = 5

move_table[SURF][MOVE_NAME] = "Surf"
move_table[SURF][EFFECT] = NO_ADDITIONAL_EFFECT
move_table[SURF][POWER] = 95
move_table[SURF][MOVE_TYPE] = WATER
move_table[SURF][ACCURACY] = 100
move_table[SURF][PP] = 15

move_table[ICE_BEAM][MOVE_NAME] = "Ice Beam"
move_table[ICE_BEAM][EFFECT] = FREEZE_SIDE_EFFECT
move_table[ICE_BEAM][POWER] = 95
move_table[ICE_BEAM][MOVE_TYPE] = ICE
move_table[ICE_BEAM][ACCURACY] = 100
move_table[ICE_BEAM][PP] = 10

move_table[BLIZZARD][MOVE_NAME] = "Blizzard"
move_table[BLIZZARD][EFFECT] = FREEZE_SIDE_EFFECT
move_table[BLIZZARD][POWER] = 120
move_table[BLIZZARD][MOVE_TYPE] = ICE
move_table[BLIZZARD][ACCURACY] = 90
move_table[BLIZZARD][PP] = 5

move_table[PSYBEAM][MOVE_NAME] = "Psybeam"
move_table[PSYBEAM][EFFECT] = CONFUSION_SIDE_EFFECT
move_table[PSYBEAM][POWER] = 65
move_table[PSYBEAM][MOVE_TYPE] = PSYCHIC_TYPE
move_table[PSYBEAM][ACCURACY] = 100
move_table[PSYBEAM][PP] = 20

move_table[BUBBLEBEAM][MOVE_NAME] = "Bubblebeam"
move_table[BUBBLEBEAM][EFFECT] = SPEED_DOWN_SIDE_EFFECT
move_table[BUBBLEBEAM][POWER] = 65
move_table[BUBBLEBEAM][MOVE_TYPE] = WATER
move_table[BUBBLEBEAM][ACCURACY] = 100
move_table[BUBBLEBEAM][PP] = 20

move_table[AURORA_BEAM][MOVE_NAME] = "Aurora Beam"
move_table[AURORA_BEAM][EFFECT] = ATTACK_DOWN_SIDE_EFFECT
move_table[AURORA_BEAM][POWER] = 65
move_table[AURORA_BEAM][MOVE_TYPE] = ICE
move_table[AURORA_BEAM][ACCURACY] = 100
move_table[AURORA_BEAM][PP] = 20

move_table[HYPER_BEAM][MOVE_NAME] = "Hyper Beam"
move_table[HYPER_BEAM][EFFECT] = HYPER_BEAM_EFFECT
move_table[HYPER_BEAM][POWER] = 150
move_table[HYPER_BEAM][MOVE_TYPE] = NORMAL
move_table[HYPER_BEAM][ACCURACY] = 90
move_table[HYPER_BEAM][PP] = 5

move_table[PECK][MOVE_NAME] = "Peck"
move_table[PECK][EFFECT] = NO_ADDITIONAL_EFFECT
move_table[PECK][POWER] = 35
move_table[PECK][MOVE_TYPE] = FLYING
move_table[PECK][ACCURACY] = 100
move_table[PECK][PP] = 35

move_table[DRILL_PECK][MOVE_NAME] = "Drill Peck"
move_table[DRILL_PECK][EFFECT] = NO_ADDITIONAL_EFFECT
move_table[DRILL_PECK][POWER] = 80
move_table[DRILL_PECK][MOVE_TYPE] = FLYING
move_table[DRILL_PECK][ACCURACY] = 100
move_table[DRILL_PECK][PP] = 20

move_table[SUBMISSION][MOVE_NAME] = "Submission"
move_table[SUBMISSION][EFFECT] = RECOIL_EFFECT
move_table[SUBMISSION][POWER] = 80
move_table[SUBMISSION][MOVE_TYPE] = FIGHTING
move_table[SUBMISSION][ACCURACY] = 80
move_table[SUBMISSION][PP] = 25

move_table[LOW_KICK][MOVE_NAME] = "Low Kick"
move_table[LOW_KICK][EFFECT] = FLINCH_SIDE_EFFECT2
move_table[LOW_KICK][POWER] = 50
move_table[LOW_KICK][MOVE_TYPE] = FIGHTING
move_table[LOW_KICK][ACCURACY] = 90
move_table[LOW_KICK][PP] = 20

move_table[COUNTER][MOVE_NAME] = "Counter"
move_table[COUNTER][EFFECT] = NO_ADDITIONAL_EFFECT
move_table[COUNTER][POWER] = 1
move_table[COUNTER][MOVE_TYPE] = FIGHTING
move_table[COUNTER][ACCURACY] = 100
move_table[COUNTER][PP] = 20

move_table[SEISMIC_TOSS][MOVE_NAME] = "Seismic Toss"
move_table[SEISMIC_TOSS][EFFECT] = SPECIAL_DAMAGE_EFFECT
move_table[SEISMIC_TOSS][POWER] = 1
move_table[SEISMIC_TOSS][MOVE_TYPE] = FIGHTING
move_table[SEISMIC_TOSS][ACCURACY] = 100
move_table[SEISMIC_TOSS][PP] = 20

move_table[STRENGTH][MOVE_NAME] = "Strength"
move_table[STRENGTH][EFFECT] = NO_ADDITIONAL_EFFECT
move_table[STRENGTH][POWER] = 80
move_table[STRENGTH][MOVE_TYPE] = NORMAL
move_table[STRENGTH][ACCURACY] = 100
move_table[STRENGTH][PP] = 15

move_table[ABSORB][MOVE_NAME] = "Absorb"
move_table[ABSORB][EFFECT] = DRAIN_HP_EFFECT
move_table[ABSORB][POWER] = 20
move_table[ABSORB][MOVE_TYPE] = GRASS
move_table[ABSORB][ACCURACY] = 100
move_table[ABSORB][PP] = 20

move_table[MEGA_DRAIN][MOVE_NAME] = "Mega Drain"
move_table[MEGA_DRAIN][EFFECT] = DRAIN_HP_EFFECT
move_table[MEGA_DRAIN][POWER] = 40
move_table[MEGA_DRAIN][MOVE_TYPE] = GRASS
move_table[MEGA_DRAIN][ACCURACY] = 100
move_table[MEGA_DRAIN][PP] = 10

move_table[LEECH_SEED][MOVE_NAME] = "Leech Seed"
move_table[LEECH_SEED][EFFECT] = LEECH_SEED_EFFECT
move_table[LEECH_SEED][POWER] = 0
move_table[LEECH_SEED][MOVE_TYPE] = GRASS
move_table[LEECH_SEED][ACCURACY] = 90
move_table[LEECH_SEED][PP] = 10

move_table[GROWTH][MOVE_NAME] = "Growth"
move_table[GROWTH][EFFECT] = SPECIAL_UP1_EFFECT
move_table[GROWTH][POWER] = 0
move_table[GROWTH][MOVE_TYPE] = NORMAL
move_table[GROWTH][ACCURACY] = 100
move_table[GROWTH][PP] = 40

move_table[RAZOR_LEAF][MOVE_NAME] = "Razor Leaf"
move_table[RAZOR_LEAF][EFFECT] = NO_ADDITIONAL_EFFECT
move_table[RAZOR_LEAF][POWER] = 55
move_table[RAZOR_LEAF][MOVE_TYPE] = GRASS
move_table[RAZOR_LEAF][ACCURACY] = 95
move_table[RAZOR_LEAF][PP] = 25

move_table[SOLARBEAM][MOVE_NAME] = "Solarbeam"
move_table[SOLARBEAM][EFFECT] = CHARGE_EFFECT
move_table[SOLARBEAM][POWER] = 120
move_table[SOLARBEAM][MOVE_TYPE] = GRASS
move_table[SOLARBEAM][ACCURACY] = 100
move_table[SOLARBEAM][PP] = 10

move_table[POISONPOWDER][MOVE_NAME] = "Poisonpowder"
move_table[POISONPOWDER][EFFECT] = POISON_EFFECT
move_table[POISONPOWDER][POWER] = 0
move_table[POISONPOWDER][MOVE_TYPE] = POISON
move_table[POISONPOWDER][ACCURACY] = 75
move_table[POISONPOWDER][PP] = 35

move_table[STUN_SPORE][MOVE_NAME] = "Stun Spore"
move_table[STUN_SPORE][EFFECT] = PARALYZE_EFFECT
move_table[STUN_SPORE][POWER] = 0
move_table[STUN_SPORE][MOVE_TYPE] = GRASS
move_table[STUN_SPORE][ACCURACY] = 75
move_table[STUN_SPORE][PP] = 30

move_table[SLEEP_POWDER][MOVE_NAME] = "Sleep Powder"
move_table[SLEEP_POWDER][EFFECT] = SLEEP_EFFECT
move_table[SLEEP_POWDER][POWER] = 0
move_table[SLEEP_POWDER][MOVE_TYPE] = GRASS
move_table[SLEEP_POWDER][ACCURACY] = 75
move_table[SLEEP_POWDER][PP] = 15

move_table[PETAL_DANCE][MOVE_NAME] = "Petal Dance"
move_table[PETAL_DANCE][EFFECT] = THRASH_PETAL_DANCE_EFFECT
move_table[PETAL_DANCE][POWER] = 70
move_table[PETAL_DANCE][MOVE_TYPE] = GRASS
move_table[PETAL_DANCE][ACCURACY] = 100
move_table[PETAL_DANCE][PP] = 20

move_table[STRING_SHOT][MOVE_NAME] = "String Shot"
move_table[STRING_SHOT][EFFECT] = SPEED_DOWN1_EFFECT
move_table[STRING_SHOT][POWER] = 0
move_table[STRING_SHOT][MOVE_TYPE] = BUG
move_table[STRING_SHOT][ACCURACY] = 95
move_table[STRING_SHOT][PP] = 40

move_table[DRAGON_RAGE][MOVE_NAME] = "Dragon Rage"
move_table[DRAGON_RAGE][EFFECT] = SPECIAL_DAMAGE_EFFECT
move_table[DRAGON_RAGE][POWER] = 1
move_table[DRAGON_RAGE][MOVE_TYPE] = DRAGON
move_table[DRAGON_RAGE][ACCURACY] = 100
move_table[DRAGON_RAGE][PP] = 10

move_table[FIRE_SPIN][MOVE_NAME] = "Fire Spin"
move_table[FIRE_SPIN][EFFECT] = TRAPPING_EFFECT
move_table[FIRE_SPIN][POWER] = 15
move_table[FIRE_SPIN][MOVE_TYPE] = FIRE
move_table[FIRE_SPIN][ACCURACY] = 70
move_table[FIRE_SPIN][PP] = 15

move_table[THUNDERSHOCK][MOVE_NAME] = "Thundershock"
move_table[THUNDERSHOCK][EFFECT] = PARALYZE_SIDE_EFFECT1
move_table[THUNDERSHOCK][POWER] = 40
move_table[THUNDERSHOCK][MOVE_TYPE] = ELECTRIC
move_table[THUNDERSHOCK][ACCURACY] = 100
move_table[THUNDERSHOCK][PP] = 30

move_table[THUNDERBOLT][MOVE_NAME] = "Thunderbolt"
move_table[THUNDERBOLT][EFFECT] = PARALYZE_SIDE_EFFECT1
move_table[THUNDERBOLT][POWER] = 95
move_table[THUNDERBOLT][MOVE_TYPE] = ELECTRIC
move_table[THUNDERBOLT][ACCURACY] = 100
move_table[THUNDERBOLT][PP] = 15

move_table[THUNDER_WAVE][MOVE_NAME] = "Thunder Wave"
move_table[THUNDER_WAVE][EFFECT] = PARALYZE_EFFECT
move_table[THUNDER_WAVE][POWER] = 0
move_table[THUNDER_WAVE][MOVE_TYPE] = ELECTRIC
move_table[THUNDER_WAVE][ACCURACY] = 100
move_table[THUNDER_WAVE][PP] = 20

move_table[THUNDER][MOVE_NAME] = "Thunder"
move_table[THUNDER][EFFECT] = PARALYZE_SIDE_EFFECT1
move_table[THUNDER][POWER] = 120
move_table[THUNDER][MOVE_TYPE] = ELECTRIC
move_table[THUNDER][ACCURACY] = 70
move_table[THUNDER][PP] = 10

move_table[ROCK_THROW][MOVE_NAME] = "Rock Throw"
move_table[ROCK_THROW][EFFECT] = NO_ADDITIONAL_EFFECT
move_table[ROCK_THROW][POWER] = 50
move_table[ROCK_THROW][MOVE_TYPE] = ROCK
move_table[ROCK_THROW][ACCURACY] = 65
move_table[ROCK_THROW][PP] = 15

move_table[EARTHQUAKE][MOVE_NAME] = "Earthquake"
move_table[EARTHQUAKE][EFFECT] = NO_ADDITIONAL_EFFECT
move_table[EARTHQUAKE][POWER] = 100
move_table[EARTHQUAKE][MOVE_TYPE] = GROUND
move_table[EARTHQUAKE][ACCURACY] = 100
move_table[EARTHQUAKE][PP] = 10

move_table[FISSURE][MOVE_NAME] = "Fissure"
move_table[FISSURE][EFFECT] = OHKO_EFFECT
move_table[FISSURE][POWER] = 1
move_table[FISSURE][MOVE_TYPE] = GROUND
move_table[FISSURE][ACCURACY] = 30
move_table[FISSURE][PP] = 5

move_table[DIG][MOVE_NAME] = "Dig"
move_table[DIG][EFFECT] = CHARGE_EFFECT
move_table[DIG][POWER] = 100
move_table[DIG][MOVE_TYPE] = GROUND
move_table[DIG][ACCURACY] = 100
move_table[DIG][PP] = 10

move_table[TOXIC][MOVE_NAME] = "Toxic"
move_table[TOXIC][EFFECT] = POISON_EFFECT
move_table[TOXIC][POWER] = 0
move_table[TOXIC][MOVE_TYPE] = POISON
move_table[TOXIC][ACCURACY] = 85
move_table[TOXIC][PP] = 10

move_table[CONFUSION][MOVE_NAME] = "Confusion"
move_table[CONFUSION][EFFECT] = CONFUSION_SIDE_EFFECT
move_table[CONFUSION][POWER] = 50
move_table[CONFUSION][MOVE_TYPE] = PSYCHIC_TYPE
move_table[CONFUSION][ACCURACY] = 100
move_table[CONFUSION][PP] = 25

move_table[PSYCHIC_M][MOVE_NAME] = "Psychic M"
move_table[PSYCHIC_M][EFFECT] = SPECIAL_DOWN_SIDE_EFFECT
move_table[PSYCHIC_M][POWER] = 90
move_table[PSYCHIC_M][MOVE_TYPE] = PSYCHIC_TYPE
move_table[PSYCHIC_M][ACCURACY] = 100
move_table[PSYCHIC_M][PP] = 10

move_table[HYPNOSIS][MOVE_NAME] = "Hypnosis"
move_table[HYPNOSIS][EFFECT] = SLEEP_EFFECT
move_table[HYPNOSIS][POWER] = 0
move_table[HYPNOSIS][MOVE_TYPE] = PSYCHIC_TYPE
move_table[HYPNOSIS][ACCURACY] = 60
move_table[HYPNOSIS][PP] = 20

move_table[MEDITATE][MOVE_NAME] = "Meditate"
move_table[MEDITATE][EFFECT] = ATTACK_UP1_EFFECT
move_table[MEDITATE][POWER] = 0
move_table[MEDITATE][MOVE_TYPE] = PSYCHIC_TYPE
move_table[MEDITATE][ACCURACY] = 100
move_table[MEDITATE][PP] = 40

move_table[AGILITY][MOVE_NAME] = "Agility"
move_table[AGILITY][EFFECT] = SPEED_UP2_EFFECT
move_table[AGILITY][POWER] = 0
move_table[AGILITY][MOVE_TYPE] = PSYCHIC_TYPE
move_table[AGILITY][ACCURACY] = 100
move_table[AGILITY][PP] = 30

move_table[QUICK_ATTACK][MOVE_NAME] = "Quick Attack"
move_table[QUICK_ATTACK][EFFECT] = NO_ADDITIONAL_EFFECT
move_table[QUICK_ATTACK][POWER] = 40
move_table[QUICK_ATTACK][MOVE_TYPE] = NORMAL
move_table[QUICK_ATTACK][ACCURACY] = 100
move_table[QUICK_ATTACK][PP] = 30

move_table[RAGE][MOVE_NAME] = "Rage"
move_table[RAGE][EFFECT] = RAGE_EFFECT
move_table[RAGE][POWER] = 20
move_table[RAGE][MOVE_TYPE] = NORMAL
move_table[RAGE][ACCURACY] = 100
move_table[RAGE][PP] = 20

move_table[TELEPORT][MOVE_NAME] = "Teleport"
move_table[TELEPORT][EFFECT] = SWITCH_AND_TELEPORT_EFFECT
move_table[TELEPORT][POWER] = 0
move_table[TELEPORT][MOVE_TYPE] = PSYCHIC_TYPE
move_table[TELEPORT][ACCURACY] = 100
move_table[TELEPORT][PP] = 20

move_table[NIGHT_SHADE][MOVE_NAME] = "Night Shade"
move_table[NIGHT_SHADE][EFFECT] = SPECIAL_DAMAGE_EFFECT
move_table[NIGHT_SHADE][POWER] = 0
move_table[NIGHT_SHADE][MOVE_TYPE] = GHOST
move_table[NIGHT_SHADE][ACCURACY] = 100
move_table[NIGHT_SHADE][PP] = 15

move_table[MIMIC][MOVE_NAME] = "Mimic"
move_table[MIMIC][EFFECT] = MIMIC_EFFECT
move_table[MIMIC][POWER] = 0
move_table[MIMIC][MOVE_TYPE] = NORMAL
move_table[MIMIC][ACCURACY] = 100
move_table[MIMIC][PP] = 10

move_table[SCREECH][MOVE_NAME] = "Screech"
move_table[SCREECH][EFFECT] = DEFENSE_DOWN2_EFFECT
move_table[SCREECH][POWER] = 0
move_table[SCREECH][MOVE_TYPE] = NORMAL
move_table[SCREECH][ACCURACY] = 85
move_table[SCREECH][PP] = 40

move_table[DOUBLE_TEAM][MOVE_NAME] = "Double Team"
move_table[DOUBLE_TEAM][EFFECT] = EVASION_UP1_EFFECT
move_table[DOUBLE_TEAM][POWER] = 0
move_table[DOUBLE_TEAM][MOVE_TYPE] = NORMAL
move_table[DOUBLE_TEAM][ACCURACY] = 100
move_table[DOUBLE_TEAM][PP] = 15

move_table[RECOVER][MOVE_NAME] = "Recover"
move_table[RECOVER][EFFECT] = HEAL_EFFECT
move_table[RECOVER][POWER] = 0
move_table[RECOVER][MOVE_TYPE] = NORMAL
move_table[RECOVER][ACCURACY] = 100
move_table[RECOVER][PP] = 20

move_table[HARDEN][MOVE_NAME] = "Harden"
move_table[HARDEN][EFFECT] = DEFENSE_UP1_EFFECT
move_table[HARDEN][POWER] = 0
move_table[HARDEN][MOVE_TYPE] = NORMAL
move_table[HARDEN][ACCURACY] = 100
move_table[HARDEN][PP] = 30

move_table[MINIMIZE][MOVE_NAME] = "Minimize"
move_table[MINIMIZE][EFFECT] = EVASION_UP1_EFFECT
move_table[MINIMIZE][POWER] = 0
move_table[MINIMIZE][MOVE_TYPE] = NORMAL
move_table[MINIMIZE][ACCURACY] = 100
move_table[MINIMIZE][PP] = 20

move_table[SMOKESCREEN][MOVE_NAME] = "Smokescreen"
move_table[SMOKESCREEN][EFFECT] = ACCURACY_DOWN1_EFFECT
move_table[SMOKESCREEN][POWER] = 0
move_table[SMOKESCREEN][MOVE_TYPE] = NORMAL
move_table[SMOKESCREEN][ACCURACY] = 100
move_table[SMOKESCREEN][PP] = 20

move_table[CONFUSE_RAY][MOVE_NAME] = "Confuse Ray"
move_table[CONFUSE_RAY][EFFECT] = CONFUSION_EFFECT
move_table[CONFUSE_RAY][POWER] = 0
move_table[CONFUSE_RAY][MOVE_TYPE] = GHOST
move_table[CONFUSE_RAY][ACCURACY] = 100
move_table[CONFUSE_RAY][PP] = 10

move_table[WITHDRAW][MOVE_NAME] = "Withdraw"
move_table[WITHDRAW][EFFECT] = DEFENSE_UP1_EFFECT
move_table[WITHDRAW][POWER] = 0
move_table[WITHDRAW][MOVE_TYPE] = WATER
move_table[WITHDRAW][ACCURACY] = 100
move_table[WITHDRAW][PP] = 40

move_table[DEFENSE_CURL][MOVE_NAME] = "Defense Curl"
move_table[DEFENSE_CURL][EFFECT] = DEFENSE_UP1_EFFECT
move_table[DEFENSE_CURL][POWER] = 0
move_table[DEFENSE_CURL][MOVE_TYPE] = NORMAL
move_table[DEFENSE_CURL][ACCURACY] = 100
move_table[DEFENSE_CURL][PP] = 40

move_table[BARRIER][MOVE_NAME] = "Barrier"
move_table[BARRIER][EFFECT] = DEFENSE_UP2_EFFECT
move_table[BARRIER][POWER] = 0
move_table[BARRIER][MOVE_TYPE] = PSYCHIC_TYPE
move_table[BARRIER][ACCURACY] = 100
move_table[BARRIER][PP] = 30

move_table[LIGHT_SCREEN][MOVE_NAME] = "Light Screen"
move_table[LIGHT_SCREEN][EFFECT] = LIGHT_SCREEN_EFFECT
move_table[LIGHT_SCREEN][POWER] = 0
move_table[LIGHT_SCREEN][MOVE_TYPE] = PSYCHIC_TYPE
move_table[LIGHT_SCREEN][ACCURACY] = 100
move_table[LIGHT_SCREEN][PP] = 30

move_table[HAZE][MOVE_NAME] = "Haze"
move_table[HAZE][EFFECT] = HAZE_EFFECT
move_table[HAZE][POWER] = 0
move_table[HAZE][MOVE_TYPE] = ICE
move_table[HAZE][ACCURACY] = 100
move_table[HAZE][PP] = 30

move_table[REFLECT][MOVE_NAME] = "Reflect"
move_table[REFLECT][EFFECT] = REFLECT_EFFECT
move_table[REFLECT][POWER] = 0
move_table[REFLECT][MOVE_TYPE] = PSYCHIC_TYPE
move_table[REFLECT][ACCURACY] = 100
move_table[REFLECT][PP] = 20

move_table[FOCUS_ENERGY][MOVE_NAME] = "Focus Energy"
move_table[FOCUS_ENERGY][EFFECT] = FOCUS_ENERGY_EFFECT
move_table[FOCUS_ENERGY][POWER] = 0
move_table[FOCUS_ENERGY][MOVE_TYPE] = NORMAL
move_table[FOCUS_ENERGY][ACCURACY] = 100
move_table[FOCUS_ENERGY][PP] = 30

move_table[BIDE][MOVE_NAME] = "Bide"
move_table[BIDE][EFFECT] = BIDE_EFFECT
move_table[BIDE][POWER] = 0
move_table[BIDE][MOVE_TYPE] = NORMAL
move_table[BIDE][ACCURACY] = 100
move_table[BIDE][PP] = 10

move_table[METRONOME][MOVE_NAME] = "Metronome"
move_table[METRONOME][EFFECT] = METRONOME_EFFECT
move_table[METRONOME][POWER] = 0
move_table[METRONOME][MOVE_TYPE] = NORMAL
move_table[METRONOME][ACCURACY] = 100
move_table[METRONOME][PP] = 10

move_table[MIRROR_MOVE][MOVE_NAME] = "Mirror Move"
move_table[MIRROR_MOVE][EFFECT] = MIRROR_MOVE_EFFECT
move_table[MIRROR_MOVE][POWER] = 0
move_table[MIRROR_MOVE][MOVE_TYPE] = FLYING
move_table[MIRROR_MOVE][ACCURACY] = 100
move_table[MIRROR_MOVE][PP] = 20

move_table[SELFDESTRUCT][MOVE_NAME] = "Selfdestruct"
move_table[SELFDESTRUCT][EFFECT] = EXPLODE_EFFECT
move_table[SELFDESTRUCT][POWER] = 130
move_table[SELFDESTRUCT][MOVE_TYPE] = NORMAL
move_table[SELFDESTRUCT][ACCURACY] = 100
move_table[SELFDESTRUCT][PP] = 5

move_table[EGG_BOMB][MOVE_NAME] = "Egg Bomb"
move_table[EGG_BOMB][EFFECT] = NO_ADDITIONAL_EFFECT
move_table[EGG_BOMB][POWER] = 100
move_table[EGG_BOMB][MOVE_TYPE] = NORMAL
move_table[EGG_BOMB][ACCURACY] = 75
move_table[EGG_BOMB][PP] = 10

move_table[LICK][MOVE_NAME] = "Lick"
move_table[LICK][EFFECT] = PARALYZE_SIDE_EFFECT2
move_table[LICK][POWER] = 20
move_table[LICK][MOVE_TYPE] = GHOST
move_table[LICK][ACCURACY] = 100
move_table[LICK][PP] = 30

move_table[SMOG][MOVE_NAME] = "Smog"
move_table[SMOG][EFFECT] = POISON_SIDE_EFFECT2
move_table[SMOG][POWER] = 20
move_table[SMOG][MOVE_TYPE] = POISON
move_table[SMOG][ACCURACY] = 70
move_table[SMOG][PP] = 20

move_table[SLUDGE][MOVE_NAME] = "Sludge"
move_table[SLUDGE][EFFECT] = POISON_SIDE_EFFECT2
move_table[SLUDGE][POWER] = 65
move_table[SLUDGE][MOVE_TYPE] = POISON
move_table[SLUDGE][ACCURACY] = 100
move_table[SLUDGE][PP] = 20

move_table[BONE_CLUB][MOVE_NAME] = "Bone Club"
move_table[BONE_CLUB][EFFECT] = FLINCH_SIDE_EFFECT1
move_table[BONE_CLUB][POWER] = 65
move_table[BONE_CLUB][MOVE_TYPE] = GROUND
move_table[BONE_CLUB][ACCURACY] = 85
move_table[BONE_CLUB][PP] = 20

move_table[FIRE_BLAST][MOVE_NAME] = "Fire Blast"
move_table[FIRE_BLAST][EFFECT] = BURN_SIDE_EFFECT2
move_table[FIRE_BLAST][POWER] = 120
move_table[FIRE_BLAST][MOVE_TYPE] = FIRE
move_table[FIRE_BLAST][ACCURACY] = 85
move_table[FIRE_BLAST][PP] = 5

move_table[WATERFALL][MOVE_NAME] = "Waterfall"
move_table[WATERFALL][EFFECT] = NO_ADDITIONAL_EFFECT
move_table[WATERFALL][POWER] = 80
move_table[WATERFALL][MOVE_TYPE] = WATER
move_table[WATERFALL][ACCURACY] = 100
move_table[WATERFALL][PP] = 15

move_table[CLAMP][MOVE_NAME] = "Clamp"
move_table[CLAMP][EFFECT] = TRAPPING_EFFECT
move_table[CLAMP][POWER] = 35
move_table[CLAMP][MOVE_TYPE] = WATER
move_table[CLAMP][ACCURACY] = 75
move_table[CLAMP][PP] = 10

move_table[SWIFT][MOVE_NAME] = "Swift"
move_table[SWIFT][EFFECT] = SWIFT_EFFECT
move_table[SWIFT][POWER] = 60
move_table[SWIFT][MOVE_TYPE] = NORMAL
move_table[SWIFT][ACCURACY] = 100
move_table[SWIFT][PP] = 20

move_table[SKULL_BASH][MOVE_NAME] = "Skull Bash"
move_table[SKULL_BASH][EFFECT] = CHARGE_EFFECT
move_table[SKULL_BASH][POWER] = 100
move_table[SKULL_BASH][MOVE_TYPE] = NORMAL
move_table[SKULL_BASH][ACCURACY] = 100
move_table[SKULL_BASH][PP] = 15

move_table[SPIKE_CANNON][MOVE_NAME] = "Spike Cannon"
move_table[SPIKE_CANNON][EFFECT] = TWO_TO_FIVE_ATTACKS_EFFECT
move_table[SPIKE_CANNON][POWER] = 20
move_table[SPIKE_CANNON][MOVE_TYPE] = NORMAL
move_table[SPIKE_CANNON][ACCURACY] = 100
move_table[SPIKE_CANNON][PP] = 15

move_table[CONSTRICT][MOVE_NAME] = "Constrict"
move_table[CONSTRICT][EFFECT] = SPEED_DOWN_SIDE_EFFECT
move_table[CONSTRICT][POWER] = 10
move_table[CONSTRICT][MOVE_TYPE] = NORMAL
move_table[CONSTRICT][ACCURACY] = 100
move_table[CONSTRICT][PP] = 35

move_table[AMNESIA][MOVE_NAME] = "Amnesia"
move_table[AMNESIA][EFFECT] = SPECIAL_UP2_EFFECT
move_table[AMNESIA][POWER] = 0
move_table[AMNESIA][MOVE_TYPE] = PSYCHIC_TYPE
move_table[AMNESIA][ACCURACY] = 100
move_table[AMNESIA][PP] = 20

move_table[KINESIS][MOVE_NAME] = "Kinesis"
move_table[KINESIS][EFFECT] = ACCURACY_DOWN1_EFFECT
move_table[KINESIS][POWER] = 0
move_table[KINESIS][MOVE_TYPE] = PSYCHIC_TYPE
move_table[KINESIS][ACCURACY] = 80
move_table[KINESIS][PP] = 15

move_table[SOFTBOILED][MOVE_NAME] = "Softboiled"
move_table[SOFTBOILED][EFFECT] = HEAL_EFFECT
move_table[SOFTBOILED][POWER] = 0
move_table[SOFTBOILED][MOVE_TYPE] = NORMAL
move_table[SOFTBOILED][ACCURACY] = 100
move_table[SOFTBOILED][PP] = 10

move_table[HI_JUMP_KICK][MOVE_NAME] = "Hi Jump Kick"
move_table[HI_JUMP_KICK][EFFECT] = JUMP_KICK_EFFECT
move_table[HI_JUMP_KICK][POWER] = 85
move_table[HI_JUMP_KICK][MOVE_TYPE] = FIGHTING
move_table[HI_JUMP_KICK][ACCURACY] = 90
move_table[HI_JUMP_KICK][PP] = 20

move_table[GLARE][MOVE_NAME] = "Glare"
move_table[GLARE][EFFECT] = PARALYZE_EFFECT
move_table[GLARE][POWER] = 0
move_table[GLARE][MOVE_TYPE] = NORMAL
move_table[GLARE][ACCURACY] = 75
move_table[GLARE][PP] = 30

move_table[DREAM_EATER][MOVE_NAME] = "Dream Eater"
move_table[DREAM_EATER][EFFECT] = DREAM_EATER_EFFECT
move_table[DREAM_EATER][POWER] = 100
move_table[DREAM_EATER][MOVE_TYPE] = PSYCHIC_TYPE
move_table[DREAM_EATER][ACCURACY] = 100
move_table[DREAM_EATER][PP] = 15

move_table[POISON_GAS][MOVE_NAME] = "Poison Gas"
move_table[POISON_GAS][EFFECT] = POISON_EFFECT
move_table[POISON_GAS][POWER] = 0
move_table[POISON_GAS][MOVE_TYPE] = POISON
move_table[POISON_GAS][ACCURACY] = 55
move_table[POISON_GAS][PP] = 40

move_table[BARRAGE][MOVE_NAME] = "Barrage"
move_table[BARRAGE][EFFECT] = TWO_TO_FIVE_ATTACKS_EFFECT
move_table[BARRAGE][POWER] = 15
move_table[BARRAGE][MOVE_TYPE] = NORMAL
move_table[BARRAGE][ACCURACY] = 85
move_table[BARRAGE][PP] = 20

move_table[LEECH_LIFE][MOVE_NAME] = "Leech Life"
move_table[LEECH_LIFE][EFFECT] = DRAIN_HP_EFFECT
move_table[LEECH_LIFE][POWER] = 20
move_table[LEECH_LIFE][MOVE_TYPE] = BUG
move_table[LEECH_LIFE][ACCURACY] = 100
move_table[LEECH_LIFE][PP] = 15

move_table[LOVELY_KISS][MOVE_NAME] = "Lovely Kiss"
move_table[LOVELY_KISS][EFFECT] = SLEEP_EFFECT
move_table[LOVELY_KISS][POWER] = 0
move_table[LOVELY_KISS][MOVE_TYPE] = NORMAL
move_table[LOVELY_KISS][ACCURACY] = 75
move_table[LOVELY_KISS][PP] = 10

move_table[SKY_ATTACK][MOVE_NAME] = "Sky Attack"
move_table[SKY_ATTACK][EFFECT] = CHARGE_EFFECT
move_table[SKY_ATTACK][POWER] = 140
move_table[SKY_ATTACK][MOVE_TYPE] = FLYING
move_table[SKY_ATTACK][ACCURACY] = 90
move_table[SKY_ATTACK][PP] = 5

move_table[TRANSFORM][MOVE_NAME] = "Transform"
move_table[TRANSFORM][EFFECT] = TRANSFORM_EFFECT
move_table[TRANSFORM][POWER] = 0
move_table[TRANSFORM][MOVE_TYPE] = NORMAL
move_table[TRANSFORM][ACCURACY] = 100
move_table[TRANSFORM][PP] = 10

move_table[BUBBLE][MOVE_NAME] = "Bubble"
move_table[BUBBLE][EFFECT] = SPEED_DOWN_SIDE_EFFECT
move_table[BUBBLE][POWER] = 20
move_table[BUBBLE][MOVE_TYPE] = WATER
move_table[BUBBLE][ACCURACY] = 100
move_table[BUBBLE][PP] = 30

move_table[DIZZY_PUNCH][MOVE_NAME] = "Dizzy Punch"
move_table[DIZZY_PUNCH][EFFECT] = NO_ADDITIONAL_EFFECT
move_table[DIZZY_PUNCH][POWER] = 70
move_table[DIZZY_PUNCH][MOVE_TYPE] = NORMAL
move_table[DIZZY_PUNCH][ACCURACY] = 100
move_table[DIZZY_PUNCH][PP] = 10

move_table[SPORE][MOVE_NAME] = "Spore"
move_table[SPORE][EFFECT] = SLEEP_EFFECT
move_table[SPORE][POWER] = 0
move_table[SPORE][MOVE_TYPE] = GRASS
move_table[SPORE][ACCURACY] = 100
move_table[SPORE][PP] = 15

move_table[FLASH][MOVE_NAME] = "Flash"
move_table[FLASH][EFFECT] = ACCURACY_DOWN1_EFFECT
move_table[FLASH][POWER] = 0
move_table[FLASH][MOVE_TYPE] = NORMAL
move_table[FLASH][ACCURACY] = 70
move_table[FLASH][PP] = 20

move_table[PSYWAVE][MOVE_NAME] = "Psywave"
move_table[PSYWAVE][EFFECT] = SPECIAL_DAMAGE_EFFECT
move_table[PSYWAVE][POWER] = 1
move_table[PSYWAVE][MOVE_TYPE] = PSYCHIC_TYPE
move_table[PSYWAVE][ACCURACY] = 80
move_table[PSYWAVE][PP] = 15

move_table[SPLASH][MOVE_NAME] = "Splash"
move_table[SPLASH][EFFECT] = SPLASH_EFFECT
move_table[SPLASH][POWER] = 0
move_table[SPLASH][MOVE_TYPE] = NORMAL
move_table[SPLASH][ACCURACY] = 100
move_table[SPLASH][PP] = 40

move_table[ACID_ARMOR][MOVE_NAME] = "Acid Armor"
move_table[ACID_ARMOR][EFFECT] = DEFENSE_UP2_EFFECT
move_table[ACID_ARMOR][POWER] = 0
move_table[ACID_ARMOR][MOVE_TYPE] = POISON
move_table[ACID_ARMOR][ACCURACY] = 100
move_table[ACID_ARMOR][PP] = 40

move_table[CRABHAMMER][MOVE_NAME] = "Crabhammer"
move_table[CRABHAMMER][EFFECT] = NO_ADDITIONAL_EFFECT
move_table[CRABHAMMER][POWER] = 90
move_table[CRABHAMMER][MOVE_TYPE] = WATER
move_table[CRABHAMMER][ACCURACY] = 85
move_table[CRABHAMMER][PP] = 10

move_table[EXPLOSION][MOVE_NAME] = "Explosion"
move_table[EXPLOSION][EFFECT] = EXPLODE_EFFECT
move_table[EXPLOSION][POWER] = 170
move_table[EXPLOSION][MOVE_TYPE] = NORMAL
move_table[EXPLOSION][ACCURACY] = 100
move_table[EXPLOSION][PP] = 5

move_table[FURY_SWIPES][MOVE_NAME] = "Fury Swipes"
move_table[FURY_SWIPES][EFFECT] = TWO_TO_FIVE_ATTACKS_EFFECT
move_table[FURY_SWIPES][POWER] = 18
move_table[FURY_SWIPES][MOVE_TYPE] = NORMAL
move_table[FURY_SWIPES][ACCURACY] = 80
move_table[FURY_SWIPES][PP] = 15

move_table[BONEMERANG][MOVE_NAME] = "Bonemerang"
move_table[BONEMERANG][EFFECT] = ATTACK_TWICE_EFFECT
move_table[BONEMERANG][POWER] = 50
move_table[BONEMERANG][MOVE_TYPE] = GROUND
move_table[BONEMERANG][ACCURACY] = 90
move_table[BONEMERANG][PP] = 10

move_table[REST][MOVE_NAME] = "Rest"
move_table[REST][EFFECT] = HEAL_EFFECT
move_table[REST][POWER] = 0
move_table[REST][MOVE_TYPE] = PSYCHIC_TYPE
move_table[REST][ACCURACY] = 100
move_table[REST][PP] = 10

move_table[ROCK_SLIDE][MOVE_NAME] = "Rock Slide"
move_table[ROCK_SLIDE][EFFECT] = NO_ADDITIONAL_EFFECT
move_table[ROCK_SLIDE][POWER] = 75
move_table[ROCK_SLIDE][MOVE_TYPE] = ROCK
move_table[ROCK_SLIDE][ACCURACY] = 90
move_table[ROCK_SLIDE][PP] = 10

move_table[HYPER_FANG][MOVE_NAME] = "Hyper Fang"
move_table[HYPER_FANG][EFFECT] = FLINCH_SIDE_EFFECT1
move_table[HYPER_FANG][POWER] = 80
move_table[HYPER_FANG][MOVE_TYPE] = NORMAL
move_table[HYPER_FANG][ACCURACY] = 90
move_table[HYPER_FANG][PP] = 15

move_table[SHARPEN][MOVE_NAME] = "Sharpen"
move_table[SHARPEN][EFFECT] = ATTACK_UP1_EFFECT
move_table[SHARPEN][POWER] = 0
move_table[SHARPEN][MOVE_TYPE] = NORMAL
move_table[SHARPEN][ACCURACY] = 100
move_table[SHARPEN][PP] = 30

move_table[CONVERSION][MOVE_NAME] = "Conversion"
move_table[CONVERSION][EFFECT] = CONVERSION_EFFECT
move_table[CONVERSION][POWER] = 0
move_table[CONVERSION][MOVE_TYPE] = NORMAL
move_table[CONVERSION][ACCURACY] = 100
move_table[CONVERSION][PP] = 30

move_table[TRI_ATTACK][MOVE_NAME] = "Tri Attack"
move_table[TRI_ATTACK][EFFECT] = NO_ADDITIONAL_EFFECT
move_table[TRI_ATTACK][POWER] = 80
move_table[TRI_ATTACK][MOVE_TYPE] = NORMAL
move_table[TRI_ATTACK][ACCURACY] = 100
move_table[TRI_ATTACK][PP] = 10

move_table[SUPER_FANG][MOVE_NAME] = "Super Fang"
move_table[SUPER_FANG][EFFECT] = SUPER_FANG_EFFECT
move_table[SUPER_FANG][POWER] = 1
move_table[SUPER_FANG][MOVE_TYPE] = NORMAL
move_table[SUPER_FANG][ACCURACY] = 90
move_table[SUPER_FANG][PP] = 10

move_table[SLASH][MOVE_NAME] = "Slash"
move_table[SLASH][EFFECT] = NO_ADDITIONAL_EFFECT
move_table[SLASH][POWER] = 70
move_table[SLASH][MOVE_TYPE] = NORMAL
move_table[SLASH][ACCURACY] = 100
move_table[SLASH][PP] = 20

move_table[SUBSTITUTE][MOVE_NAME] = "Substitute"
move_table[SUBSTITUTE][EFFECT] = SUBSTITUTE_EFFECT
move_table[SUBSTITUTE][POWER] = 0
move_table[SUBSTITUTE][MOVE_TYPE] = NORMAL
move_table[SUBSTITUTE][ACCURACY] = 100
move_table[SUBSTITUTE][PP] = 10

move_table[STRUGGLE][MOVE_NAME] = "Struggle"
move_table[STRUGGLE][EFFECT] = RECOIL_EFFECT
move_table[STRUGGLE][POWER] = 50
move_table[STRUGGLE][MOVE_TYPE] = NORMAL
move_table[STRUGGLE][ACCURACY] = 100
move_table[STRUGGLE][PP] = 10