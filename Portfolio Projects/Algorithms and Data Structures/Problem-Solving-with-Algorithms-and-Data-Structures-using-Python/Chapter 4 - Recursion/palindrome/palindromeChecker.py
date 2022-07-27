paldindromeList = ["redivider", "deified", "civic", "radar", "level", "rotor", "kayak", "reviver", "racecar", "madam", "refer"]

# I will write a couple different approaches to solve
# Approach One - deque
from pythonds.basic import deque

deckOne = deque(paldindromeList[0])
print(deckOne.removeFront())