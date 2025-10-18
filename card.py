class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = self._calculate_value()
    
    def _calculate_value(self):
        """Calculate the value of the card"""
        if self.rank in ['J', 'Q', 'K']:
            return 10
        elif self.rank == 'A':
            return 11  # Ace handled as 11 initially, adjusted in Hand class
        else:
            return int(self.rank)
    
    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
    def __repr__(self):
        return f"Card('{self.suit}', '{self.rank}')"