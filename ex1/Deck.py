"""Deck container for Card objects.

Keeps a list of cards and provides basic deck operations such as add/remove,
shuffle, draw, and simple deck statistics.
"""

from ex0.Card import Card
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex0.CreatureCard import CreatureCard
from typing import Any, List, Optional
import random


class Deck:
    def __init__(self) -> None:
        self.cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        # Adds the card to the deck (does not play the card).
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Optional[Card]:
        if not self.cards:
            return None
        return self.cards.pop()

    def get_deck_stats(self) -> dict[str, Any]:
        # Counts each card type and computes average mana cost.
        total = len(self.cards)
        creature_count = sum(
            1 for card in self.cards
            if isinstance(card, CreatureCard)
        )
        spell_count = sum(
            1 for card in self.cards
            if isinstance(card, SpellCard)
        )
        artifact_count = sum(
            1 for card in self.cards
            if isinstance(card, ArtifactCard)
        )
        total_cost = sum(card.cost for card in self.cards)
        avg_cost = (
            round(total_cost / total, 2) if total > 0 else 0.0
        )

        return {
            "total_cards": total,
            "creatures": creature_count,
            "spells": spell_count,
            "artifacts": artifact_count,
            "avg_cost": avg_cost,
        }
