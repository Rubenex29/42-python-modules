from typing import Dict, List
from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    def __init__(self) -> None:
        self._participants: Dict[str, TournamentCard] = {}
        self._matches_played: int = 0

    def register_card(self, card: TournamentCard) -> str:
        base_name = card.name.lower().replace(" ", "_")
        card_id = f"{base_name}_001"
        suffix = 1

        while card_id in self._participants:
            suffix += 1
            card_id = f"{base_name}_{suffix:03d}"

        self._participants[card_id] = card
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        if card1_id not in self._participants:
            return {"error": f"Card not found: {card1_id}"}
        if card2_id not in self._participants:
            return {"error": f"Card not found: {card2_id}"}
        if card1_id == card2_id:
            return {"error": "Cannot create match with same card"}

        card1 = self._participants[card1_id]
        card2 = self._participants[card2_id]

        result = card1.process_match(card2)
        self._matches_played += 1

        winner_id = (card1_id if result["winner"] == card1.name
                     else card2_id)
        loser_id = card2_id if winner_id == card1_id else card1_id

        return {
            "winner": winner_id,
            "loser": loser_id,
            "winner_rating": result["winner_rating"],
            "loser_rating": result["loser_rating"],
        }

    def get_leaderboard(self) -> list:
        leaderboard: List[dict] = []
        for card_id, card in self._participants.items():
            info = card.get_rank_info()
            info["card_id"] = card_id
            leaderboard.append(info)

        def rating_key(item: dict) -> int:
            return item["rating"]

        leaderboard.sort(key=rating_key, reverse=True)
        return leaderboard

    def generate_tournament_report(self) -> dict:
        total_cards = len(self._participants)
        total_rating = sum(
            card.calculate_rating()
            for card in self._participants.values()
        )
        avg_rating = (
            total_rating // total_cards if total_cards > 0 else 0
        )

        return {
            "total_cards": total_cards,
            "matches_played": self._matches_played,
            "avg_rating": avg_rating,
            "platform_status": (
                "active" if total_cards > 0 else "inactive"
            ),
        }
