from ex0.CreatureCard import CreatureCard
from typing import Dict, Any


def main() -> None:
    print()
    print("=== DataDeck Card Foundation ===")
    print()
    print("Testing Abstract Base Class Design:")
    print()
    print("CreatureCard Info:")
    red_dragon: CreatureCard
    red_dragon = CreatureCard('Fire Dragon', 5, 'Legendary', 7, 5)
    print(f"{red_dragon.get_card_info()}")
    print()
    print("Playing Fire Dragon with 6 mana available:")
    print(f"Playable: {red_dragon.is_playable(6)}")
    game_state: Dict[str, Any] = {}
    print(f"Play result: {red_dragon.play(game_state)}")
    print("Fire Dragon attacks Goblin Warrior:")
    goblin_warrior: CreatureCard
    goblin_warrior = CreatureCard('Goblin Warrior', 1, 'Common', 1, 1)
    print(f"Attack result: {red_dragon.attack_target(goblin_warrior)}")
    print()
    print("Testing insufficient mana (3 available):")
    print(f"Playable: {red_dragon.is_playable(3)}")
    print()
    print("Abstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
