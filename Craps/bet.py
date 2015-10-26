__author__ = 'William'
import random
import math

def droll():
    die1=random.randint(1,6)
    die2=random.randint(1,6)
    totalroll=die1+die2
    print(totalroll)
    return(totalroll)
def money():
    money=int(input("How much money are you starting with?"))
    print(money)
    return money
def betm():
    bet=int(input("What amount would you like to bet."))
    money=money()-bet
    print money
def passlinebet():
    droll()
    if droll()==(7,11):
        money *2
        return money
    elif droll()==(4,5,6,8,9,10):
        point=droll()
        droll()
        while droll()!= point:
            print (droll())
            if droll() ==7 :
                print ("You lost")
                bet=0
                print ("Money on the table is now equal to",bet)
                break
            if droll()==point:
                print ("You win")
                #bet= bet*2
                break
    elif droll()==(2,3,12):
        print("Congrats you lost")
       # bet=0
    return bet
print(passlinebet())

'''
def craps():
    money=int(input("How much money do you have?"))
    bet= int(input("How much would you like to bet?"))
    nmoney=money-bet
'''

'''
def cont():
    userinput= input("Would you like to continue y/n?")
    if userinput=="n":
        print("goodbye")
    else:
        game=("what bet would you like to place")
'''

