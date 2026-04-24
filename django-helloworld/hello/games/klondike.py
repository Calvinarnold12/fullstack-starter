from .base import BaseSolitaire

class Klondike(BaseSolitaire):
    def setup_board(self):
        self.stock = []
        self.waste = []
        self.foundations = [[] for _ in range(4)]
        self.tableaus = [[] for _ in range(7)]

        self.generate_deck(decks=1)

        for tableau_index in range(7):
            for card_index in range(tableau_index + 1):
                card = self.stock.pop()
                card.is_face_up = (card_index == tableau_index)
                self.tableaus[tableau_index].append(card)

    def is_valid_move(self, card, destination):
        # Placeholder for future move validation rules.
        return True

    def draw_from_stock(self):
        if self.stock:
            card = self.stock.pop()
            card.is_face_up = True
            self.waste.append(card)