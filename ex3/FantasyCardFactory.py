from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


class CardFactory():
    def __init__(self):
        self.registered_cards = {}

        dragon = CreatureCard("dragon", 5, "Legendary", 5, 5)
        self.register_card("dragon", dragon)

        goblin = CreatureCard("goblin", 2, "Rare", 5, 5)
        self.register_card("goblin", goblin)

        fireball = SpellCard("fireball", 4, "super rare", "damage")
        self.register_card("fireball", fireball)

        ice = SpellCard("Ice", 4, "Epic", "debuff")
        self.register_card("ice", ice)

        lightning = SpellCard("Lightning Bolt", 3, "Epic", "damage")
        self.register_card("lightning", lightning)

        ring = ArtifactCard("Ring of Power", 3, "Rare", 5, "boost_attack")
        self.register_card("ring", ring)

        staff = ArtifactCard("Mage Staff", 4, "Epic", 8, "mana_regen")
        self.register_card("staff", staff)

        crystal = ArtifactCard("Crystal Orb", 2, "Rare", 4, "spell_amplify")
        self.register_card("crystal", crystal)

    def register_card(self, card_type: str, card) -> None:
        self.registered_cards[card_type] = card

    def get_card(self, card_type: str):
        return self.registered_cards.get(card_type)

    def list_cards(self) -> list:
        return list(self.registered_cards.keys())
