from random import shuffle
import Player
import Card

class Dealer(Player.Player):
    """description of class"""

    NUM_SUITES = 4
    NUM_CARDS = 13
    hand = []
    hand_value = 0

    def __init__(self):
        global deck
        deck = []
        self.ShuffleDeck()

    def DealNextCard(self, player: Player.Player):
        if len(deck) - 1 <= 0:
            self.ShuffleDeck()
        player.DealCard(card = deck[0])
        deck.remove(deck[0])

    def DealSelf(self):
       if len(deck) - 1 <= 0:
           self.ShuffleDeck()
       self.DealCard(card = deck[0])
       deck.remove(deck[0])

    def DealPlayerInitialHand(self, player: Player.Player):
        self.DealNextCard(player = player)
        self.DealNextCard(player = player)

    def ShuffleDeck(self):
        deck.clear()
        for i in range (1, self.NUM_SUITES + 1):
            for j in range(1, self.NUM_CARDS + 1):
                card = Card.Card(i, j)
                deck.append(card)
        shuffle(deck)