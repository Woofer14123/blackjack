from deck import Deck
from hand import Hand
from card import Card
import os

class BlackjackGame:
    def __init__(self):
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        self.player_score = 0
        self.deck.shuffle()
    
    def clear_screen(self):
        """Clear the console screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def deal_initial_cards(self):
        """Deal initial two cards to player and dealer"""
        self.player_hand.clear()
        self.dealer_hand.clear()
        
        for _ in range(2):
            self.player_hand.add_card(self.deck.deal())
            self.dealer_hand.add_card(self.deck.deal())
    
    def show_hands(self, show_dealer_hidden=True):
        """Display current hands"""
        print("\n" + "="*50)
        print(f"DEALER'S HAND:")
        if show_dealer_hidden:
            # Show first card, second card hidden
            print(f"  {self.dealer_hand.cards[0]}")
            print("  [Hidden Card]")
            print(f"  Current value: {self.dealer_hand.cards[0].value} + ?")
        else:
            # Show all cards at end of game
            print(f"  {self.dealer_hand}")
            print(f"  Total value: {self.dealer_hand.value}")
        
        print(f"\nYOUR HAND:")
        print(f"  {self.player_hand}")
        print(f"  Total value: {self.player_hand.value}")
        print("="*50)
    
    def player_turn(self):
        """Handle player's turn (Hit or Stand)"""
        while self.player_hand.value < 21:
            choice = input("\nDo you want to (H)it or (S)tand? ").lower().strip()
            
            if choice in ['h', 'hit']:
                new_card = self.deck.deal()
                self.player_hand.add_card(new_card)
                self.clear_screen()
                print(f"\nYou drew: {new_card}")
                self.show_hands()
                
                if self.player_hand.value > 21:
                    print("\n*** BUST! You went over 21. ***")
                    return 'bust'
                    
            elif choice in ['s', 'stand']:
                print("\nYou chose to stand.")
                return 'stand'
            else:
                print("Please enter 'H' for Hit or 'S' for Stand.")
        
        if self.player_hand.value == 21:
            print("\n*** BLACKJACK! ***")
            return 'blackjack'
        
        return 'stand'
    
    def determine_winner(self):
        """Determine the winner and update scores"""
        player_value = self.player_hand.value
        dealer_value = self.dealer_hand.value
        
        self.clear_screen()
        print("\n" + "="*50)
        print("FINAL RESULTS:")
        print("="*50)
        self.show_hands(show_dealer_hidden=False)
        
        # Determine winner
        if player_value > 21:
            result = "dealer"
            message = "DEALER WINS! (You busted)"
            self.player_score -= 25
        elif dealer_value > 21:
            result = "player" 
            message = "YOU WIN! (Dealer busted)"
            self.player_score += 50
        elif player_value > dealer_value:
            result = "player"
            message = "YOU WIN!"
            self.player_score += 50
        elif dealer_value > player_value:
            result = "dealer"
            message = "DEALER WINS!"
            self.player_score -= 25
        else:
            result = "push"
            message = "PUSH! It's a tie."
            # No score change for ties
        
        print(f"\n*** {message} ***")
        print(f"Score change: {'+50' if result == 'player' else '-25' if result == 'dealer' else '0'}")
        print(f"Your total score: {self.player_score}")
        
        return result
    
    def play_round(self):
        """Play one round of Blackjack"""
        self.deal_initial_cards()
        self.clear_screen()
        
        print("🎰 WELCOME TO BLACKJACK! 🎰")
        self.show_hands()
        
        # Check for natural blackjack
        if self.player_hand.value == 21:
            print("\n*** NATURAL BLACKJACK! ***")
            self.show_hands(show_dealer_hidden=False)
            if self.dealer_hand.value == 21:
                print("*** But dealer also has Blackjack! Push! ***")
                return 'push'
            else:
                print("*** YOU WIN WITH BLACKJACK! ***")
                self.player_score += 50
                return 'blackjack'
        
        # Player's turn
        player_result = self.player_turn()
        
        # If player busted, game over
        if player_result == 'bust':
            self.player_score -= 25
            return 'bust'
        
        # Dealer doesn't draw additional cards in this simplified version
        # Dealer's hand is already complete from initial deal
        
        # Determine winner
        return self.determine_winner()
    
    def play_game(self):
        """Main game loop"""
        playing = True
        
        while playing:
            result = self.play_round()
            
            # Ask to play again
            while True:
                play_again = input("\nDo you want to play again? (Y/N): ").lower().strip()
                if play_again in ['y', 'yes']:
                    # Reshuffle if deck is getting low
                    if len(self.deck) < 15:
                        self.deck = Deck()
                        self.deck.shuffle()
                        print("Deck reshuffled!")
                    break
                elif play_again in ['n', 'no']:
                    playing = False
                    break
                else:
                    print("Please enter 'Y' for Yes or 'N' for No.")
        
        print(f"\nThanks for playing! Your final score: {self.player_score}")
        print("Goodbye!")

# Run the game
if __name__ == "__main__":
    game = BlackjackGame()
    game.play_game()