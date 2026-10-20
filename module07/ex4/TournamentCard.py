"""TournamentCard adds ranking stats on top
of combat and base Card behavior."""

from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable
import random
from typing import Any


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int, rarity: str, attack: int,
                 health: int, wins: int = 0, losses: int = 0,
                 base_rating: int = 1000) -> None:
        super().__init__(name, cost, rarity)
        if not isinstance(attack, int) or attack <= 0:
            raise ValueError("attack must be a positive integer")
        if not isinstance(health, int) or health <= 0:
            raise ValueError("health must be a positive integer")
        self.attack_power = attack
        self.health = health
        self.wins = wins
        self.losses = losses
        self.base_rating = base_rating

    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        available_mana = game_state.get("available_mana", 0)
        playable = self.is_playable(available_mana)
        if playable:
            return {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": "Tournament contender enters the arena",
            }
        return {}

    def attack(self, target: object) -> dict[str, Any]:
        target_name = getattr(target, "name", str(target))
        combat_resolved = self.attack_power > 0 and self.health > 0
        return {
            "attacker": self.name,
            "target": target_name,
            "damage_dealt": self.attack_power,
            "combat_resolved": combat_resolved,
        }

    def defend(self, incoming_damage: int) -> dict[str, Any]:
        block_value = random.randint(0, 2)
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
        }

    def calculate_rating(self) -> int:
        return max(0, self.base_rating + (self.wins * 16) - (self.losses * 16))

    def update_wins(self, wins: int) -> None:
        self.wins = wins

    def update_losses(self, losses: int) -> None:
        self.losses = losses

    def get_rank_info(self) -> dict[str, Any]:
        return {
            "card": self.name,
            "wins": self.wins,
            "losses": self.losses,
            "rating": self.calculate_rating(),
        }

    def get_tournament_stats(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "record": f"{self.wins}-{self.losses}",
            "rating": self.calculate_rating(),
            "attack": self.attack_power,
            "health": self.health,
        }

    def process_match(self, opponent: "TournamentCard") -> dict[str, Any]:
        # Decide winner by attack power; break ties randomly.
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
