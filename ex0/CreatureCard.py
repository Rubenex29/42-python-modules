from .Card import Card
import random
from typing import Any


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, attack: int,
                 health: int) -> None:
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health

    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        effects = [
            "Creature summoned to battlefield",
            "A mysterious aura surrounds the creature",
            "The creature steps onto the battlefield with determination",
            "A chilling silence follows its arrival",
            "An ancient sigil flashes above the battlefield",
            "The ground trembles as the creature takes its stance",
            "A distant roar echoes across the battlefield",
        ]

        available_mana = game_state["available_mana"]
        playable = self.is_playable(available_mana)
        if playable:
            chosen_effect = random.choice(effects)
            return {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": chosen_effect,
            }
        return {}

    def attack_target(self, target: str) -> dict[str, Any]:
        if self.attack > 0 and self.health > 0:
            combat_resolved = True
        else:
            combat_resolved = False
        return {
            "attacker": self.name,
            "target": target,
            "damage_dealt": self.attack,
            "combat_resolved": combat_resolved
        }
