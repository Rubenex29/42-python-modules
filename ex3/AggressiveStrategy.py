from typing import Any


class GameStrategy():
    def __init__(self, type: str) -> None:
        self.strategy = type

    def execute_turn(
        self,
        hand: list[dict[str, Any]],
        battlefield: list[Any],
    ) -> dict[str, Any]:
        # Sort the hand by cost (ascending) to maximize plays under mana limit.
        for i in range(len(hand)):
            for j in range(i + 1, len(hand)):
                if hand[i]['cost'] > hand[j]['cost']:
                    hand[i], hand[j] = hand[j], hand[i]

        cards_played = []
        mana_used = 0
        mana_limit = 10

        for card in hand:
            if mana_used + card['cost'] <= mana_limit:
                cards_played.append(card['name'])
                mana_used += card['cost']

        damage = sum(card['cost']
                     for card in hand if card['name'] in cards_played)

        # If the battlefield has enemies, attack creatures
        # otherwise, attack player.
        if len(battlefield) > 0:
            targets_attacked = ['Enemy Creatures']
        else:
            targets_attacked = ['Enemy Player']

        return {
            'cards_played': cards_played,
            'mana_used': mana_used,
            'targets_attacked': targets_attacked,
            'damage_dealt': damage
        }

    def get_strategy_name(self) -> str:
        return self.strategy

    def prioritize_targets(
        self,
        available_targets: list[dict[str, Any]],
    ) -> list[dict[str, Any]]:
        at = available_targets
        for i in range(len(at)):
            for j in range(i + 1, len(at)):
                if at[i]['damage'] < at[j]['damage']:
                    at[i], at[j] = at[j], at[i]
        return at
