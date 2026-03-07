from ex3.GameStrategy import GameStrategy
from ex3.CardFactory import CardFactory
from ex0.Card import Card


class GameEngine:
    def __init__(self) -> None:
        self.factory: CardFactory | None = None
        self.strategy: GameStrategy | None = None
        self.turns_simulated: int = 0
        self.total_damage: int = 0
        self.cards_created: int = 0
        self.hand: list[Card] = []
        self.battlefield: list[Card] = []

    def configure_engine(
            self, factory: CardFactory, strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> dict:
        if not self.factory or not self.strategy:
            raise RuntimeError("GameEngine is not configured")
        try:
            self.hand.append(self.factory.create_creature("dragon"))
            self.hand.append(self.factory.create_creature("goblin"))
            self.hand.append(self.factory.create_spell("lightning"))
            self.cards_created += len(self.hand)
            result: dict
            result = self.strategy.execute_turn(self.hand, self.battlefield)
        except (TypeError, ValueError) as error:
            raise RuntimeError(error)
        self.turns_simulated += 1
        self.total_damage += result.get("damage_dealt")
        return result

    def get_engine_status(self) -> dict:
        strategy_name: str = (
            self.strategy.get_strategy_name()
            if self.strategy else "None")
        return {
            "turns_simulated": self.turns_simulated,
            "strategy_used": strategy_name,
            "total_damage": self.total_damage,
            "cards_created": self.cards_created,
        }
