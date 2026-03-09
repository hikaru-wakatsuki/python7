from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from random import shuffle


class Deck:
    def __init__(self) -> None:
        self.deck: list[Card] = []

    def add_card(self, card: Card) -> None:
        if not isinstance(card, Card):
            raise TypeError("Must be a Card")
        self.deck.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.deck:
            if card.name == card_name:
                self.deck.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        shuffle(self.deck)

    def draw_card(self) -> Card:
        if not self.deck:
            raise IndexError("Deck is empty")
        return self.deck.pop()

    def get_deck_stats(self) -> dict:
        total_cards: int = len(self.deck)
        total_cost: int = 0
        total_creatures: int = 0
        total_spells: int = 0
        total_artifacts: int = 0
        for card in self.deck:
            if isinstance(card, CreatureCard):
                total_creatures += 1
            elif isinstance(card, SpellCard):
                total_spells += 1
            elif isinstance(card, ArtifactCard):
                total_artifacts += 1
            total_cost += card.cost
        avg_cost: float = total_cost / total_cards if total_cards > 0 else 0
        return {
            'total_cards': total_cards,
            'creatures': total_creatures,
            'spells': total_spells,
            'artifacts': total_artifacts,
            'avg_cost': avg_cost
        }
