from abc import ABC, abstractmethod
from enum import Enum


class Rarity(Enum):
    COMMON = 'Common'
    RARE = "Rare"
    EPIC = "Epic"
    LEGENDARY = "Legendary"


class Card(ABC):
    def __init__(self,  name: str, cost: int, rarity: str) -> None:
        if not name or not name.strip():
            raise ValueError(
                f"{self.name} card name must be a non-empty string.")
        self.name: str = name
        if cost < 0:
            raise ValueError(f"{self.name} cost must be non-negative.")
        self.cost: int = cost
        try:
            self.rarity: Rarity = Rarity(rarity)
        except ValueError:
            raise ValueError(f"{self.name} invalid rarity: {rarity}")

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        pass

    def get_card_info(self) -> dict:
        return {
            'name': self.name,
            'cost': self.cost,
            'rarity': self.rarity.value
        }

    def is_playable(self, available_mana: int) -> bool:
        return available_mana >= self.cost
