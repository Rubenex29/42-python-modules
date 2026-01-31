from ex3.GameEngine import GameEngine
from ex3.FantasyCardFactory import CardFactory
from ex3.AggressiveStrategy import GameStrategy as AggressiveStrategy

print("=== DataDeck Game Engine ===\n")
print("Configuring Fantasy Card Game...")
engine = GameEngine()
factory = CardFactory()
strategy = AggressiveStrategy("AggressiveStrategy")
engine.configure_engine(factory, strategy)

print(f"Factory: {factory.__class__.__name__}")
print(f"Strategy: {strategy.get_strategy_name()}")
available_types = {
    'creatures': ['dragon', 'goblin'],
    'spells': ['fireball', 'ice', 'lightning'],
    'artifacts': ['ring', 'staff', 'crystal']
}
print(f"Available types: {available_types}")
print("\nSimulating aggressive turn...")
print("Hand: [Fire Dragon (cost: 5), "
      "Goblin Warrior (cost: 2), Lightning Bolt (cost: 3)]")
hand = [
    {"name": "Fire Dragon", "cost": 5},
    {"name": "Goblin Warrior", "cost": 2},
    {"name": "Lightning Bolt", "cost": 3}
]
print("\nTurn execution:")
print(f"Strategy: {strategy.get_strategy_name()}")
game = GameEngine()
game.configure_engine(factory, strategy)
print(game.simulate_turn())
print("\nGame Report:")
print(game.get_engine_status())
