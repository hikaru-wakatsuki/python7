from ex0.Card import Card
from enum import Enum
from typing import Any


class Effect(Enum):
    MANA = 'mana'
    HEALTH = 'health'
    ATTACK = 'attack'


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str) -> None:
        super().__init__(name, cost, rarity)
        if durability <= 0:
            raise ValueError(
                f"{self.name} durability must be a positive integer.")
        self.durability: int = durability
        try:
            self.effect: Effect = Effect(effect)
        except ValueError:
            raise ValueError(f"{self.name} has invalid effect")

    def play(self, game_state: dict) -> dict:
        if 'field_creatures' not in game_state:
            raise KeyError("game_state must contain 'field_creatures'")
        field_creatures: list[Card]
        field_creatures = game_state.get('field_creatures')
        result: dict[str, Any] = self.activate_ability()
        if result.get('active'):
            for card in field_creatures:
                if self.effect == Effect.MANA:
                    if hasattr(card, 'mana'):
                        card.mana += 1
                elif self.effect == Effect.ATTACK:
                    if hasattr(card, 'attack'):
                        card.attack += 1
                else:
                    if hasattr(card, 'health'):
                        card.health += 1
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': result.get('description')
        }

    def activate_ability(self) -> dict:
        if self.durability <= 0:
            return {
                'active': False,
                'effect': self.effect.value,
                'description': 'ArtifactCard is destroyed'
            }
        self.durability -= 1
        return {
            'active': True,
            'effect': self.effect.value,
            'description': f'Permanent: +1 {self.effect.value} per turn'
        }
