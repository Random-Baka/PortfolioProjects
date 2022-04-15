from GameManager import GameManager

class PlayGame():

    def __init__(self) -> None:
      self.totalMoneyPool = 1000
      self.stake = 0
        
    def getStake(self):
        return self.stake

    def setStake(self, newStake):
        self.stake = self.getTotalMoney() if newStake > self.getTotalMoney() else newStake
        #self.setTotalMoney((self.getTotalMoney() - self.getStake()))
        self.totalMoneyPool = self.totalMoneyPool - self.stake

    def getTotalMoney(self):
        return self.totalMoneyPool
    
    def setTotalMoney(self, newAmount):
        self.getTotalMoney = newAmount
    
    def playRound(self):
        pass

    def playFullGame():
        pass

if __name__ == "__main__":
        #test = cardManager()
        #test.main()
        playing = PlayGame()
        while playing.getTotalMoney() > 0:
           playing.setStake(int(input()))
        print(playing.getTotalMoney())
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
        

