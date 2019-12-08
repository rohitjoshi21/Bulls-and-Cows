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
                resp.append('f')
            else:
                resp.append('p')
    if resp == []:
        resp.append('b')

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


def inputClues(valids):
    '''
    Takes clues from the user when computer is guessing the number
    '''
    inp = input('Enter the clues? ').lower()
    inp = inp.replace(' ', '')
    inp = inp.replace('pico', 'p')
    inp = inp.replace('bagel', 'b')
    inp = inp.replace('fermi', 'f')

    hint = ''.join(sorted(list(inp))).lower()

    if hint not in valids:
        print('\nInvalid Clue. Please enter again.')
        return inputClues(valids)
    else:
        return hint


def main(DIGITS, CHANCES):
    all_possible = [''.join(x) for x in permutations('0123456789', DIGITS)]

    VALID_CLUES = []
    for i in range(1, DIGITS + 1):
        clues = map(''.join, combinations_with_replacement('fp', i))
        for clue in clues:
            VALID_CLUES.append(clue)
    VALID_CLUES.append('b')

    # print(VALID_CLUES)
    guessCount = 1
    found = False
    while not found and guessCount < CHANCES:

        guess = getBestGuess(all_possible)
        if guess == None:
            found = True
            break

        print('Guess %d: %s' % (guessCount, guess))

        # Hint is given by user.
        hint = inputClues(VALID_CLUES)

        # If correct
        if hint == 'f' * DIGITS:
            found = True
            print('\nWow, I did it.')

        all_possible = filterPossible(all_possible, guess, hint)

        guessCount += 1

    if found == False:
        print('Oh No! You are out of guess.')


welcomeText = '''
You should think of a 3-digit number. I will try to guess what it is.
Here are some clues which you should give me for my each guesses:
  When you say:          That means:
  Pico   -->P      One digit is correct but in the wrong position.
  Fermi  -->F      One digit is correct and in the right position.
  Bagels -->B      No digit is correct.

I assume you have thought of a number. I will try to guess it.


'''

if __name__ == "__main__":
    DIGITS = 3
    CHANCES = 10

    print(welcomeText)

    while True:
        main(DIGITS, CHANCES)

        resp = input('Do you want to play again? Y/N')
        if resp.lower() in ['y', 'yes', 'ok']:
            continue
        else:
            print('Thank you for playing the game.')
            break
