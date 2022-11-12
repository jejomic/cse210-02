from game.dealer import Dealer
from game.player import Player


class Game__operation:
    def __init__(self):
        self.dealer = Dealer()
        self.players = []

    
    #function to register players
    def player_registration(self):
        player_count = 0
        while (player_count < 1 or player_count > 4):
            try:
                user_input = int(
                    input("Enter number of players (min: 1, max: 4): "))
            except ValueError:
                print("Please enter a number")
            else:
                player_count = user_input
                break

        for i in range(player_count):
            player = Player()
            self.players.append(player)

        counter = 0
        for player in self.players:
            player.set_name(input(f"Enter player {counter + 1} name: "))
            counter = counter + 1
        counter = 0

    #check if player is still playing
    def players_playing(self):
        player_count = 0
        for player in self.players:
            if player.is_playing == True:
                player_count = player_count+1
        return player_count

    #returns player guess
    def get_player_guess(self):
        input_invalid = True
        global player_guess
        while (input_invalid):
            player_answer = input("Higher or lower? [h/l] ")
            if (player_answer == 'h' or player_answer == 'l'):
                player_guess = player_answer
                input_invalid = False

        return player_guess

    #prompts player if they still want to play
    def prompt_to_continue(self, Player):
        input_invalid = True
        global player_continue
        while (input_invalid):
            player_input = input(f"\nContinue playing {Player.name}? y/n ")
            if player_input == 'y':
                player_continue = True
            if player_input == 'n':
                player_continue = False
            if player_input == 'y' or player_input == 'n':
                input_invalid = False

        return player_continue

    #updates player scores, reshuffle the deck, returns the next card
    def scores(self, answers):
        scores = []
        current_card = int(self.dealer.current_card)
        next_card = int(self.dealer.next_card())
        for i in answers:
      
            if next_card > current_card and i == 'h':
             
                scores.append(100)
            elif next_card < current_card and i == 'l':
              
                scores.append(100)
            else:
                
                scores.append(-75)
        return scores

    #function to start the game
    def game_start(self):
        self.player_registration() #players registration
        player_count = self.players_playing() #ensures that a player is playing
        self.dealer.shuffle_deck() #shuffles the deck first
        while player_count: #ensures that a player is playing
            
            """
            next lines could be functions
            """
            
            #presents the current card to the players
            print(f"\nThe card is {self.dealer.current_card}") 
            
            #get player guess
            players_answers = []
            for player in self.players:
                print(f"{player.name}'s turn")
                players_answers.append(self.get_player_guess())
            
            #calculate score, compare current card to the next card
            scores = self.scores(players_answers)
            print(f"\nNext card is {self.dealer.current_card}")
            
            #prints scoreboard
            for player, score in zip(self.players, scores):
                player.score = player.score + score
                print(f"{player.name}'s score is {player.score}")
                
            #remove players with 0 scores
            for player in self.players:
                if player.score < 0:
                    print(f"{player.name} has not enough score to continue, Goodbye!")
                    self.players.remove(player)    

            #prompt each player if they want to play
            for player in self.players:
                player.is_playing = self.prompt_to_continue(player)
                
                #removes quitters from the game
                if player.is_playing == False:
                    print(f"{player.name} has left the game")
                    self.players.remove(player)
            
            #update the game about players still willing to play
            #game over if no players left      
            player_count = self.players_playing()
            if player_count < 1:
                print("Game Over! No players left.")
            
