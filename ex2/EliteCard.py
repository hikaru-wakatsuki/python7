from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int, mana: int) -> None:
        super().__init__(name, cost, rarity)
        if attack <= 0:
            raise ValueError("Attack must be positive integers.")
        if health <= 0:
            raise ValueError("Health must be positive integers.")
        if mana <= 0:
            raise ValueError("Mana must be positive integers.")
        self.attack: int = attack
        self.health: int = health
        self.mana: int = mana

    def play(self, game_state: dict) -> dict:
        field_creatures: list[Card]
        try:
            field_creatures = game_state.get('field_creatures')
        except KeyError:
            raise KeyError()
        field_creatures.append(self)
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': 'Elite summoned to battlefield'
            }

    def attack(self, target) -> dict:
        if not hasattr(target, 'health'):
            raise TypeError("Target must have a 'health' attribute")
        target.health -= self.attack
        if target.health < 0:
            target.health = 0
        return {
            'attacker': self.name,
            'target': target.name,
            'damage': self.attack,
            'combat_type': 'melee'
        }

    def defend(self, incoming_damage: int) -> dict:
        blocked: int = incoming_damage // 2
        taken: int = incoming_damage - blocked
        if taken < 0:
            taken = 0
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
            "attack": self.attack,
            "health": self.health
        }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        mana

    def channel_mana(self, amount: int) -> dict:
        pass

    def get_magic_stats(self) -> dict:
        return {
            "mana": self.mana
        }
