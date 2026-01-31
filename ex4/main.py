from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main():
    print("=== DataDeck Tournament Platform ===\n")

    # Create tournament platform
    platform = TournamentPlatform()

    # Create tournament cards
    print("Registering Tournament Cards...\n")
    fire_dragon = TournamentCard(
        name="Fire Dragon",
        cost=5,
        rarity="Legendary",
        attack=8,
        health=10,
        base_rating=1200
    )

    ice_wizard = TournamentCard(
        name="Ice Wizard",
        cost=4,
        rarity="Epic",
        attack=6,
        health=8,
        base_rating=1150
    )

    # Register cards and get IDs
    dragon_id = platform.register_card(fire_dragon)
    wizard_id = platform.register_card(ice_wizard)

    # Display card information
    print(f"{fire_dragon.name} (ID: {dragon_id}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {fire_dragon.calculate_rating()}")
    print(f"- Record: {fire_dragon.wins}-{fire_dragon.losses}\n")

    print(f"{ice_wizard.name} (ID: {wizard_id}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {ice_wizard.calculate_rating()}")
    print(f"- Record: {ice_wizard.wins}-{ice_wizard.losses}\n")

    # Create tournament match
    print("Creating tournament match...")
    match_result = platform.create_match(dragon_id, wizard_id)
    print(f"Match result: {match_result}\n")

    # Display leaderboard
    print("Tournament Leaderboard:")
    leaderboard = platform.get_leaderboard()
    print(leaderboard)
    for idx, entry in enumerate(leaderboard, 1):
        card_name = entry["card"]
        rating = entry["rating"]
        wins = entry["wins"]
        losses = entry["losses"]
        print(f"{idx}. {card_name} - Rating: {rating} ({wins}-{losses})")

    # Generate platform report
    print("\nPlatform Report:")
    report = platform.generate_tournament_report()
    print(report)

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
