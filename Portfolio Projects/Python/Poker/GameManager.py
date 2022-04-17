from CardManager import CardManager

class GameManager():

    def __init__(self) -> None:
        self.cardMan = CardManager()
        self.cardMan.createDeck()
        self.playerHand = self.cardMan.returnNewHand()

    def dealCentre(self, centreDeck, cardAdd=1):
        for x in range(cardAdd):
            centreDeck.append(self.getCardManager().returnTopCard())
        return centreDeck

    def getPlayerHand(self):
        return self.playerHand

    def setPlayerHand(self, newPlayerHand):
        self.playerHand = newPlayerHand
    
    def getCardManager(self):
        return self.cardMan

    def calculateIfWin(self, finalHand, finalCentre, stake):
        print("I don't know, have your stake back")

        winningOdds = 1
        return self.calculateIfWin(stake, winningOdds)

    def calculateWinnings(self, stake, winningOdds):
        return stake * winningOdds