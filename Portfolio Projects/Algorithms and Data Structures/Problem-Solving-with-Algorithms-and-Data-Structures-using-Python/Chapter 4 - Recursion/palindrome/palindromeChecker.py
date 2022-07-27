
from random import randrange
from pythonds.basic import Deque

# I will write a couple different approaches to solve the paldindrom problem.
class Palindrome:
    def __init__(self, paldindromeList=None):
        if not paldindromeList:
            self.paldindromeList = ["redivider", "deified", "civic", "radar", "level", "rotor", "kayak", "reviver", "racecar", "madam", "refer"]
        else:
            self.paldindromeList = paldindromeList

    # Approach One - deque
    def paldindromeWithDeck(self, wordToCheck):
        """This function uses the deque(deck) data structure to pop
        both sides of the word until ethier the word has 1 or less chars or
        the chars are not equal. Though it doesn't use recursion, I like
        this solution to the palindrome problem."""
        isPalindrome = True
        deckOne = Deque()
        for ch in wordToCheck:
            deckOne.addRear(ch)

        while (deckOne.size() > 1 and isPalindrome):
            charsAreEqual = deckOne.removeFront() == deckOne.removeRear()
            if not charsAreEqual:
                isPalindrome = False
        stringToRet = "Word: " + wordToCheck + (" is a paldindrome"  if isPalindrome else " is not a paldindrome")
        return stringToRet

    # Approach Two Itteration
    def palindromeWithItteration(self, wordToCheck):
        """This function uses the itterative approach to solve the problem
        again this doesn't use recursion, but is a simple to code method"""
        # Initial state settings
        isPalindrome = True
        firstChar = 0
        lastChar = len(wordToCheck) - 1

        while firstChar < lastChar and isPalindrome:
            if wordToCheck[firstChar] != wordToCheck[lastChar]:
                isPalindrome = False
                continue
            firstChar += 1
            lastChar -= 1

        stringToRet = "Word: " + wordToCheck + (" is a paldindrome"  if isPalindrome else " is not a paldindrome")
        return stringToRet

    # Approach Three Itteration with Recursion
    def paldindromeWithItterationAndRecursion(self, wordToCheck):
        """Using itteration and recusion. It is simular to Appraoch Two, but 
        instead of a while loop, the shrinking indexes are feed back into the method.
        A sub method is required for the recursion to work as the len-1 of the word is 
        needed to start the chain."""
        def paldindromeWithIttAndRecSubFun(wordToCheck, start, end):
            if start >= end:
                return True
            else:
                if wordToCheck[start] == wordToCheck[end]:
                    return paldindromeWithIttAndRecSubFun(wordToCheck, start + 1, end - 1)
                else:
                    return False
        return paldindromeWithIttAndRecSubFun(wordToCheck, 0, len(wordToCheck) - 1)

    # Approach Four Slicing
    def palindromeWithSlicing(self, wordToCheck):
        """Uses recursion to solve the palindrome problem. 
        It does this by slicing the remaining chars and feeding it back into itself.
        Eventualy ethier the word will be 1 or 0 len and thus return true or index 0 and -1 
        won't match and it will return false."""
        # Base case
        if len(wordToCheck) <= 1:
            return True
        else:
            if wordToCheck[0] == wordToCheck[-1]:
                return self.palindromeWithSlicing(wordToCheck[1:-1])
            else:
                return False

pCalc = Palindrome()
# Gen random number to select word from list.
randomNum = randrange(0, len(pCalc.paldindromeList)-1)


# Calculate and print results
print(pCalc.paldindromeWithDeck(pCalc.paldindromeList[randomNum]) + "\ntested with deque\n")
print(pCalc.palindromeWithItteration(pCalc.paldindromeList[randomNum]) + "\ntested with itteration\n")
print("Word: {} is {} paldindrome".format(pCalc.paldindromeList[randomNum], ("a" if pCalc.paldindromeWithItterationAndRecursion(wordToCheck=pCalc.paldindromeList[randomNum]) else "not a")) + "\ntested with itteration and recursion\n")
print("Word: {} is {} paldindrome".format(pCalc.paldindromeList[randomNum], ("a" if pCalc.palindromeWithSlicing(pCalc.paldindromeList[randomNum]) else "not a")) + "\ntested with slicing\n")