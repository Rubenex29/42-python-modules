"""Concrete fantasy card factory."""

from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import EffectType, SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex0.Card import Card
from ex3.CardFactory import CardFactory
from typing import Dict, Tuple
import random


class FantasyCardFactory(CardFactory):
    def __init__(self) -> None:
        self.creature_types = {
            "dragon": ("Fire Dragon", 5, "Legendary", 7, 5),
            "goblin": ("Goblin Warrior", 2, "Common", 2, 2),
        }
        self.spell_types: Dict[str, Tuple[str, int, str, EffectType]] = {
            "fireball": ("Fireball", 4, "Rare", "damage"),
            "ice": ("Ice Lance", 3, "Epic", "debuff"),
            "lightning": ("Lightning Bolt", 3, "Epic", "damage"),
        }
        self.artifact_types = {
            "mana_ring": (
                "Mana Ring",
                2,
                "Rare",
                5,
                "Permanent: +1 mana per turn",
            ),
            "staff": (
                "Mage Staff",
                4,
                "Epic",
                8,
                "Permanent: spells cost -1",
            ),
            "crystal": (
                "Crystal Orb",
                2,
                "Rare",
                4,
                "Permanent: +1 card draw",
            ),
        }

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        if (
            isinstance(name_or_power, str)
            and name_or_power in self.creature_types
        ):
            name, cost, rarity, attack, health = (
                self.creature_types[name_or_power]
            )
        else:
            name, cost, rarity, attack, health = random.choice(
                list(self.creature_types.values())
            )
        return CreatureCard(name, cost, rarity, attack, health)

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        if (
            isinstance(name_or_power, str)
            and name_or_power in self.spell_types
        ):
            name, cost, rarity, effect_type = (
                self.spell_types[name_or_power]
            )
        else:
            name, cost, rarity, effect_type = random.choice(
                list(self.spell_types.values())
            )
        return SpellCard(name, cost, rarity, effect_type)

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        if (
            isinstance(name_or_power, str)
            and name_or_power in self.artifact_types
        ):
            name, cost, rarity, durability, effect = (
                self.artifact_types[name_or_power]
            )
        else:
            name, cost, rarity, durability, effect = random.choice(
                list(self.artifact_types.values())
            )
        return ArtifactCard(name, cost, rarity, durability, effect)

    def create_themed_deck(self, size: int) -> dict[str, object]:
        cards: list[Card] = []
        for _ in range(size):
            choice = random.choice(["creature", "spell", "artifact"])
            if choice == "creature":
                cards.append(self.create_creature())
            elif choice == "spell":
                cards.append(self.create_spell())
            else:
                cards.append(self.create_artifact())
        return {"size": size, "cards": cards}

    def get_supported_types(self) -> dict[str, list[str]]:
        return {
            "creatures": list(self.creature_types.keys()),
            "spells": list(self.spell_types.keys()),
            "artifacts": list(self.artifact_types.keys()),
        }
