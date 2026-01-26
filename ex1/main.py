from ex1.Deck import Deck
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex0.CreatureCard import CreatureCard


print("=== DataDeck Deck Builder ===\n")
print("Building deck with different card types...")
creature = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
spell = SpellCard("Lightning Bolt", 3, "Epic", "damage")
artifact = ArtifactCard("Mana Crysta", 2, "Epic", 999,
                        "Permanent: +1 mana per turn")
deck = Deck()
deck.add_card(creature)
deck.add_card(spell)
deck.add_card(artifact)
print(f"Deck stats: {deck.get_deck_stats()}")
print("\nDrawing and playing cards:\n")
print("Drew: Lightning Bolt (Spell)")
print(f"Play result: {spell.play({"available_mana": 3})}")
print("\nDrew: Mana Crystal (Artifact)")
print(f"Play result: {artifact.play({"available_mana": 2})}")
print("\nDrew: Fire Dragon (Creature)")
print(f"Play result: {creature.play({"available_mana": 5})}")
print("\nPolymorphism in action: Same interface, different card behaviors!")
