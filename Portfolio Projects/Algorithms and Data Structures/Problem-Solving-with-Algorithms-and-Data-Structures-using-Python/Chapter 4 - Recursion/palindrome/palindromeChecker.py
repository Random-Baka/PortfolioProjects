paldindromeList = ["redivider", "deified", "civic", "radar", "level", "rotor", "kayak", "reviver", "racecar", "madam", "refer"]

# I will write a couple different approaches to solve
# Approach One - deque
from pythonds.basic import Deque

def paldindromeWithDeck(wordToCheck=paldindromeList[0]):
    """This function uses the deque(deck) data structure to pop
    both sides of the word until ethier the word has 1 or less chars or
    the chars are not equal. Though it doesn't use recursion, I like
    this solution to the palindrome problem."""
    isPalindrome = True
    deckOne = Deque()
    for ch in paldindromeList[0]:
        deckOne.addRear(ch)

    while (deckOne.size() > 1 and isPalindrome):
        charsAreEqual = deckOne.removeFront() == deckOne.removeRear()
        if not charsAreEqual:
            isPalindrome = False
    stringToRet = "Word: " + wordToCheck + (" is a paldindrome"  if isPalindrome else " is not a paldindrome")
    return stringToRet

def palindromeWithSlicing():
    # Base case
    print("1")

def palindromeWithItteration(wordToCheck=paldindromeList[0]):
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
