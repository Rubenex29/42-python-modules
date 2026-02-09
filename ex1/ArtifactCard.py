from ex0.Card import Card
from typing import Any


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, durability: int,
                 effect: str) -> None:
        super().__init__(name, cost, rarity)
        if not isinstance(durability, int) or durability <= 0:
            raise ValueError("durability must be a positive integer")
        self.durability = durability  # how long it lasts
        self.effect = effect  # permanent ability description
        self.in_play = False  # Artifacts remain in play until destroyed

    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        available_mana = game_state.get("available_mana", 0)
        playable = self.is_playable(available_mana)
        if playable:
            self.in_play = True
            return {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": self.effect,
            }
        return {}

    def activate_ability(self) -> dict[str, Any]:
        # Implements activate_ability for ongoing effects
        if not self.in_play or self.durability <= 0:
            return {
                "artifact": self.name,
                "effect": "Artifact is not in play or destroyed",
                "active": False,
            }

        return {
            "artifact": self.name,
            "effect": self.effect,
            "durability": self.durability,
            "active": True,
        }
