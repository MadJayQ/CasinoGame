import Player as Player
from Card import Card
from random import shuffle
from GameRules import GameRules

class Dealer(Player.Player):
    
    NUM_SUITES = 4
    NUM_CARDS_PER_SUITE = 13

    def __init__(self, x : int, y : int):
        self.x = x
        self.y = y
        self.deck = []
        self.hand = []
        self.InitializeDeck()

    def DealCard(self):
        return self.deck.pop(0)
    def DealSelf(self):
        self.hand.append(self.DealCard())

    def DealCommunityCards(self, numCards : int, game : GameRules):
        for i in range(numCards):
            game.hole_cards.append(self.DealCard())

    def InitializeDeck(self):
        self.deck.clear()
        for i in range(1, self.NUM_SUITES + 1):
            for j in range(1, self.NUM_CARDS_PER_SUITE + 1):
                 card = Card(1, j)
                 self.deck.append(card)
        shuffle(self.deck)




