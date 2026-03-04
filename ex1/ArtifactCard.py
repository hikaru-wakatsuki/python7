from ex0 import Card, CreatureCard
from enum import Enum


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
            raise ValueError()

    def play(self, game_state: dict) -> dict:
        targets: list[CreatureCard] = game_state.get('targets', [])
        result: dict[str, str] = self.resolve_effect(targets)
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': f'Permanent: +1 mana per turn'
        }

    def activate_ability(self) -> dict:
        if self.durability <= 0:
            return {
                'active': False,
                'effect': self.effect,
                'description': 'ArtifactCard is destroyed'
            }
        self.durability -= 1
        return {
            'active': True,
            'effect': self.effect,
            'description': f'Permanent: +1 {self.effect.value} per turn'
        }
