from enum import Enum
from Player import Player
import Dealer
from Card import Card

class HandType(Enum):
    ROYAL_FLUSH = 0
    STRAIGHT_FLUSH = 1
    FOUR_OF_A_KIND = 2
    FULL_HOUSE = 3
    FLUSH = 4
    STRAIGHT = 5
    THREE_OF_A_KIND = 6
    TWO_PAIRS = 7
    PAIR = 8
    HIGH_CARD = 9
class HandStatistics(object):
    def __init__(self, hand : list):
        self.handtype = HandType.HIGH_CARD
        self.player_hand = hand
        self.checkAllHandTypes()
    def checkAllHandTypes(self):
        if(self.checkForRoyalFlush()):
            self.handtype = HandType.ROYAL_FLUSH
        elif(self.checkForStraightFlush()):
            self.handtype = HandType.STRAIGHT_FLUSH 
    def determineHighestCard(self):
        highestCard = Card(0, 0)
        for cards in self.player_hand:
            if cards.CARD > highestCard.CARD:
                highestCard = cards
        return highestCard
    def determineHighestCardFromList(self, cards : list):
        highestCard = Card(0, 0)
        for card in cards:
            if card.CARD > highestCard.CARD:
                highestCard = card
        return highestCard
    def containsCard(self, card : Card):
        for cards in self.player_hand:
            if(cards.CARD == card.CARD and cards.SUITE == card.SUITE):
                return True
        return False

    def checkForRoyalFlush(self):
        highestCard = self.determineHighestCard()
        if highestCard.CARD == Card.ACES:
            ace_suit = highestCard.SUITE
            for i in range(Card.ACES, 9, -1):
                card = Card(ace_suit, i)
                if not self.containsCard(card):
                    return False
            return True
        return False
    def checkForStraightFlush(self):
        highestCard = self.determineHighestCard()
        if highestCard.CARD < 6:
            return False
        for i in range(highestCard.CARD, highestCard.CARD - 5, -1):
            card = Card(highestCard.SUITE, i)
            if not self.containsCard(card):
                return False
        return True
     




class GameRules(object):
    def __init__(self):
        self.hole_cards = []
        self.NUM_HOLE_CARDS = 5
        self.HOLE_STARTING_X = 200
        self.HOLE_STARTING_Y = 352
    def ComparePlayers(self, playerOne : Player, playerTwo : Player):
        playerOneStats = HandStatistics(playerOne.hand + self.hole_cards)
        playerTwoStats = HandStatistics(playerOne.hand + self.hole_cards)
        if playerOneStats.handtype.value < playerTwoStats.handtype.value:
            return playerOne
        else:
            return playerTwo


