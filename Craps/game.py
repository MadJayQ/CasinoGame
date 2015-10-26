__author__ = 'William'
#from bet import passlinebet
import random

class Moneys:
    def money(self):
         money=int(input("How much money are you starting with?"))
         print(money)
         return money
    def betm(money):
        money = Moneys.money()
        bet=int(input("What amount would you like to bet."))
        money = money -bet
        print (money)
        print ("Your bet is", bet)
        return bet
class Die:
    def droll(self):
        die1=random.randint(1,6)
        die2=random.randint(1,6)
        totalroll=die1+die2
        print(totalroll)
        return(totalroll)

class Bets:
    def passlinebet(bet,money):
        Die.droll()
        if Die.droll()==(7,11):
            print("You Won")
            bet = bet*2
            money = money + bet
            print ("To tal money now equals ", money)
            return bet
        elif Die.droll()==(4,5,6,8,9,10):
            point=Die.droll()
            Die.droll()
            while Die.droll()!= point:
                print (Die.droll())
                if Die.droll() ==7 :
                    print ("You lost")
                    bet=0
                    print ("Money on the table is now equal to",bet)
                    break
                if Die.droll()==point:
                    print ("You win")
                    bet= bet*2
                    break
        elif Die.droll()==(2,3,12):
            print("Congrats you lost")
            bet=0
            return bet
def craps():
    '''
    money=int(input("How much money do you have?"))
    bet= int(input("How much would you like to bet?"))
    nmoney=money-bet
    if nmoney>=0:
        print("This is the amount left after you have place your bet: ", nmoney)
    else:
        while nmoney < 0:
            print("You don't hve the funds to make this bet. \nPlease enter in a bet that does not exceed current avilible funds.")
            bet= int(input("How much would you like to bet?"))
            nmoney=money-bet
            print("This is the amount left after you have place your bet: ", nmoney)
    '''
    cbet=input("What bet would you like to place?\nEnter in:\n1.Pass Line bet\n2.Don't Pass Bet\n3.Field Bet\n4.Come bet\n5.Place Bets\n6.Proposition Bets\n7.Free odd on pass Line Bets\n8.Free odds on come bet\n9.Dont Come Bet\n10.Hardways\n  ")
    print("You chose", cbet)
    #if cbet==1:
    Bets.passlinebet(Moneys.betm(),Moneys.money())
Moneys.money(12)
Moneys.betm(Moneys.money(12))
craps()