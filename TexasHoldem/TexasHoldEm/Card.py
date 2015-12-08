from tkinter import *


class Card(object):
    """Definition of the Card Class"""
    VALUE = 0
    SUITE = 0
    CARD = 0

    CLUBS = 1
    SPADES = 2
    HEARTS = 3
    DIAMONDS = 4
    ACES = 14
    JACKS = 11
    QUEENS = 12
    KINGS = 13

    IMAGE_WIDTH = 72
    IMAGE_HEIGHT = 97

    Visible = True

    def __init__(self, suite, card):
        self.SUITE = suite
        self.CARD = card
        if (self.CARD == 1):
            self.CARD = 14
    def SubImage(self, src, l, t, r, b):
        dst = PhotoImage()
        dst.tk.call(dst, 'copy', src, '-from', l, t, r, b, '-to', 0, 0)
        return dst
    def GrabCard(self, src):
        temp_card = self.CARD
        temp_suite = self.SUITE
        if temp_suite < 1:
            return
        if temp_card < 1:
            return
        if temp_card == 14:
            temp_card =1
        yOffset = 2
        if temp_suite == self.DIAMONDS:
            yOffset = 3
        elif temp_suite == self.CLUBS or temp_suite == self.SPADES:
            yOffset = 0
        return self.SubImage(src, ((temp_card - 1) * self.IMAGE_WIDTH) + temp_card,
        ((temp_suite - 1) * self.IMAGE_HEIGHT) + temp_suite, ((temp_card) * self.IMAGE_WIDTH) + (temp_card - 1), ((temp_suite) * self.IMAGE_HEIGHT) 
        + yOffset)


