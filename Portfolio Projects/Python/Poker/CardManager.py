from random import shuffle

class cardManager():
    def __init__(self) -> None:
        self.cardDeck = []
        print("test")
        self.createDeck()

    def main(self):
        print("Test")
        print(self.cardDeck)
        
    def createDeck(self, numOfDecks=1):
        suitNames = ["Hearts", "Diamonds", "Clubs", "Spades"]
        currentCard = 1
        currentSuit = 0
        numberOfDecks = numOfDecks
        for x in range(0, 52 * numberOfDecks):
            self.cardDeck.append({suitNames[currentSuit] : currentCard})
            currentCard += 1
            if currentCard == 14:
                currentCard = 1
                currentSuit += 1
                # Prep for more than one deck
                if currentSuit > 3:
                    currentSuit = 0
        # Randomise card order
        shuffle(self.cardDeck)

    def returnTopCard(self):
        return self.cardDeck.pop(0)
        
    def returnNewHand(self):
        newHand = []
        for x in range(5):
            newHand.append(self.returnTopCard())
        return newHand