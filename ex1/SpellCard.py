from ex0.Card import Card


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect = effect_type
        self.consumed = False  # Spells are consumed when played (one-time use)

    def resolve_effect(self) -> str:
        effect_phrases = {
            "damage": "Deal 3 damage to target",
            "heal": "Restore 3 health to target",
            "buff": "Give target creature +2/+2",
            "debuff": "Silence target creature",
        }
        effect_type = str(self.effect).lower()
        return effect_phrases.get(effect_type, "No valid spell effect")

    def play(self, game_state: dict) -> dict:
        if self.consumed:
            return {
                "card_played": self.name,
                "mana_used": 0,
                "effect": "Spell already consumed",
                "consumed": True,
            }

        available_mana = game_state["available_mana"]
        playable = self.is_playable(available_mana)
        if playable:
            self.consumed = True
            return {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": self.resolve_effect(),
            }
        return {}
