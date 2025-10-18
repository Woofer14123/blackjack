class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0  # Track aces for flexible value calculation
    
    def add_card(self, card):
        """Add a card to the hand and recalculate value"""
        self.cards.append(card)
        self.value += card.value
        
        # Track aces
        if card.rank == 'A':
            self.aces += 1
        
        # Adjust for aces if over 21
        self._adjust_for_ace()
    
    def _adjust_for_ace(self):
        """Adjust ace value from 11 to 1 if hand is over 21"""
        while self.value > 21 and self.aces > 0:
            self.value -= 10  # Change ace from 11 to 1
            self.aces -= 1
    
    def clear(self):
        """Clear the hand for a new round"""
        self.cards = []
        self.value = 0
        self.aces = 0
    
    def __str__(self):
        return ", ".join(str(card) for card in self.cards)