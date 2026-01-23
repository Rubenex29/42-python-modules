from ex0.Card import Card
from ex1.ArtifactCard import ArtifactCard
import random


class Deck:
    def __init__(self):
        self.cards = []

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

    def draw_card(self) -> Card:
        return self.cards.pop()

    def get_deck_stats(self) -> None:
        total = len(self.cards)
