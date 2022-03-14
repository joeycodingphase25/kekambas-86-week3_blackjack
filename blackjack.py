
import random
from re import L
import os
class Deck:

    def __init__(self, number_of_decks): #maybe another variable?
        self.deck_of_cards = []
        self.number_of_decks = number_of_decks
        self.build_deck()
        pass
    
    def build_deck(self):
        weight = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king']*self.number_of_decks
        types = ['spades', 'diamonds', 'hearts', 'clubs']
        for x in types:
            for y in weight:
                self.deck_of_cards.append(Card(y,x))
        self.shuffle_deck()

    def print_deck(self):
        for card in self.deck_of_cards:
            print(card)
        

    def shuffle_deck(self):
        random.shuffle(self.deck_of_cards)
        pass

class Card:
    # card class will be defined by WEIGHT and TYPE
    def __init__(self, card, suit): #maybe another variable?
        self.card = card
        self.suit = suit
        self.hidden = False
        if self.card in ['jack', 'queen', 'king']:
            self.weight = 10
        elif self.card == 'ace':
            self.weight = 11
        else: 
            self.weight = int(card)

    def __str__(self):
        return f"{self.card} of {self.suit.title()}"
    


class Player:
    # User will be able to HIT or PASS
    def __init__(self, name): #maybe another variable?
        self.hand = []
        self.name = name
    
    def hit(self, deck):
        self.hand.append(deck.deck_of_cards.pop())

    def print_hand(self):
        new_list = []
        for card in self.hand:
            if card.hidden != True:
                new_list.append(f"{card.card} of {card.suit.title()}")
            else:
                new_list.append("Face Down")
        return new_list
    
    def current_weight(self): 
        self.total = 0
        for card in self.hand: 
            if card.weight == 11 and self.total >= 11:
                card.weight = 1
            self.total += int(card.weight)
        return self.total

    def game_state(self):

        if self.current_weight() == 21:
            print(f"Congrats {self.name}, you have BlackJack!")
            return False
        if self.current_weight() > 21:
            print(f"Sorry {self.name}, you have Busted!")
            return False
        
class Dealer(Player):
    # Dealer will HIT or PASS but only if logic variables are satisfied ACCORDING TO RULES
    # def __init__(self): #maybe another variable?
    #     self.hand = []
    def deal(self, deck, players):
        for player in players:
            player.hand.append(deck.deck_of_cards.pop())    
        for player in players:  # Simulate Real Deal * 1 at a time
            player.hand.append(deck.deck_of_cards.pop())
         # FIX THIS
        self.hand[0].hidden = True   
        for player in players:
            player.game_state()
        
    def hit(self, deck):
        while self.current_weight() < 17:  # Make diff current weight for dealer
            self.hand.append(deck.deck_of_cards.pop())

def board_state(dealer, name):
    os.system('cls')
    print(f"""
Dealers hand:{dealer.print_hand()}  
-------------------------
Your Hand:   {name.print_hand()} --> {name.current_weight()}/21 Possible""")
    
def main(): # Put ace fix in CURRENT WEIGHT FUNCTION / could introduce another ACE
    while True:
        answer = input("Welcome TO BlackJack. Play ('1'), Quit ('2') --> ")
        if answer == '1':
            
            # name = input("Welcome to High-Stake BlackJack, What is Your Name? --> ")
            name = 'jo'
            name = Player(name)
            # decks = input("how many decks would you like to play with --> ")
            decks = 1
            deck = Deck(int(decks))
            dealer = Dealer('Mike The Dealer')
            list_of_players = [dealer, name]
            dealer.deal(deck, list_of_players)
                
            while True:
                board_state(dealer, name)
                choice = input("What Would you Like to do? Hit ('1') or Stand ('2')? --> ")
                if choice == '1':
                    name.hit(deck)
                    # name.game_state()
                    if name.game_state() == False:
                        break                
                if choice == '2':
                    dealer.hit(deck)
                    dealer.hand[0].hidden = False
                    board_state(dealer, name)
                    if dealer.game_state() == False:
                        print(f'Congratulations {name.name}, You Won!')
                        break
                    if dealer.current_weight() == name.current_weight():
                        print("Game Has Tied, No winners")
                        break
                    elif dealer.current_weight() > name.current_weight():
                        print(f"Dealer has Won with {dealer.current_weight()} points") 
                        break
                    else:
                        print(f'Congratulations {name.name}, You Won!') 
                        break
        if answer == '2':
            break

main()

























# deck1 = Deck(1)
# deck1.build_deck()
# deck1.shuffle_deck()
# dealer = Dealer()
# dealer.init_deal(deck1, list_of_players)
# print(dealer.print_hand())
# dealer.hit(deck1)
# print(dealer.print_hand())
# print(dealer.current_weight())
# #     pass