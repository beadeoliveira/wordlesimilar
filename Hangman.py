'''
Description:
        You must create a Hangman game that allows the user to play and guess a secret word.
        See the assignment description for details.

@author: Bea De Oliveira    bcd23
'''


import random

def handleUserInputDifficulty():
    '''
    This function asks the user if they would like to play the game in (h)ard or (e)asy mode, then returns the
    corresponding number of misses allowed for the game.
    '''

    inp = input("How many misses do you want? Hard has 8 and Easy has 12. Select (h)ard or (e)asy> ")
    if inp == "e":
        return 12
    if inp == "h":
        return 8
    pass



def getWord(words, length):
    '''
    Selects the secret word that the user must guess.
    This is done by randomly selecting a word from words that is of length length.
    '''
    '''list = []
    for word in words:
        if len(word) == length:
            list.append(word)
    total_num = len(list)
    x = random.randint(0,(total_num-1))
    selected = list[x]
    return selected'''

    list = []
    for word in words:
        if len(word) == length:
            list.append(word)
    total_num = len(list)
    x = random.randint(0,(total_num-1))
    selected = list[x]
    return selected

    pass




def createDisplayString(lettersGuessed, missesLeft, hangmanWord):
    '''
    Creates the string that will be displayed to the user, using the information in the parameters.
    '''
    lettersGuessed = " ".join(lettersGuessed)
    hangmanWord = " ".join(hangmanWord)
    missesLeft = str(missesLeft)
    return "letters you've guessed: " + " " + lettersGuessed + "\n" + \
           "misses remaining = " + missesLeft + "\n" + hangmanWord

    pass




def handleUserInputLetterGuess(lettersGuessed, displayString):
    '''
    Prints displayString, then asks the user to input a letter to guess.
    This function handles the user input of the new letter guessed and checks if it is a repeated letter.
    '''
    print(displayString)
    leter = input("letter> ")
    while leter in lettersGuessed:
        print ("you already guessed that")
        leter = input("letter> ")
    return leter



    pass




def updateHangmanWord(guessedLetter, secretWord, hangmanWord):
    '''
    Updates hangmanWord according to whether guessedLetter is in secretWord and where in secretWord guessedLetter is in.
    '''
    hangman_split = list(hangmanWord)
    if guessedLetter in secretWord:
       location = []
       n = 0
    else:
        return hangmanWord
    for letter in secretWord:
        n += 1
        if letter == guessedLetter:
            location.append(n-1)
    if len(location) != 0:
        for place in location:
                hangman_split[place] = guessedLetter
    return hangman_split

    pass




def processUserGuess(guessedLetter, secretWord, hangmanWord, missesLeft):
    '''
    Uses the information in the parameters to update the user's progress in the hangman game.
    '''
    i0 = updateHangmanWord(guessedLetter, secretWord, hangmanWord)
    if guessedLetter in secretWord:
        i1 = missesLeft
        i2 = True
    else:
        i1 = (missesLeft - 1)
        i2 = False
    return [i0, i1, i2]


    #Your Code Here
    pass




def runGame(filename):
    '''
    This function sets up the game, runs each round, and prints a final message on whether or not the user won.
    True is returned if the user won the game. If the user lost the game, False is returned.
    '''

    f = open(filename)
    words = []
    for line in f:
        line = line.strip()
        words.append(line)
    f.close
    length = random.randint(5,10)
    difficultiy = handleUserInputDifficulty()
    word = getWord(words, length)
    guesses = difficultiy
    misses = 0
    lettersGuessed = []
    secretword = ["_" for n in range(length)]
    while guesses > 0 and "_" in secretword:
        displaystring = createDisplayString(lettersGuessed, guesses, secretword)
        guess = handleUserInputLetterGuess(lettersGuessed, displaystring)
        lettersGuessed.append(guess)
        result = processUserGuess(guess, word, secretword, guesses)
        secretword = result[0]
        guesses = result[1]
        correct = result[2]
        if correct == True:
            print(createDisplayString(lettersGuessed, guesses, secretword))
        elif correct == False:
            misses += 1
            print("you missed: " + guess + "not in word")
            print(createDisplayString(lettersGuessed, guesses, secretword))
    if "_" not in secretword:
        print("you guessed the word: " + word)
        print("you made " + str(guesses) + " guesses with " + str(len(lettersGuessed)) + " misses")
        return True
    if "_" in secretword:
        print("you're hung!!" + "\n" + "word is " + word)
        print("you made " + str(difficultiy) + " guesses with " + str(difficultiy) + " misses")
        return False




    '''Loads the words from the file at the location specified in the parameter filename.'''
    '''Randomly chooses the length of the secret word between 5-10 inclusive.'''
    '''Calls handleUserInputDifficulty and getWord'''
    '''After calling the function getWord, it creates the list of strings that holds the currently \n
    displayed hangman (a.k.a. hangmanWord).'''



    #Your Code Here
    pass



if __name__ == "__main__":
    '''
    Running Hangman.py should start the game, which is done by calling runGame, therefore, we have provided you this code below.
    '''
    hello = runGame('lowerwords.txt')
    hello
    wins = 0
    losses = 0
    if hello == True:
        wins += 1
    if hello == False:
        losses += 1
    again = input("Do you want to play again? y or n> ")
    while again == "y":
        hello = runGame('lowerwords.txt')
        hello
        if hello == True:
            wins += 1
        if hello == False:
            losses += 1
        again = input("Do you want to play again? y or n> ")
    print("You won " + str(wins) + " game(s) and lost " + str(losses))


    '''print(updateHangmanWord("a", "cat", ["c", "_", "_"]))'''

    '''print(processUserGuess("l", "happy", "__ppy", 4))'''

    '''length = random.randint(5,10)
    f = open('lowerwords.txt')
    words = []
    for line in f:
        line = line.strip()
        words.append(line)
    f.close
    list = []
    for word in words:
        if len(word) == length:
            list.append(word)
    total_num = len(list)
    x = random.randint(0,(total_num-1))
    selected = list[x]
    print(selected)'''
