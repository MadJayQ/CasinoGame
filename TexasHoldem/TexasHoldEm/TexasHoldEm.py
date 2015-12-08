import graphics
import Card
import math
from Player import Player
from Dealer import Dealer
from GameRules import GameRules
from tkinter import *


class TexasHoldEm(object):

    def __init__(self, Player: Player, Dealer: Dealer, GameRules: GameRules):
        Player.hand.append(Dealer.DealCard())
        Player.hand.append(Dealer.DealCard())
        Dealer.DealSelf()
        Dealer.DealSelf()
        Dealer.DealCommunityCards(numCards = GameRules.NUM_HOLE_CARDS, game = GameRules)
    def update(self):
        pass


class Game(object):

    def __init__(self, Player: Player, Dealer: Dealer, GameRules: GameRules):
        self.WINDOW_WIDTH = 700
        self.WINDOW_HEIGHT = 700
        self.cardsheet = graphics.GraphicsImage(fileName = "cards.png")
        self.background = graphics.GraphicsImage(fileName = "background.png", x = (self.WINDOW_WIDTH / 2), y = (self.WINDOW_HEIGHT / 2))
        self.card_back = graphics.GraphicsImage(fileName = "back.png", x = 636, y = 352)
        self.ObjectsOnScreen = []
        self.win = graphics.GraphicsWindow(width = self.WINDOW_WIDTH, height = self.WINDOW_HEIGHT)
        self.canvas = self.win.canvas()
        self.poker = TexasHoldEm(Player, Dealer, GameRules)
        self.player = Player
        self.dealer = Dealer
        self.gamerules = GameRules
        self.bCheckStats = True #Temporary

    def drawPlayers(self):
        self.ObjectsOnScreen.clear() #Resource Management
        self.ObjectsOnScreen.append(self.card_back)
        for i in range(len(self.player.hand)):
            if isinstance(self.player.hand[i], Card.Card):
                img = graphics.GraphicsImage(x = self.player.x + (72 / 2 * i), y = self.player.y)
                img.image = self.player.hand[i].GrabCard(self.cardsheet.image)
                self.ObjectsOnScreen.append(img)
        for i in range(len(self.dealer.hand)):
            if isinstance(self.dealer.hand[i], Card.Card):
                img = graphics.GraphicsImage(x = self.dealer.x + (72 / 2 * i), y = self.dealer.y)
                img.image = self.dealer.hand[i].GrabCard(self.cardsheet.image)
                self.ObjectsOnScreen.append(img)
        for i in range(len(self.gamerules.hole_cards)):
            if isinstance(self.gamerules.hole_cards[i], Card.Card):
                img = graphics.GraphicsImage(x = self.gamerules.HOLE_STARTING_X + (80 * i), y = self.gamerules.HOLE_STARTING_Y)
                img.image = self.gamerules.hole_cards[i].GrabCard(self.cardsheet.image)
                self.ObjectsOnScreen.append(img)
        if(self.bCheckStats == True):
            if isinstance(self.gamerules.ComparePlayers(playerOne = self.player, playerTwo = self.dealer), Dealer):
                print("DEALER WINS!")
            else:
                print("PLAYER WINS")
            self.bCheckStats = False

    def update(self):
        self.poker.update()
        self.drawPlayers()
        self.render()

    def render(self):
        self.canvas._tkcanvas.delete("all") #graphics.py clear function is not good 
        self.canvas._tkcanvas.create_image(self.background.xCoord, self.background.yCoord, image = self.background.image)
        for object in self.ObjectsOnScreen:
            if isinstance(object, graphics.GraphicsImage): #If the object in the list is an image, we want to draw it..otherwise we DEFINITELY don't want to try to draw it
                self.canvas._tkcanvas.create_image(object.xCoord, object.yCoord, image = object.image)
        


    def startUpdateLoop(self):
        while not self.win.isClosed():
            self.update()
            self.win._tkwin.update()

if __name__ == "__main__":
    playerOne = Player(350, 621)
    dealer = Dealer(350, 67)
    gamerules = GameRules()
    game = Game(playerOne, dealer, gamerules)
    game.startUpdateLoop()