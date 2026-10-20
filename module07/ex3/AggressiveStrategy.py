from ex3.GameStrategy import GameStrategy
from typing import Any


class AggressiveStrategy(GameStrategy):
    def execute_turn(
        self,
        hand: list[Any],
        battlefield: list[Any],
    ) -> dict[str, Any]:
        sorted_hand = list(hand)
        for i in range(len(sorted_hand)):
            for j in range(i + 1, len(sorted_hand)):
                cost_i = getattr(sorted_hand[i], "cost", 0)
                cost_j = getattr(
                    sorted_hand[j],
                    "cost",
                    0,
                )
                if cost_i > cost_j:
                    sorted_hand[i], sorted_hand[j] = (
                        sorted_hand[j],
                        sorted_hand[i],
                    )

        cards_played: list[str] = []
        mana_used = 0
        mana_limit = 10

        for card in sorted_hand:
            card_cost = getattr(card, "cost", 0)
            if mana_used + card_cost <= mana_limit:
                cards_played.append(getattr(card, "name", "Unknown"))
                mana_used += card_cost

        if battlefield:
            targets_attacked = ["Enemy Creatures"]
        else:
            targets_attacked = ["Enemy Player"]

        damage_dealt = 0
        for card in sorted_hand:
            if getattr(card, "name", "") in cards_played:
                base_damage = getattr(
                    card,
                    "attack",
                    getattr(card, "attack_power", 0),
                )
                if base_damage == 0:
                    base_damage = getattr(card, "cost", 0)
                damage_dealt += base_damage

        return {
            "cards_played": cards_played,
            "mana_used": mana_used,
            "targets_attacked": targets_attacked,
            "damage_dealt": damage_dealt,
        }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(
        self,
        available_targets: list[Any],
    ) -> list[Any]:
        targets = list(available_targets)
        for i in range(len(targets)):
            for j in range(i + 1, len(targets)):
                health_i = getattr(targets[i], "health", 0)
                health_j = getattr(targets[j], "health", 0)
                if health_i < health_j:
                    targets[i], targets[j] = targets[j], targets[i]
        return targets
