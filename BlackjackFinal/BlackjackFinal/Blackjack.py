from tkinter import *
from tkinter import messagebox

from functools import partial
import sys

import Player
import Dealer


class Blackjack(object):
    """ This class controls how the game's logic should flow"""

    window = Tk()

    WINDOW_WIDTH = 700
    WINDOW_HEIGHT = 700

    bWaitingForRound = True
    bWaitingForNextRound = False
    bDealerPlaying = False
    bLooping = True
    money = 5000
    MINIMUM_BET = 20
    MAXIMUM_BET = 400
    USER_BET = 0
    PlayerOne = Player.Player()
    DealerPlayer = Dealer.Dealer()

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you really want to quit?" ):
            self.window.destroy()
    def CreateWindow(self):
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.window.resizable(width = False, height = False)
        self.window.minsize(width = self.WINDOW_WIDTH, height = self.WINDOW_HEIGHT)
        self.window.title("BlackJack")
        return True
    def WaitForNextRound(self):
        DealButton.place(x = 150, y = 650)
        DealButton.place(x = 150, y = 650)
        BetFive.place(x = 450, y = 670)
        BetTen.place(x = 470, y = 670)
        BetFifty.place(x = 495, y = 670)
        BetHundred.place(x = 520, y = 670)
        ResetBet.place(x = 550, y = 670)
        StayButton.place_forget()
    def UpdateCardList(self):
        PlayerOneRenderList.clear()
        for cards in self.PlayerOne.hand:
            PlayerOneRenderList.append(cards.GrabCard(CARD_SHEET))
        DealerRenderList.clear()
        for cards in self.DealerPlayer.hand:
            if(cards.Visible):
                DealerRenderList.append(cards.GrabCard(CARD_SHEET))
            else:
                DealerRenderList.append(CARD_BACK)
    def EndRound(self):
        if self.DealerPlayer.HasBlackJack():
            self.DealerWin()
        elif self.PlayerOne.HasBlackJack():
            self.PlayerWin()
        elif self.DealerPlayer.Busted() and not self.PlayerOne.Busted():
            self.PlayerWin()
        elif self.PlayerOne.Busted():
            self.DealerWin()
        elif self.DealerPlayer.hand_value == self.PlayerOne.hand_value:
            self.DealerWin()
        elif self.DealerPlayer.hand_value < self.PlayerOne.hand_value:
            self.PlayerWin()
        else:
            self.DealerWin()
        self.bDealerPlaying = False
    def PlayerWin(self):
        self.money += self.USER_BET
        messagebox.showinfo("WIN", "Player Win!\nPlayer: %d\nDealer: %d" % (self.PlayerOne.hand_value, self.DealerPlayer.hand_value))
    def DealerWin(self):
        self.money = self.money - self.USER_BET
        messagebox.showerror("LOSS", "Dealer Win!\nPlayer: %d\nDealer: %d" % (self.PlayerOne.hand_value, self.DealerPlayer.hand_value))
    def Update(self):
        if self.money <= 0:
            self.money == 0
            messagebox.showerror("Loss", "Game Over")
        if self.bDealerPlaying:
            self.DealerPlayer.hand[0].Visible = True
            if self.DealerPlayer.hand_value < 17:
                self.DealerPlayer.DealSelf()
            else:
                self.EndRound()
        if self.bWaitingForRound:
            DealButton.place(x = 150, y = 650)
            BetFive.place(x = 450, y = 670)
            BetTen.place(x = 470, y = 670)
            BetFifty.place(x = 495, y = 670)
            BetHundred.place(x = 520, y = 670)
            ResetBet.place(x = 550, y = 670)
            HitButton.place_forget()
            StayButton.place_forget()
            return
        if self.bWaitingForNextRound:
            self.WaitForNextRound()
            return
        DealButton.place_forget()
        HitButton.place(x = 150, y = 650)
        StayButton.place(x = 200, y = 650)
    def Render(self):
        self.Clear()
        canvas.create_image(self.WINDOW_WIDTH / 2, self.WINDOW_HEIGHT / 2, image = BACKGROUND)
        canvas.create_image(636, 352, image = CARD_BACK)
        for i in range(0, len(PlayerOneRenderList)):
            canvas.create_image(350 + (72/ 2 * i), 621, image = PlayerOneRenderList[i])
        for i in range(0, len(DealerRenderList)):
            canvas.create_image(350 + (72 / 2 * i), 66, image = DealerRenderList[i])
        self.window.title("Blackjack Bet $%d Balance $%d" % (self.USER_BET , self.money))
        self.window.update()
    def HitPressed(self):
        if self.PlayerOne.Busted():
            return
        self.DealerPlayer.DealNextCard(player = self.PlayerOne)
    def Clear(self):
        canvas.delete("all")
    def StayPressed(self):
        self.bDealerPlaying = True
        self.bWaitingForNextRound = True
    def DealPressed(self):
        self.PlayerOne.hand.clear()
        self.DealerPlayer.hand.clear()
        if(self.USER_BET < self.MINIMUM_BET):
            self.USER_BET = self.MINIMUM_BET
        BetFive.place_forget()
        BetTen.place_forget()
        BetFifty.place_forget()
        BetHundred.place_forget()
        ResetBet.place_forget()
        self.DealerPlayer.DealPlayerInitialHand(player = self.PlayerOne)
        self.DealerPlayer.DealSelf()
        self.DealerPlayer.hand[0].Visible = False
        self.DealerPlayer.DealSelf()
        self.bWaitingForRound = False
        self.bWaitingForNextRound = False
    def Bet(self, amount = 20):
        if(self.USER_BET < self.MAXIMUM_BET):
            self.USER_BET += amount
    def ResetBet(self):
        self.USER_BET = 0

    def Initialize(self):
        global CARD_BACK 
        global CARD_SHEET
        global BACKGROUND
        global canvas
        global PlayerOne
        global PlayerTwo
        global DealButton
        global HitButton
        global StayButton
        global ResetButton
        global BetFive
        global BetTen
        global BetFifty
        global BetHundred
        global ResetBet
        global PlayerOneRenderList
        global DealerRenderList
        PlayerOneRenderList = []
        DealerRenderList = []
        canvas = Canvas(self.window, width = self.WINDOW_WIDTH, height = self.WINDOW_HEIGHT)
        CARD_BACK = PhotoImage(file="back.png")
        CARD_SHEET = PhotoImage(file="cards.png")
        BACKGROUND = PhotoImage(file="background.png")

        HitButton = Button(self.window, text = "Hit", command = self.HitPressed)
        StayButton = Button(self.window, text = "Stay", command = self.StayPressed)
        DealButton = Button(self.window, text = "Deal", command = self.DealPressed)
        BetFive = Button(self.window, text = "5", command = partial(self.Bet, 5))
        BetTen = Button(self.window, text = "10", command = partial(self.Bet, 10))
        BetFifty = Button(self.window, text = "50", command = partial(self.Bet, 50))
        BetHundred = Button(self.window, text = "100", command = partial(self.Bet, 100))
        ResetBet = Button(self.window, text = "Reset Bet", command = self.ResetBet)

        if(not(self.CreateWindow())):
            return False
        canvas.create_image(self.WINDOW_WIDTH / 2, self.WINDOW_HEIGHT / 2, image = BACKGROUND)
        canvas.pack()
        return True


