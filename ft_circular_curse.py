print("\n=== Circular Curse Breaking ===\n")
print("Testing ingredient validation:")
from alchemy.grimoire import validate_ingredients
print('validate_ingredients("fire air"):', validate_ingredients("fire air"))
print('validate_ingredients("dragon scales"):', validate_ingredients("dragon scales"))
print()
print("Testing spell recording with validation:")
from alchemy.grimoire import record_spell
print('record_spell("Fireball", "fire air"):', record_spell("Fireball", "fire air"))
print('record_spell("Dark Magic", "shadow"):', record_spell("Dark Magic", "shadow"))
print()
print("Testing late import technique:")
print('record_spell("Lightning", "air"):', record_spell("Lightning", "air"))
print()
print("Circular dependency curse avoided using late imports!")
print("All spells processed safely!")

# a.py
# SIGNATURE = "assinatura de A"

# def hello():
#     import b  # late import (Método 1)
#     return "A: " + b.world()


# b.py
# import a

# def world():
#     return "mundo! (e eu vi " + a.SIGNATURE + ")"
