from random import shuffle

class CardManager():
    def __init__(self) -> None:
        self.cardDeck = []
        self.createDeck()
        
    def createDeck(self, numOfDecks=1):
        self.suitNames = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.currentCard = 1
        self.currentSuit = 0
        self.numberOfDecks = numOfDecks
        for x in range(0, 52 * self.numberOfDecks):
            self.cardDeck.append({self.suitNames[self.currentSuit] : self.currentCard})
            self.currentCard += 1
            if self.currentCard == 14:
                self.currentCard = 1
                self.currentSuit += 1
                # Prep for more than one deck
                if self.currentSuit > 3:
                    self.currentSuit = 0
        # Randomise card order
        shuffle(self.cardDeck)

    def returnTopCard(self):
        return self.cardDeck.pop(0)
        
    def returnNewHand(self):
        self.newHand = []
        for x in range(5):
            self.newHand.append(self.returnTopCard())
        return self.newHand

    def replaceCards(self, playersHand, replaceList):
        for x in range(5):
            if replaceList[x] != None:
                playersHand[x] = self.returnTopCard()
        return playersHand
