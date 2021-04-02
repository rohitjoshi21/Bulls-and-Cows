from itertools import permutations
import random
import time

import Guesser


DIGITS = 3
TIMES = 1000


def simulateGame(all_possible):

    all_possible = all_possible[:]

    secretNum = random.choice(all_possible)

    clue = None
    guess = None
    count = 0
    while True:

        guess, all_possible = Guesser.main(DIGITS, all_possible, guess, clue)
        clue = Guesser.getClues(secretNum, guess)

        count += 1
        if clue == 'b' * DIGITS:
            return count

if __name__ == "__main__":

    all_possible = [''.join(x) for x in permutations('0123456789', DIGITS)]

    random.shuffle(all_possible)

    counts = []
    for i in range(TIMES):
        c = simulateGame(all_possible)
        counts.append(c)

    average = sum(counts)/len(counts)
    
    output = \
'''
Simulation done for %d times and the results obtained are:

Maximum no of steps needed: %d
Minimum no of steps needed: %d
Average steps need:         %.2f
'''
    print(output%(TIMES,max(counts),min(counts),average))
