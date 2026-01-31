from ex3.FantasyCardFactory import CardFactory
from ex3.AggressiveStrategy import GameStrategy


class GameEngine():
    def __init__(self):
        self.count = 0
        self.total_damage = 0

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> dict:
        self.count += 1
        card_names = self.factory.list_cards()
        hand = [self.factory.get_card(name).__dict__
                for name in card_names
                if self.factory.get_card(name) is not None]
        result = self.strategy.execute_turn(hand, ["enemy1"])
        self.total_damage += result['damage_dealt']
        return dict(result)

    def get_engine_status(self) -> dict:
        return {
            "turns_simulated": self.count,
            "strategy_used": self.strategy.get_strategy_name(),
            "total_damage": self.total_damage,
            "cards_created": len(self.factory.list_cards())
        }
