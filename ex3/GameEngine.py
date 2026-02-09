"""Minimal game engine that wires a factory and strategy together."""

from ex3.FantasyCardFactory import CardFactory
from ex3.AggressiveStrategy import GameStrategy
from typing import Any


class GameEngine():
    def __init__(self) -> None:
        self.count = 0
        self.total_damage = 0

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        # Dependency injection:
        # engine behavior comes from the provided objects.
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> dict[str, Any]:
        self.count += 1
        card_names = self.factory.list_cards()
        # Convert each card object to a dict
        # so the strategy can operate on data.
        hand = [self.factory.get_card(name).__dict__
                for name in card_names
                if self.factory.get_card(name) is not None]
        result = self.strategy.execute_turn(hand, ["enemy1"])
        self.total_damage += result['damage_dealt']
        return dict(result)

    def get_engine_status(self) -> dict[str, Any]:
        return {
            "turns_simulated": self.count,
            "strategy_used": self.strategy.get_strategy_name(),
            "total_damage": self.total_damage,
            "cards_created": len(self.factory.list_cards())
        }
