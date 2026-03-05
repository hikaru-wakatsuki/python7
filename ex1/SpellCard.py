from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from enum import Enum


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
            raise ValueError()

    def play(self, game_state: dict) -> dict:
        targets: list[CreatureCard] = game_state.get('targets', [])
        result: dict[str, str] = self.resolve_effect(targets)
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': result.get('description')
        }

    def resolve_effect(self, targets: list) -> dict:
        description: str
        for target in targets:
            if self.effect_type == EffectType.DAMAGE:
                target.health -= self.cost
                if target.health < 0:
                    target.health = 0
                description = f'Deal {self.cost} damage to target'
            elif self.effect_type == EffectType.HEAL:
                target.health += self.cost
                description = f'Heal {self.cost} health'
            elif self.effect_type == EffectType.BUFF:
                target.attack += self.cost
                description = f'Increase attack by {self.cost}'
            elif self.effect_type == EffectType.DEBUFF:
                target.attack -= self.cost
                if target.attack < 0:
                    target.attack = 0
                description = f'Decrease attack by {self.cost}'
        return {'description': description}
