from card import Card
import random
class Deck:
    def __init__(self):
        self.cards = []
        self.build()
    
    def build(self):
        """Build a standard 52-card deck"""
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))
    
    def shuffle(self):
        """Shuffle the deck"""
        random.shuffle(self.cards)
    
    def deal(self):
        """Deal one card from the deck"""
        if len(self.cards) == 0:
            self.build()
            self.shuffle()
        return self.cards.pop()
    
    def __len__(self):
        return len(self.cards)