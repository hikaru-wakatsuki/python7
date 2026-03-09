from ex0.Card import Card
from typing import Any


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int) -> None:
        super().__init__(name, cost, rarity)
        if attack <= 0:
            raise ValueError(f"{self.name} attack must be a positive integer.")
        if health <= 0:
            raise ValueError(f"{self.name} health must be a positive integer.")
        self.attack: int = attack
        self.health: int = health

    def play(self, game_state: dict) -> dict:
        if 'field_creatures' not in game_state:
            raise KeyError("game_state must contain 'field_creatures'")
        field_creatures: list[Card]
        field_creatures = game_state.get('field_creatures')
        if not isinstance(field_creatures, list):
            raise TypeError("game_state['field_creatures'] must be a list")
        field_creatures.append(self)
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': 'Creature summoned to battlefield'
            }

    def attack_target(self, target) -> dict:
        if not isinstance(target, Card):
            raise TypeError(f"{self.name} target must be a Card")
        if not hasattr(target, 'health'):
            raise TypeError(f"{self.name} target must have a "
                            f"'health' attribute")
        target.health -= self.attack
        if target.health < 0:
            target.health = 0
        return {
            'attacker': self.name,
            'target': target.name,
            'damage_dealt': self.attack,
            'combat_resolved': True
            }

    def get_card_info(self) -> dict:
        info: dict[str, Any] = super().get_card_info()
        info.update({
            'type': 'Creature',
            'attack': self.attack,
            'health': self.health,
        })
        return info
