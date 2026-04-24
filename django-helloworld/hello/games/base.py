import random
from .cards import Card

class BaseSolitaire:
    def __init__(self):
        # The universal zones of almost every Solitaire game
        self.stock = []         # The draw pile
        self.waste = []         # The discard/face-up pile
        self.foundations = []   # The winning piles (usually 4)
        self.tableaus = []      # The main playing columns

    def generate_deck(self, decks=1):
        """Generates one or more standard 52-card decks and shuffles them."""
        self.stock = []
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        for _ in range(decks):
            for suit in suits:
                for rank in range(1, 14):
                    self.stock.append(Card(suit, rank))
        random.shuffle(self.stock)

    def setup_board(self):
        """
        Abstract method: Every variant (Klondike, Spider) must 
        define how it deals the initial cards.
        """
        raise NotImplementedError("Subclasses must implement setup_board()")

    def is_valid_move(self, card, destination):
        """
        Abstract method: The rules for moving cards change drastically 
        between variants.
        """
        raise NotImplementedError("Subclasses must implement move validation")

    def check_win_condition(self):
        """Checks if all foundations are full (13 cards each)."""
        return all(len(f) == 13 for f in self.foundations)

    def to_dict(self):
        return {
            'stock_count': len(self.stock),
            'stock': [card.to_dict() for card in self.stock],
            'waste': [card.to_dict() for card in self.waste],
            'foundations': [[card.to_dict() for card in foundation] for foundation in self.foundations],
            'tableaus': [[card.to_dict() for card in tableau] for tableau in self.tableaus]
        }