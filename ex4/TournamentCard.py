from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable
import random


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int, rarity: str, attack: int,
                 health: int, wins: int = 0, losses: int = 0,
                 base_rating: int = 1000):
        super().__init__(name, cost, rarity)
        self.attack_power = attack
        self.health = health
        self.wins = wins
        self.losses = losses
        self.base_rating = base_rating

    def play(self, game_state: dict) -> dict:
        available_mana = game_state["available_mana"]
        playable = self.is_playable(available_mana)
        if playable:
            return {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": "Tournament contender enters the arena",
            }
        return {}

    def attack(self, target) -> dict:
        target_name = getattr(target, "name", str(target))
        combat_resolved = self.attack_power > 0 and self.health > 0
        return {
            "attacker": self.name,
            "target": target_name,
            "damage_dealt": self.attack_power,
            "combat_resolved": combat_resolved,
        }

    def defend(self, incoming_damage: int) -> dict:
        block_value = random.randint(0, 2)
        damage_taken = max(0, incoming_damage - block_value)
        still_alive = (self.health - damage_taken) > 0
        return {
            "defender": self.name,
            "damage_taken": incoming_damage,
            "damage_blocked": block_value,
            "still_alive": still_alive,
        }

    def get_combat_stats(self) -> dict:
        return {
            "combatant": self.name,
            "attack_power": self.attack_power,
            "health": self.health,
        }

    def calculate_rating(self) -> int:
        return max(0, self.base_rating + (self.wins * 16) - (self.losses * 16))

    def update_wins(self, wins: int) -> None:
        self.wins = wins

    def update_losses(self, losses: int) -> None:
        self.losses = losses

    def get_rank_info(self) -> dict:
        return {
            "card": self.name,
            "wins": self.wins,
            "losses": self.losses,
            "rating": self.calculate_rating(),
        }

    def process_match(self, opponent) -> dict:
        winner = self
        loser = opponent

        if opponent.attack_power > self.attack_power:
            winner = opponent
            loser = self
        elif opponent.attack_power == self.attack_power:
            winner = random.choice([self, opponent])
            loser = opponent if winner is self else self

        winner.update_wins(winner.wins + 1)
        loser.update_losses(loser.losses + 1)

        return {
            "winner": winner.name,
            "loser": loser.name,
            "winner_rating": winner.calculate_rating(),
            "loser_rating": loser.calculate_rating(),
        }
