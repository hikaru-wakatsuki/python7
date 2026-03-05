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
            raise ValueError("Durability must be positive integers.")
        self.durability: int = durability
        try:
            self.effect: Effect = Effect(effect)
        except ValueError:
            raise ValueError("Invalid effect type")

    def play(self, game_state: dict) -> dict:
        result: dict[str, Any] = self.activate_ability()
        game_state.update(result)
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
