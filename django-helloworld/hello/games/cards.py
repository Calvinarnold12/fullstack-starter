import random

class Card:
    def __init__(self, suit, rank, is_face_up=False):
        self.suit = suit  # 'Hearts', 'Diamonds', 'Clubs', 'Spades'
        self.rank = rank  # 1 (Ace) through 13 (King)
        self.is_face_up = is_face_up

    @property
    def color(self):
        return 'Red' if self.suit in ['Hearts', 'Diamonds'] else 'Black'

    @property
    def rank_display(self):
        return {1: 'A', 11: 'J', 12: 'Q', 13: 'K'}.get(self.rank, str(self.rank))

    @property
    def suit_symbol(self):
        return {
            'Hearts': '♥',
            'Diamonds': '♦',
            'Clubs': '♣',
            'Spades': '♠'
        }[self.suit]

    def to_dict(self):
        """Crucial for saving game state to your Django database later."""
        return {
            'suit': self.suit,
            'rank': self.rank,
            'rank_display': self.rank_display,
            'suit_symbol': self.suit_symbol,
            'is_face_up': self.is_face_up,
            'color': self.color
        }