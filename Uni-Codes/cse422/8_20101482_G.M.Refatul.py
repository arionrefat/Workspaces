import random
import math

studentiD = "20101482".replace("0", "8")

minVal = int(studentiD[4])
revID = studentiD[6:]
totalPointsWin = int(revID[::-1])
maxVal = int(totalPointsWin * 1.5)
numOfShuffles = int(studentiD[3])


def miniMax(node, maximizingPlayer, values, alphaValue, betaValue, depth):
    if depth == 3:
        return values[node]

    if not maximizingPlayer:
        minVal = math.inf
        for i in range(2):
            value = miniMax((node * 2 + i), 1, values, alphaValue, betaValue, depth + 1)
            minVal = min(minVal, value)
            if min(betaValue, minVal) <= alphaValue:
                break
        return minVal

    else:
        maxVal = -math.inf
        for i in range(2):
            value = miniMax((node * 2 + i), 0, values, alphaValue, betaValue, depth + 1)
            maxVal = max(maxVal, value)
            if betaValue <= max(alphaValue, maxVal):
                break
        return maxVal


value = []
for _ in range(8):
    value.append(random.randint(minVal, maxVal))

alphabetaValue = miniMax(0, True, value, -math.inf, math.inf, 0)

print("-------------TASK 1-----------------")
print("Generated 8 random points between the minimum and maximum point limits:", value)
print("Total points to win:", totalPointsWin)
print("Achieved point by applying alpha-beta pruning =", alphabetaValue)
print(
    "The winner is",
    "Optimus Prime" if (totalPointsWin <= alphabetaValue) else "Megatron",
    "\n",
)


listOfVic = []
wonCount = 0
for _ in range(numOfShuffles):
    value2 = []
    for _ in range(8):
        value2.append(random.randint(minVal, maxVal))
    winValue = miniMax(0, True, value2, -math.inf, math.inf, 0)
    listOfVic.append(winValue)
    if totalPointsWin <= winValue:
        wonCount += 1

print("-------------TASK 2-----------------")
print("After the shuffle:\nList of all points values from each shuffle:", listOfVic)
print("The maximum value of all shuffles:", max(listOfVic))
print(f"Won {wonCount} times out of {numOfShuffles} number of shuffles")
