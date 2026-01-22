from ex0.Card import card
from ex0.CreatureCard import CreatureCard

# ...o resto do teu main...
print("=== DataDeck Card Foundation ===\n")
print("Testing Abstract Base Class Design:\n")
print("CreatureCard Info:")
dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
print(dragon.get_card_info())
print()
print("Playing Fire Dragon with 6 mana available:")
print("Playable:", dragon.is_playable(6))
result = dragon.attack_target("Goblin Warrior")
print("Attack result:", result)
print()
print("Testing insufficient mana (3 available):")
print("Playable:", dragon.is_playable(3))
print()
print("Abstract pattern successfully demonstrated!")