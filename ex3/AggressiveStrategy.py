from ex0.Card import Card
from ex3.GameStrategy import GameStrategy
from ex1.SpellCard import EffectType
from ex1.ArtifactCard import Effect


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        cards_played: list[str] = []
        mana_used: int = 0
        targets_attacked: list[str] = []
        damage_dealt: int = 0
        hand_sorted: list[Card] = sorted(hand, key=lambda t: t.cost)
        played_creature: bool = False
        for card in hand_sorted:
            if hasattr(card, 'health') and not played_creature:
                cards_played.append(card.name)
                mana_used += card.cost
                if hasattr(card, "attack"):
                    damage_dealt += card.attack
                played_creature = True
            elif hasattr(card, 'effect_type'):
                if card.effect_type == EffectType.DAMAGE:
                    cards_played.append(card.name)
                    mana_used += card.cost
                    damage_dealt += card.cost
            elif hasattr(card, 'effect'):
                if card.effect == Effect.ATTACK:
                    cards_played.append(card.name)
                    mana_used += card.cost
        prioritized_targets: list[Card] = self.prioritize_targets(battlefield)
        if prioritized_targets:
            targets_attacked += [prioritized_targets[0].name]
        else:
            targets_attacked += ['Enemy Player']
        return {
            "cards_played": cards_played,
            "mana_used": mana_used,
            "targets_attacked": targets_attacked,
            "damage_dealt": damage_dealt
        }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        for target in available_targets:
            if not hasattr(target, 'health'):
                raise TypeError("Target must have a 'health' attribute")
        return sorted(available_targets, key=lambda t: t.health)
