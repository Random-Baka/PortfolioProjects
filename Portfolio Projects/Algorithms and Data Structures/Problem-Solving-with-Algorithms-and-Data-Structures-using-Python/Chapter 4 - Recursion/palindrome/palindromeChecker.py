paldindromeList = ["redivider", "deified", "civic", "radar", "level", "rotor", "kayak", "reviver", "racecar", "madam", "refer"]
from random import randrange
# I will write a couple different approaches to solve the paldindrom problem.

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

# Approach Two Itteration
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

# Approach Three Slicing
def palindromeWithSlicing(wordToCheck):
    """Uses recursion to solve the palindrome problem. 
    It does this by slicing the remaining chars and feeding it back into itself.
    Eventualy ethier the word will be 1 or 0 len and thus return true or index 0 and -1 
    won't match and it will return false."""
    # Base case
    if len(wordToCheck) <= 1:
        return True
    else:
        if wordToCheck[0] == wordToCheck[-1]:
            return palindromeWithSlicing(wordToCheck[1:-1])
        else:
            return False

# Gen random number to select word from list.
randomNum = randrange(0, len(paldindromeList)-1)

# Calculate and print results
print(paldindromeWithDeck(paldindromeList[randomNum]) + "\ntested with deque\n")
print(palindromeWithItteration(paldindromeList[randomNum]) + "\ntested with itteration\n")
print("Word: {} is {} paldindrome".format(paldindromeList[randomNum], ("a" if palindromeWithSlicing(paldindromeList[randomNum]) else "not a")) + "\ntested with slicing\n")