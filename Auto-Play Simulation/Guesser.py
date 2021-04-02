import random
from itertools import permutations, combinations_with_replacement


def getBestGuess(possible):
    '''
    Select a best guess from the list of possible guesses.
    Not Implemented Completely
    '''

    if len(possible) > 0:
        return possible[0]
    else:
        print('You have given some wrong clues. Play Again.')
        return None


def getClues(num, guess):
    '''
    Takes a secret number and guess and return the clue for it
    '''

    resp = []
    for i, n in enumerate(guess):
        if n in num:
            if guess[i] == num[i]:
                resp.append('b')
            else:
                resp.append('c')
    if resp == []:
        resp.append(' ')

    resp.sort()
    return ''.join(resp)


def filterPossible(possible, guess, hint):
    '''
    Removes all the numbers from possible which cannot be the secret number.
    '''

    i = 0
    while i < len(possible):
        num = possible[i]
        result = getClues(num, guess)

        if result.lower() != hint.lower():
            possible.remove(num)
            i -= 1

        i += 1
    return possible


def main(DIGITS, all_possible, previousGuess, clue):

    if clue:
        all_possible = filterPossible(all_possible, previousGuess, clue)

    guess = getBestGuess(all_possible)

    return guess, all_possible
