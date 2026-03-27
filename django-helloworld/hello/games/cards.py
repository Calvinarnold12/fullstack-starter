import random

class Card:
    def __init__(self, suit, rank, is_face_up=False):
        self.suit = suit  # 'Hearts', 'Diamonds', 'Clubs', 'Spades'
        self.rank = rank  # 1 (Ace) through 13 (King)
        self.is_face_up = is_face_up

    @property
    def color(self):
        return 'Red' if self.suit in ['Hearts', 'Diamonds'] else 'Black'

    def to_dict(self):
        """Crucial for saving game state to your Django database later."""
        return {
            'suit': self.suit,
            'rank': self.rank,
            'is_face_up': self.is_face_up
        }