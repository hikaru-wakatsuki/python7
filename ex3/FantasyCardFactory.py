from ex3.CardFactory import CardFactory
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from random import choice


class FantasyCardFactory(CardFactory):

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        if name_or_power == 'dragon':
            return CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
        elif name_or_power == 'goblin':
            return CreatureCard("Goblin Warrior", 2, "Common", 2, 2)
        else:
            raise ValueError("Unknown creature type")

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        if name_or_power == 'fire':
            return SpellCard("Fireball", 4, "Rare", "damage")
        elif name_or_power == 'ice':
            return SpellCard("Ice Shard", 3, "Rare", "debuff")
        elif name_or_power == 'lightning':
            return SpellCard("Lightning Bolt", 3, "Rare", "damage")
        else:
            raise ValueError("Unknown spell type")

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        if name_or_power == 'ring':
            return ArtifactCard("Mana Ring", 2, "Common", 5, "mana")
        elif name_or_power == 'staff':
            return ArtifactCard("Wizard Staff", 4, "Rare", 6, "health")
        elif name_or_power == 'crystal':
            return ArtifactCard("Magic Crystal", 3, "Common", 4, "mana")
        else:
            raise ValueError("Unknown artifact type")

    def create_themed_deck(self, size: int) -> dict:
        deck: list[Card] = []
        creatures: list[str] = ["dragon", "goblin"]
        spells: list[str] = ["fire", "ice", "lightning"]
        artifacts: list[str] = ["ring", "staff", "crystal"]
        for _ in range(size):
            card_type: str = choice(["creature", "spell", "artifact"])
            if card_type == "creature":
                deck.append(self.create_creature(choice(creatures)))
            elif card_type == "spell":
                deck.append(self.create_spell(choice(spells)))
            else:
                deck.append(self.create_artifact(choice(artifacts)))
        return {"deck": deck}

    def get_supported_types(self) -> dict:
        return {
            "creatures": ["dragon", "goblin"],
            "spells": ["fire", "ice", "lightning"],
            "artifacts": ["ring", "staff", "crystal"],
        }
