from ex3.GameEngine import GameEngine
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy

print("=== DataDeck Game Engine ===\n")
print("Configuring Fantasy Card Game...")
engine = GameEngine()
factory = FantasyCardFactory()
strategy = AggressiveStrategy()
engine.configure_engine(factory, strategy)

print(f"Factory: {factory.__class__.__name__}")
print(f"Strategy: {strategy.get_strategy_name()}")
print(f"Available types: {factory.get_supported_types()}")
print("\nSimulating aggressive turn...")
print("\nTurn execution:")
print(f"Strategy: {strategy.get_strategy_name()}")
print(engine.simulate_turn())
print("\nGame Report:")
print(engine.get_engine_status())
