from ex0.Card import Card
from ex2.EliteCard import EliteCard
from typing import Any, Dict


def main() -> None:
    print()
    print("=== DataDeck Ability System ===")
    print()
    print("EliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")
    print()
    print("Playing Arcane Warrior (Elite Card):")
    print()
    print("Combat phase:")
    arcane_warrior: EliteCard = EliteCard(
        'Arcane Warrior', 4, 'Epic', 5, 10, 8)
    enemy: EliteCard = EliteCard('Enemy', 1, 'Common', 1, 1, 1)
    enemy1: EliteCard = EliteCard('Enemy1', 1, 'Common', 1, 1, 1)
    enemy2: EliteCard = EliteCard('Enemy2', 1, 'Common', 1, 1, 1)
    game_state: Dict[str, Any] = {'field_creatures': []}
    enemy1.play(game_state)
    enemy2.play(game_state)
    print(f"Attack result: {arcane_warrior.attack(enemy)}")
    print(f"Defense result: {arcane_warrior.defend(5)}")
    print()
    print("Magic phase:")
    targets: list[Card] = game_state.get('field_creatures')
    print(f"Spell cast: {arcane_warrior.cast_spell('Fireball', targets)}")
    print(f"Mana channel: {arcane_warrior.channel_mana(3)}")
    print()
    print("Multiple interface implementation successful!")
