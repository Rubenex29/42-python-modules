"""Elite card implementing multiple interfaces.

EliteCard combines the base Card API with combat (Combatable) and magic
(Magical) capabilities.
"""

from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex2.Combatable import Combatable
from ex2.Magical import Magical
import random
from typing import Any


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str, attack: int,
                 health: int, spell: str) -> None:
        super().__init__(name, cost, rarity)
        self.attack_power = attack
        self.health = health
        self.spell = spell

    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        available_mana = game_state["available_mana"]
        if self.is_playable(available_mana):
            return {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": "Elite deployed with combat and spell abilities",
            }
        return {}

    def attack(self, target: object) -> dict[str, Any]:
        # Determine the combat type based on the target's runtime class.
        target_name = getattr(target, "name", str(target))
        combat_type = "unknown"
        if isinstance(target, CreatureCard):
            combat_type = "melee"
        elif isinstance(target, ArtifactCard):
            combat_type = "artifact"
        elif isinstance(target, SpellCard):
            combat_type = "spell"

        return {
            "attacker": self.name,
            "target": target_name,
            "damage": self.attack_power,
            "combat_type": combat_type,
        }

    def defend(self, incoming_damage: int) -> dict[str, Any]:
        # Simple block mechanic: randomly blocks 1-3 damage.
        block_value = random.randint(1, 3)
        damage_taken = max(0, incoming_damage - block_value)
        still_alive = (self.health - damage_taken) > 0
        return {
            "defender": self.name,
            "damage_taken": incoming_damage,
            "damage_blocked": block_value,
            "still_alive": still_alive,
        }

    def get_combat_stats(self) -> dict[str, Any]:
        return {
            "combatant": self.name,
            "attack_power": self.attack_power,
            "health": self.health,
            "spell": self.spell,
        }

    def cast_spell(
        self,
        spell_name: str,
        targets: list[str],
    ) -> dict[str, Any]:
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": self.cost,
        }

    def channel_mana(self, amount: int) -> dict[str, Any]:
        return {
            "channeled": amount,
            "total_mana": self.cost + amount,
        }

    def get_magic_stats(self) -> dict[str, Any]:
        return {
            "caster": self.name,
            "spell": self.spell,
            "mana_pool": self.mana_pool,
        }
