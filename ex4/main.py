from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main():

    print("=== DataDeck Tournament Platform ===")

    platform = TournamentPlatform()

    print("Registering Tournament Cards...")

    dragon = TournamentCard("Fire Dragon", 5, 6, 10, "dragon_001")
    wizard = TournamentCard("Ice Wizard", 4, 4, 8, "wizard_001")

    platform.register_card(dragon)
    platform.register_card(wizard)

    print("Fire Dragon (ID: dragon_001):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print("- Rating:", dragon.rating)
    print("- Record: 0-0")

    print("Ice Wizard (ID: wizard_001):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print("- Rating:", wizard.rating)
    print("- Record: 0-0")

    print("Creating tournament match...")

    result = platform.create_match("dragon_001", "wizard_001")

    print("Match result:", result)

    print("Tournament Leaderboard:")

    leaderboard = platform.get_leaderboard()

    for i, card in enumerate(leaderboard, 1):
        print(f"{i}. {card.name} - Rating: {card.rating} ({card.wins}-{card.losses})")

    print("Platform Report:")

    print(platform.generate_tournament_report())

    print("=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
