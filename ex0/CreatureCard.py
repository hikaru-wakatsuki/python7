from ex0.Card import Card
from typing import Any


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
        return {
            'card_player': self.name,
            'mana_used': self.cost,
            'effect': game_state.values
            }

    def attack_target(self, target: "CreatureCard") -> dict:
        combat_resolved: bool
        if self.attack >= target.health:
            combat_resolved = True
        else:
            combat_resolved = False
        return {
            'attacker': self.name,
            'target': target.name,
            'damage_dealt': self.attack,
            'combat_resolved': combat_resolved
            }

    def get_card_info(self) -> dict:
        info: dict[str, Any] = super().get_card_info()
        info.update({
            'type': 'Creature',
            'attack': self.attack,
            'health': self.health,
        })
        return info
