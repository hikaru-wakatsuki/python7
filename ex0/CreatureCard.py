from ex0.Card import Card
from typing import Any, Dict


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int) -> None:
        super().__init__(name, cost, rarity)
        if attack <= 0:
            raise ValueError("Attack must be positive integers.")
        if health <= 0:
            raise ValueError("Health must be positive integers.")
        self.attack: int = attack
        self.health: int = health

    def play(self, game_state: dict) -> dict:
        field_creatures: list["CreatureCard"] | None
        field_creatures = game_state.get('field_creatures')
        field_creatures.append(self)
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': 'Creature summoned to battlefield'
            }

    def attack_target(self, target: "CreatureCard") -> dict:
        return {
            'attacker': self.name,
            'target': target.name,
            'damage_dealt': self.attack,
            'combat_resolved': True
            }

    def get_card_info(self) -> dict:
        info: Dict[str, Any] = super().get_card_info()
        info.update({
            'type': 'Creature',
            'attack': self.attack,
            'health': self.health,
        })
        return info
