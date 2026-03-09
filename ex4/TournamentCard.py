from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int, card_id: str, rating: int) -> None:
        super().__init__(name, cost, rarity)
        if attack <= 0:
            raise ValueError(f"{self.name} attack must be a positive integer.")
        if health <= 0:
            raise ValueError(f"{self.name} health must be a positive integer.")
        self.attack_power: int = attack
        self.health: int = health
        self.card_id: str = card_id
        self.initial_rating: int = rating
        self.rating: int = rating
        self.wins: int = 0
        self.losses: int = 0

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

    def attack(self, target) -> dict:
        if not isinstance(target, Card):
            raise TypeError(f"{self.name} target must be Card")
        if not hasattr(target, 'health'):
            raise TypeError("Target must have a 'health' attribute")
        target.health -= self.attack_power
        if target.health < 0:
            target.health = 0
        return {
            'attacker': self.name,
            'target': target.name,
            'damage': self.attack_power,
            'combat_type': 'melee'
        }

    def defend(self, incoming_damage: int) -> dict:
        blocked: int = incoming_damage // 2
        taken: int = incoming_damage - blocked
        if taken < 0:
            taken = 0
        self.health -= taken
        if self.health < 0:
            self.health = 0
        return {
            'defender': self.name,
            'damage_taken': taken,
            'damage_blocked': blocked,
            'still_alive': self.health > 0
        }

    def get_combat_stats(self) -> dict:
        return {
            "attack": self.attack_power,
            "health": self.health
        }

    def calculate_rating(self) -> int:
        return self.initial_rating + (self.wins * 16) - (self.losses * 16)

    def update_wins(self, wins: int) -> None:
        self.wins += wins
        self.rating = self.calculate_rating()

    def update_losses(self, losses: int) -> None:
        self.losses += losses
        self.rating = self.calculate_rating()

    def get_rank_info(self) -> dict:
        return {
            "rating": self.rating,
            "wins": self.wins,
            "losses": self.losses
        }

    def get_tournament_stats(self) -> dict:
        return {
            "id": self.card_id,
            "name": self.name,
            "rating": self.rating,
            "record": f"{self.wins}-{self.losses}"
        }
