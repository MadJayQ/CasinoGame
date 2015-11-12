from tkinter import *


class Card(object):
    """description of class"""
    VALUE = 0
    SUITE = 0
    CARD = 0

    CLUBS = 1
    SPADES = 2
    HEARTS = 3
    DIAMONDS = 4
    ACES = 1
    JACKS = 11
    QUEENS = 12
    KINGS = 13

    IMAGE_WIDTH = 72
    IMAGE_HEIGHT = 97

    Visible = True

    def __init__(self, suite, card):
        self.SUITE = suite
        self.CARD = card
        if(card >= 10):
            self.VALUE = 10
        elif(card == 1):
            self.VALUE = 11
        else:
            self.VALUE = card
    def SubImage(self, src, l, t, r, b):
        dst = PhotoImage()
        dst.tk.call(dst, 'copy', src, '-from', l, t, r, b, '-to', 0, 0)
        return dst
    def GrabCard(self, src):
        if self.SUITE < 1:
            return
        if self.CARD < 1:
            return
        yOffset = 2
        if self.SUITE == self.DIAMONDS:
            yOffset = 3
        elif self.SUITE == self.CLUBS or self.SUITE == self.SPADES:
            yOffset = 0
        return self.SubImage(src, ((self.CARD - 1) * self.IMAGE_WIDTH) + self.CARD,
        ((self.SUITE - 1) * self.IMAGE_HEIGHT) + self.SUITE, ((self.CARD) * self.IMAGE_WIDTH) + (self.CARD - 1), ((self.SUITE) * self.IMAGE_HEIGHT) 
        + yOffset)


