from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform
from typing import Any


def main():
    try:
        print()
        print("=== DataDeck Tournament Platform ===")
        print()
        print("Registering Tournament Cards...")
        platform: TournamentPlatform = TournamentPlatform()
        print()
        dragon: TournamentCard = TournamentCard(
            'Fire Dragon', 5, 'Legendary', 7, 5, 'dragon_001', 1200)
        platform.register_card(dragon)
        print(f"{dragon.name} (ID: {dragon.card_id}):")
        print("- Interfaces: [Card, Combatable, Rankable]")
        print(f"- Rating: {dragon.rating}")
        print(f"- Record: {dragon.get_tournament_stats().get('record')}")
        print()
        wizard: TournamentCard = TournamentCard(
            'Ice Wizard', 4, 'Epic', 4, 4, 'wizard_001', 1150)
        platform.register_card(wizard)
        print(f"{wizard.name} (ID: {wizard.card_id}):")
        print("- Interfaces: [Card, Combatable, Rankable]")
        print(f"- Rating: {wizard.rating}")
        print(f"- Record: {wizard.get_tournament_stats().get('record')}")
        print()
        print("Creating tournament match...")
        result: dict[str, Any]
        result = platform.create_match("dragon_001", "wizard_001")
        print(f"Match result: {result}")
        print()
        print("Tournament Leaderboard:")
        leaderboard: list[TournamentCard] = platform.get_leaderboard()
        i: int = 1
        for card in leaderboard:
            print(f"{i}. {card.name} - Rating: {card.rating} "
                  f"({card.get_tournament_stats().get('record')})")
            i += 1
        print()
        print("Platform Report:")
        print(platform.generate_tournament_report())
        print()
        print("=== Tournament Platform Successfully Deployed! ===")
        print("All abstract patterns working together harmoniously!")
    except (KeyError, IndexError, TypeError,
            ValueError) as error:
        print(error)


if __name__ == "__main__":
    main()
