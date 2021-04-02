import random


def getrandomnumber(digit):
    nums = list(range(10))
    random.shuffle(nums)
    start = 0 if nums[0] != 0 else 1
    n = nums[start:start + digit]
    return [str(i) for i in n]


def getclues(sec, inp):
    resp = []
    for i, n in enumerate(inp):
        if n in sec:
            if inp[i] == sec[i]:
                resp.append('Bull')
            else:
                resp.append('Cow')
    if resp == []:
        resp.append('Nothing matched')
    resp.sort()
    return ' '.join(resp)


def main(DIGIT, GUESS):
    secretnum = getrandomnumber(DIGIT)
    solved = False
    for i in range(GUESS):
        print('Guess #%d:' % (i + 1))
        inp = list(input())
        if inp == secretnum:
            print('You got it')
            solved = True
            break
        response = getclues(secretnum, inp)
        print(response + '\n')
    if not solved:
        print('Oops! You are out of guess.')
        print('The secret number is ', secretnum)


# Main Program Starts Here:-
welcometext = \
    '''
I am thinking of a 3-digit number. Try to guess what it is.
Here are some clues:
When I say:   That means:
  Cow         A digit is correct but in the wrong position.
  Bull        A digit is correct and in the right position.

I have thought up a number. You have to guess the number now.
'''

if __name__ == "__main__":
    GUESS = 10
    DIGIT = 3
    print(welcometext)
    play = True
    while play:
        main(DIGIT, GUESS)
        ans = input('Do you want to play again? Y/N ')
        print()
        if ans.lower() not in ['y', 'yes', 'ok', '1']:
            play = False
