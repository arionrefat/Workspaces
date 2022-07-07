import random
from collections import namedtuple

population = [[]]

def generatePop(size, pop_size):
    return [random.choices([0, 1], k=pop_size) for _ in range(size)]

def fitness(pop, data, limit):
    run = 0
    for i, match in enumerate(data):
        if pop[i] == 1:
            run += match.run
            if run > limit:
                return 0
    return run


def select(popu, input,targetScore):
    index = random.randint(0, len(popu) -1)
    while 0:
        fit = fitness(popu[index], input, targetScore)
        if fit != 0:
            break
    return popu[index]


def crossover(p1, p2,playertotal):
    index = random.randint(0, playertotal - 1)
    return p2[:index] + p1[index:]


def mutate(child, playertotal):
    index = random.randint(0, playertotal - 1)
    if child[index] == 0:
        child[index] = 1
    else:
        child[index] = 0
    return child


def geneticAlgoFunc(popu, inputs, target, playerTotal, mutation_threshold=0.4):
    for _ in range(1000):
        for _ in range(len(popu)):
            chrm1 = select(popu, inputs,target)
            chrm2 = select(popu, inputs,target)
            child = crossover(chrm1, chrm2, playerTotal)

            if random.random() < mutation_threshold:
                child = mutate(child,playerTotal)

            fit1 = fitness(child, inputs, target)
            if fit1 == target:
                return child
    return -1



playerScore = namedtuple("match", ["player", "run"])

input1 = [
    playerScore("Tamim", 68),
    playerScore("Shoumyo", 25),
    playerScore("Shakib", 70),
    playerScore("Afif", 53),
    playerScore("Mushfiq", 71),
    playerScore("Liton", 55),
    playerScore("Mahmudullah", 66),
    playerScore("Shanto", 29),
]

input2 = [
    playerScore("Bradman", 120),
    playerScore("Tendulkar", 90),
    playerScore("Sangakkara", 70),
    playerScore("Kallis", 65),
    playerScore("Lara", 80),
]

input3 = [
    playerScore("Ralph", 80),
    playerScore("John", 70),
    playerScore("Tom", 40),
    playerScore("Young", 50),
]

def printHighestFitness(playaList, playertotal, targetScore):
    population = generatePop(12, playertotal)
    print(population)
    fitArray = geneticAlgoFunc(population, playaList, targetScore,playertotal)
    players = []
    for _, match in enumerate(playaList):
        players.append(match.player)
    print(players)
    print(fitArray)

printHighestFitness(input1,8,330)
printHighestFitness(input2,5,240)
printHighestFitness(input3,4,100)
