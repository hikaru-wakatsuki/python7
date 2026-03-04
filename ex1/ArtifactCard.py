from ex0 import Card


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, durability: int, effect: str):
        super().__init__(name, cost, rarity)
        if durability <= 0:
            raise ValueError("Durability must be positive integers.")
        try:
            self.effect: Effect = Effect(effect)
        except ValueError:
            raise ValueError()

    def play(self, game_state: dict) -> dict:
        game_state.update({
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': f'Deal {self.cost} {self.effect_type.value()} to target'
        })

    def activate_ability(self) -> dict:
