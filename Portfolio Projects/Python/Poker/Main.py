from GameManager import GameManager

class PlayGame():

    def __init__(self) -> None:
      self.totalMoneyPool = 1000
      self.stake = 0
      self.gamemanager = GameManager()
        
    def getStake(self):
        return self.stake

    def setStake(self, newStake):
        self.stake = self.getTotalMoney() if newStake > self.getTotalMoney() else newStake
        #self.setTotalMoney((self.getTotalMoney() - self.getStake()))
        self.totalMoneyPool = self.totalMoneyPool - self.stake

    def getGameManager(self):
        return self.gamemanager

    def getTotalMoney(self):
        return self.totalMoneyPool
    
    def setTotalMoney(self, newAmount):
        self.getTotalMoney = newAmount
    
    def playRound(self):
        pass

    def playFullGame():
        pass

    def isAStraight(self, playerHand, centreHand):
        tempList = [1, 2, 3, 4, 5, 6]
        #playerHand + centreHand
        #checkDict = dict(zip(2,3,4,5,6,7,8,9,10,11,12,13)) 

        for x in range(0, len(tempList) - 4):
            # issue here!
            if(tempList[x] - tempList[x + len(tempList) - 1] == 4):
                pass

if __name__ == "__main__":
    #test = cardManager()
    #test.main()
    playing = PlayGame()
    while playing.getTotalMoney() > 0:
        playing.setStake(int(input()))
        print(playing.getTotalMoney())
        #game = GameManager()
        print(playing.getGameManager().getPlayerHand())
        centreCards = []
        centreCards = playing.getGameManager().dealCentre(centreCards, 3)
        

        playing.isAStraight(centreCards, [])

        #newHand = game.getCardManager().replaceCards(game.getPlayerHand(), [1, None, 1, None, 1])
        #game.setPlayerHand(newHand)
        #print(game.getPlayerHand())
        break

