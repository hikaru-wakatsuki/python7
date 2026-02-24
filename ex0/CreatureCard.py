from ex0.Card import Card
from enum import Enum
from typing import Any


class CreatureCard(Card, Enum):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int) -> None:
        super().__init__(name, cost, rarity)
        self.attack: int = attack
        self.health: int = health

    def play(self, game_state: dict) -> dict:

    def attack_target(self, target) -> dict:

    def get_card_info(self) -> dict:
        info: dict[str, Any] = super().get_card_info()
        info['type'] = 'Creature'
        info['atta']
