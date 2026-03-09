from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck
from typing import Any


def main() -> None:
    print()
    print("=== DataDeck Deck Builder ===")
    print()
    print("Building deck with different card types...")
    try:
        deck: Deck = Deck()
        deck.add_card(ArtifactCard('Mana Crystal', 4, 'Common', 2, 'mana'))
        deck.add_card(SpellCard('Lightning Bolt', 3, 'Rare', 'damage'))
        deck.add_card(CreatureCard('Fire Dragon', 5, 'Legendary', 7, 5))
        print(f"Deck stats: {deck.get_deck_stats()}")
        print()
        print("Drawing and playing cards:")
        game_state: dict[str, Any] = {'field_creatures': []}
        print()
        print("Drew: Fire Dragon (Creature)")
        first_draw: Card = deck.draw_card()
        print(f"Play result: {first_draw.play(game_state)}")
        print()
        print("Draw: Lightning Bolt (Spell)")
        second_draw: Card = deck.draw_card()
        print(f"Play result: {second_draw.play(game_state)}")
        print()
        print("Draw: Mana Crystal (Artifact)")
        third_draw: Card = deck.draw_card()
        print(f"Play result: {third_draw.play(game_state)}")
    except (KeyError, IndexError, TypeError, ValueError) as error:
        print(error)
    print()
    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
