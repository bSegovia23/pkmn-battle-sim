#1. make a class that has a dictionary as a field

# class Effect_Calculator:
#   def __init__(self):
#     self.dict_ = {}

#     self.dict_["ATTACK_DOWN1_EFFECT"] = attackDown1
#     self.dict_["DEFENSE_DOWN1_EFFECT"] = defenseDown1

#   def modifyStats(effect, target):
#     retrieved_function = self.dict.get(effect)
#     retrieved_function(target)
#     return
    
#   def attackDown1(target):
#     target.mod_atk_stage(-1)
#     print("The opponents attack fell!")

#   def defenseDown1(target):
#     target.mod_def_stage(-1)
#     print("The opponents defense fell!")

    
#__THIS GOES IN BATTLE.PY__
# effect_dictionary = Effect_Dict()
# effect_dictionary.modifyStats(move.effect, pkmn)