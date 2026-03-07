from ex3.GameEngine import GameEngine
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.FantasyCardFactory import FantasyCardFactory


def main() -> None:
    try:
        print()
        print("=== DataDeck Game Engine ===")
        print()
        print("Configuring Fantasy Card Game...")
        print("Factory: FantasyCardFactory")
        print("Strategy: AggressiveStrategy")
        card_factory: FantasyCardFactory = FantasyCardFactory()
        print(f"Available types: {card_factory.get_supported_types()}")
        print()
        print("Simulating aggressive turn...")
        print("Hand: [Fire Dragon (5), Goblin Warrior (2), "
              "Lightning Bolt (3)]")
        print()
        print("Turn execution:")
        game_engine: GameEngine = GameEngine()
        game_engine.configure_engine(
            FantasyCardFactory(), AggressiveStrategy())
        result: dict = game_engine.simulate_turn()
        print(f"Strategy: {game_engine.get_engine_status()['strategy_used']}")
        print(f"Actions: {result}")
        print()
        print("Game Report:")
        print(game_engine.get_engine_status())
        print()
        print("Abstract Factory + Strategy Pattern: "
              "Maximum flexibility achieved!")
    except (KeyError, IndexError, TypeError,
            ValueError, RuntimeError) as error:
        print(error)


if __name__ == "__main__":
    main()
