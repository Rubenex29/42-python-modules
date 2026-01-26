from ex0.Card import Card
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex0.CreatureCard import CreatureCard
from typing import List, Optional
import random


class Deck:
    def __init__(self):
        self.cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        # Adiciona a carta ao deck (não joga a carta)
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

    def get_deck_stats(self) -> dict:
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
