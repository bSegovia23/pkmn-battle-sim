from enum import Enum, auto

class Pok(Enum):
  # Pokémon constants
  BULBASAUR = auto()
  CHARMANDER = auto()
  SQUIRTLE = auto()

class Mov(Enum):
  # move constants
  TACKLE = auto()
  SCRATCH = auto()
  GROWL = auto()
  TAIL_WHIP = auto()

class Cnd(Enum):
  # status condition constants
  BRN = auto()
  FRZ = auto()
  PAR = auto()
  PSN = auto()
  SLP = auto()
  FNT = auto()