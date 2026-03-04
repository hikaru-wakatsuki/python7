from ex0 import Card, CreatureCard
from enum import Enum


class EffectType(Enum):
    DAMEGE = 'damege'
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
            raise ValueError()

    def play(self, game_state: dict) -> dict:
        game_state.update({
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': f'Deal {self.cost} {self.effect_type.value()} to target'
        })
        return game_state

    def resolve_effect(
            self, targets: list[CreatureCard]
            ) -> dict[CreatureCard, bool]:
        is_alive: bool = True
        result: dict[CreatureCard, bool] = {}
        for target in targets:
            if self.effect_type.value() == 'damege':
                target.health -= self.cost
                if target.health < 0:
                    target.health = 0
                    is_alive = False
            if self.effect_type.value() == 'heal':
                target.health += self.cost
            if self.effect_type.value() == 'buff':
                target.attack += self.cost
            if self.effect_type.value() == 'debuff':
                target.attack -= self.cost
                if target.attack < 0:
                    target.attack = 0
            result.update({target: is_alive})
        return result
