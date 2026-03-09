from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int, mana: int) -> None:
        super().__init__(name, cost, rarity)
        if attack <= 0:
            raise ValueError(f"{self.name} attack must be a positive integer.")
        if health <= 0:
            raise ValueError(f"{self.name} health must be a positive integer.")
        if mana <= 0:
            raise ValueError(f"{self.name} mana must be a positive integer.")
        self.attack_power: int = attack
        self.health: int = health
        self.mana: int = mana

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
            'effect': 'Elite summoned to battlefield'
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
        if incoming_damage < 0:
            raise ValueError(f"{self.name} incoming_damage must be positive")
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

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        if self.mana < self.cost:
            return {
                "caster": self.name,
                "spell": spell_name,
                "targets": [],
                "mana_used": 0
            }
        self.mana -= self.cost
        for target in targets:
            if not hasattr(target, 'health'):
                raise TypeError("Target must have a 'health' attribute")
            target.health -= self.cost
            if target.health < 0:
                target.health = 0
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": [t.name for t in targets],
            "mana_used": self.cost
        }

    def channel_mana(self, amount: int) -> dict:
        if amount < 0:
            raise ValueError("Amount must be non-negative.")

        self.mana += amount

        return {
            "channeled": amount,
            "total_mana": self.mana
        }

    def get_magic_stats(self) -> dict:
        return {
            "mana": self.mana
        }
