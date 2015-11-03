__author__ = 'William'
import random
moneys= 0
bet=0
froll=False
roll=0
def money():
    global moneys
    moneys=int(input("How much money are you starting with?"))
    print("Your overall balnce is",moneys)
    return moneys

def betm():

        global bet
        bet=int(input("What amount would you like to bet."))
        global moneys
        moneys = moneys -bet
        print ("Your overall blance is now",moneys)
        print ("Your bet is", bet)
        return bet

def droll():
    global roll
    die1=random.randint(1,6)
    die2=random.randint(1,6)
    totalroll=die1+die2
    roll= totalroll
    print(totalroll)
    return(totalroll)

def passlinebet():
        global bet
        global moneys
        global roll
        if roll==(7,11):
            bet = bet*2
            cont=input("You Won\nWould you like to continue or not? Y/N")
            cont.upper()
            if cont=="Y":
                print("Coming Soon")
            else:
                moneys = moneys + bet
                bet=0
                print ("Total money now equals ", moneys)
            return bet
        elif roll==(4,5,6,8,9,10):
            point=roll
            roll=droll()
            while roll != point:
                print ("YOu rolled a",roll)
                if roll ==7 :
                    print ("You lost")
                    bet=0
                    print ("Money on the table is now equal to",bet)
                    break
                if roll==point:
                    print ("You win")
                    bet= bet*2
                    break
        elif roll==(2,3,12):
            print("Congrats you lost")
            bet=0
            return bet
def craps():
    money()
    betm()
    droll()
    passlinebet()

craps()