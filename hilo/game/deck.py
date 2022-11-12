class Deck:
    """
    Represent a deck of cards
    only the current card that dealer draws in hilo game matters
    """
    
    def __init__(self):
        #represents the dealer's current card in a deck
        self.current_card = 0 

        