import UserGuessing
import ComputerGuessing

welcomeText = \
    '''
Welcome to the game of Bulls and Cows.
In this game, one should think of a 3-digit number having different digits. Then another will try to guess what it is.
Here are some clues which should be given for each guesses:
  Clues:           Meaning:
  Bull  --> B      One digit is correct and in the right position.
  Cow   --> C      One digit is correct but in the wrong position.

Lets start the game

'''

question = \
    '''
What do you want to do?
1. Guess
2. Think

Enter 1 or 2
'''

DIGITS = 3
CHANCES = 10

if __name__ == '__main__':
    print(welcomeText)

    while True:
        print(question)
        response = input('>> ')

        if response == '1':
            UserGuessing.main(DIGITS, CHANCES)
        elif response == '2':
            ComputerGuessing.main(DIGITS, CHANCES)

        # Play Again
        resp = input('Do you want to play again? Y/N')
        if resp.lower() in ['y', 'yes', 'ok']:
            print()
            continue
        else:
            print('Thank you for playing the game.')
            break
