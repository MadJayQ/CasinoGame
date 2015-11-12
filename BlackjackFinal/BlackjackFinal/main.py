import Blackjack

def main():
    blackjack = Blackjack.Blackjack()
    blackjack.Initialize() #Initialize Game
    while blackjack.bLooping:
        blackjack.Update()
        blackjack.UpdateCardList()
        blackjack.Render()

if __name__ == "__main__":
    main()
