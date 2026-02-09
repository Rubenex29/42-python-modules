"""Spell card implementation.

Spells are one-time use: once played successfully, they become consumed.
"""

from ex0.Card import Card
from typing import Any, Literal

EffectType = Literal["damage", "heal", "buff", "debuff"]


class SpellCard(Card):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        effect_type: EffectType,
    ) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type
        self.consumed = False  # Spells are consumed when played (one-time use)

    def resolve_effect(self, targets: list) -> dict[str, Any]:
        effect_phrases = {
            "damage": "Deal 3 damage to target",
            "heal": "Restore 3 health to target",
            "buff": "Give target creature +2/+2",
            "debuff": "Silence target creature",
        }
        return {
            "effect_type": self.effect_type,
            "targets": targets,
            "effect": effect_phrases[self.effect_type],
        }

    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        if self.consumed:
            return {
                "card_played": self.name,
                "mana_used": 0,
                "effect": "Spell already consumed",
                "consumed": True,
            }

        available_mana = game_state.get("available_mana", 0)
        targets = game_state.get("targets", [])
        playable = self.is_playable(available_mana)
        if playable:
            self.consumed = True
            return {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": self.resolve_effect(targets)["effect"],
            }
        return {}
