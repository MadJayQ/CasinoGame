import Card

class Player(object):
    """description of class"""
    
    def __init__(self):
        self.hand = []
        self.hand_value = 0
    def DealCard(self, card : Card.Card):
        self.hand.append(card)
        if self.hand_value + card.VALUE > 21:
            self.CheckAces()
        self.RecalculateSum()
    def Busted(self):
        return self.hand_value > 21
    def HasBlackJack(self):
        return self.hand_value == 21
    def CheckAces(self):
        for cards in self.hand:
            if cards.VALUE == 11:
                cards.VALUE = 1
                self.RecalculateSum()
                return self.hand_value > 21
    def RecalculateSum(self):
        self.hand_value = 0
        for cards in self.hand:
            self.hand_value += cards.VALUE
    def GetHandSize(self):
        return len(self.hand)
    def GetLastCard(self):
        return self.hand[len(self.hand) - 1]



