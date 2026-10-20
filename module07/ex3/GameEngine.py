"""Minimal game engine that wires a factory and strategy together."""

from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy
from typing import Any


class GameEngine():
    def __init__(self) -> None:
        self.count = 0
        self.total_damage = 0
        self.factory: CardFactory | None = None
        self.strategy: GameStrategy | None = None

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> dict[str, Any]:
        if self.factory is None or self.strategy is None:
            raise ValueError("Engine must be configured before simulation")
        self.count += 1
        deck = self.factory.create_themed_deck(3)
        hand = deck["cards"]
        result = self.strategy.execute_turn(hand, ["enemy1"])
        self.total_damage += result['damage_dealt']
        return dict(result)

    def get_engine_status(self) -> dict[str, Any]:
        if self.factory is None or self.strategy is None:
            raise ValueError("Engine must be configured before status report")
        return {
            "turns_simulated": self.count,
            "strategy_used": self.strategy.get_strategy_name(),
            "total_damage": self.total_damage,
            "cards_created": 3 * self.count,
        }
