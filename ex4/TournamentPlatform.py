from random import choice
from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    def __init__(self):
        self.cards: dict[str, TournamentCard] = {}
        self.matches_played: int = 0

    def register_card(self, card: TournamentCard) -> str:
        self.cards[card.card_id] = card
        return card.card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        card1: TournamentCard = self.cards.get(card1_id)
        card2: TournamentCard = self.cards.get(card2_id)
        if not card1 or not card2:
            raise ValueError("Card not found")
        card1_health_backup: int = card1.get_combat_stats()["health"]
        card2_health_backup: int = card2.get_combat_stats()["health"]
        winner: TournamentCard
        while True:
            first: TournamentCard
            second: TournamentCard
            if card1.cost < card2.cost:
                first = card1
            elif card1.cost > card2.cost:
                first = card2
            else:
                first = choice([card1, card2])
            second = (card2 if first == card1 else card1)
            first.attack(second)
            if second.health == 0:
                winner = first
                break
            second.attack(first)
            if first.health == 0:
                winner = second
                break
        loser: TournamentCard = first if winner == second else second
        card1.health = card1_health_backup
        card2.health = card2_health_backup
        winner.update_wins(1)
        loser.update_losses(1)
        self.matches_played += 1
        return {
            "winner": winner.card_id,
            "loser": loser.card_id,
            "winner_rating": winner.rating,
            "loser_rating": loser.rating
        }

    def get_leaderboard(self) -> list:
        leaderboard: list[TournamentCard]
        leaderboard = sorted(
            self.cards.values(), key=lambda c: c.rating, reverse=True)
        return leaderboard

    def generate_tournament_report(self) -> dict:
        total_cards: int = len(self.cards)
        avg_rating: float = (
            sum(card.rating for card in self.cards.values())
            // total_cards if total_cards else 0)
        return {
            "total_cards": total_cards,
            "matches_played": self.matches_played,
            "avg_rating": avg_rating,
            "platform_status": "active"
        }
