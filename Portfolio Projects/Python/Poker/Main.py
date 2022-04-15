from CardManager import CardManager

class GameManager():

    def __init__(self) -> None:
        self.cardMan = CardManager()
        self.cardMan.createDeck()
        self.playerHand = self.cardMan.returnNewHand()

    def dealRiver(self, centreDeck, cardAdd=1):
        for x in range(cardAdd):
            centreDeck.append(self.getCardManager().returnTopCard())
        return centreDeck

    def getPlayerHand(self):
        return self.playerHand

    def setPlayerHand(self, newPlayerHand):
        self.playerHand = newPlayerHand
    
    def getCardManager(self):
        return self.cardMan

if __name__ == "__main__":
        #test = cardManager()
        #test.main()
        game = GameManager()
        print(game.getPlayerHand())
        centreCards = []
        centreCards = game.dealRiver(centreCards, 3)
        print(centreCards)
        centreCards = game.dealRiver(centreCards)
        print(centreCards)
        centreCards = game.dealRiver(centreCards)
        print(centreCards)

        newHand = game.getCardManager().replaceCards(game.getPlayerHand(), [1, None, 1, None, 1])
        game.setPlayerHand(newHand)
        print(game.getPlayerHand())
        

