from game.deck import Deck
import random

class Dealer:
    def __init__(self):
        self.deck = Deck()
        self.current_card = self.deck.current_card
    
    
    #function used to shuffle the deck at the beginning of the game
    #also used to get the next number on the deck then reshuffling(random)                
    def shuffle_deck(self):
        current_card = self.current_card
        while current_card == self.current_card:
            self.current_card = random.randint(1,13)
    
    #function used to return the next card after player guess it
    #also used in determining score of player 
    def next_card(self):
        self.shuffle_deck()
        return self.current_card
        
    
    
    
    
                

            
        