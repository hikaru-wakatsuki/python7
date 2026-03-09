from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from enum import Enum
from typing import Any


class EffectType(Enum):
    DAMAGE = 'damage'
    HEAL = 'heal'
    BUFF = 'buff'
    DEBUFF = 'debuff'


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        try:
            self.effect_type: EffectType = EffectType(effect_type)
        except ValueError:
            raise ValueError(f"{self.name} has invalid effect type")

    def play(self, game_state: dict) -> dict:
        if 'field_creatures' not in game_state:
            raise KeyError("game_state must contain 'field_creatures'")
        targets: list[CreatureCard] = game_state.get('field_creatures')
        if not isinstance(targets, list):
            raise TypeError("game_state['field_creatures'] must be a list")
        result: dict[str, Any] = self.resolve_effect(targets)
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': result.get('description')
        }

    def resolve_effect(self, targets: list) -> dict:
        if not targets:
            return {'description': f'{self.name} has no target'}
        description: str
        for target in targets:
            if not isinstance(target, Card):
                raise TypeError(f'{self.name} targets must be Card')
            if hasattr(target, 'health'):
                if self.effect_type == EffectType.DAMAGE:
                    target.health -= self.cost
                    if target.health < 0:
                        target.health = 0
                    description = f'Deal {self.cost} damage to target'
                elif self.effect_type == EffectType.HEAL:
                    target.health += self.cost
                    description = f'Heal {self.cost} health'
            if hasattr(target, 'attack'):
                if self.effect_type == EffectType.BUFF:
                    target.attack += self.cost
                    description = f'Increase attack by {self.cost}'
                elif self.effect_type == EffectType.DEBUFF:
                    target.attack -= self.cost
                    if target.attack < 0:
                        target.attack = 0
                    description = f'Decrease attack by {self.cost}'
        return {'description': description}
