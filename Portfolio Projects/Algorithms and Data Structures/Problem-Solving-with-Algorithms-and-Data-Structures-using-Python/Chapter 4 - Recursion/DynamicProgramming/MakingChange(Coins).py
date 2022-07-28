# Recurive Solution
# Track how many recursive calls are made for a solution
callCounter = 0

def calcMinCoins(valueList, targetValue):
    # Call tracking
    global callCounter
    callCounter += 1
    # A break in going deeper into recursion after hitting 200m calls.
    if callCounter >= 200000000:
        return 1
    """Approach One calculating every possible solution."""
    minChange = targetValue
    if targetValue in valueList:
        return 1
    else:
        for i in [c for c in valueList if c <= targetValue]:
            coinNum = 1 + calcMinCoins(valueList, targetValue - i)
            if coinNum < minChange:
                minChange = coinNum
    return minChange

def exeMinCoinCacl():
    """You can alter the values and target, but it will take
    an ever, massively, increasing time and memory. It also takes addional time
    to do the recursion in python"""
    coinValueList = [1, 2, 5, 10, 20, 50, 100, 200]
    targetValue = 247
    print(calcMinCoins(coinValueList, targetValue))
    print("It took {} recursive calls to calculate with {} coins and target value {}".format(callCounter, coinValueList, targetValue))
    if callCounter >= 200000000:
        print("Broke before finishing as depth limit exceeded")

#exeMinCoinCacl()
callCounter = 0

def calcMinCoinsRemember(valueList, targetValue, knownPaths):
    global callCounter
    callCounter += 1
    # A break in going deeper into recursion after hitting 200m calls.
    if callCounter >= 200000000:
        return 1
    """Approach Two calculating every possible solution, but saving knowns."""
    minChange = targetValue
    if targetValue in valueList:
        knownPaths[targetValue] = 1
        return 1
    elif knownPaths[targetValue] > 0:
        return knownPaths[targetValue]
    else:
        for i in [c for c in valueList if c <= targetValue]:
            coinNum = 1 + calcMinCoinsRemember(valueList, targetValue - i, knownPaths)
            if coinNum < minChange:
                minChange = coinNum
                knownPaths[targetValue] = minChange

    return minChange

def exeMinCoinRememberCacl():
    """You can alter the values and target, but it will take
    an ever, massively, increasing time and memory. Each path only needs one calculation. 
    Basicly adding caching. Much better than approach one,
    but still very slow and inefficient."""
    coinValueList = [1, 2, 5, 10, 20, 50, 100, 200]
    targetValue = 247
    print(calcMinCoinsRemember(coinValueList, targetValue, [0]*(targetValue+1)))
    print("It took {} recursive calls to calculate with {} coins and target value {}".format(callCounter, coinValueList, targetValue))

#exeMinCoinRememberCacl()
callCounter = 0

def dynamicMinCoin(valueList, targetValue, minCoins):
    #Global Counter increment
    global callCounter
    callCounter += 1
    """Approach Three uses dynamic programming to solve the problem, working out smallest
    and then increasing. However, only returns the number of coins and not what coins"""
    for coins in range(targetValue+1):
        minChange = coins
        for j in [c for c in valueList if c <= coins]:
            callCounter += 1
            if minCoins[coins-j] + 1 < minChange:
                minChange = minCoins[coins-j]+1
        minCoins[coins] = minChange
    return minCoins[targetValue]

def exeDynamicMinCoin():
    """You can alter the values and target, but it will take
    an ever, massively, increasing time and memory. Takes about as many loops
    as approach twos recurssion, but even so it is far faster and more 
    efficient."""
    coinValueList = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000]
    targetValue = 247124
    print(dynamicMinCoin(coinValueList, targetValue, [0]*(targetValue+1)))
    print("It took {} loops to calculate with {} coins and target value {}".format(callCounter, coinValueList, targetValue))

exeDynamicMinCoin()

