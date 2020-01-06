# Problem Set 2, hangman.py
# Name: Alec Dewulf 
# Collaborators:
# Time spent: 2 Hours
# Added in an option for the user to select whether or not they want
# to play with hints.

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"

print("Would you like to play with hints?")
game_mode = input("Y for yes, N for no: ")


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program

wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    num_wrong = 0
    for l in secret_word:
        if l in letters_guessed:
            pass
        else:
            num_wrong += 1

    if num_wrong == 0:
        return True
    else:
        return False


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    ans = ''
    for l in secret_word:
        if l in letters_guessed:
            ans += l
        else:
            ans = ans + "_ "
    return ans


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    alph = string.ascii_lowercase

    available_letters = ''

    for l in alph:
        if l in letters_guessed:
            pass
        else:
            available_letters += l
            
    return available_letters
        

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # JUST NEED TO IMPLEMENT WINNING CONDITION
    print("Welcome to the game Hangman!")
    

    #find the amount of unique letters
    unique_letters = []
    for l in word:
        if l not in unique_letters:
            unique_letters.extend(l)
    
    print("I am thinking of a word that is", len(word), "letters long...")
    print("---------------------")
    guesses = 6
    print("You have", guesses, "guesses left")

    lets_guessed = []

    print("Available letters:", get_available_letters(lets_guessed))
    letters_guessed = []
    vowels = ['a', 'e', 'i', 'o', 'u']

    warnings = 3
    while guesses > 0:
        
        guess = input("Please guess a letter: ").lower()

        if guess in word and guess not in letters_guessed:
            letters_guessed.append(guess)
            if '_' not in get_guessed_word(word, letters_guessed):
                total_score = guesses * len(unique_letters)
                print("Congrutulations, you won!")
                print("The word was:", get_guessed_word(word, letters_guessed))
                print("Your score was:", total_score)
                break
            
            else:
                print("Good guess:", get_guessed_word(word, letters_guessed))
            
        
        # if they guessed something that wasn't a letter   
        elif guess not in string.ascii_lowercase:
            warnings -= 1
            if warnings != 0:
                print("Not a valid input, you have", warnings, "warnings left")

            # loose a guess on the third warning
            elif warnings == 0:
                print("That was your third warning!")
                print("As a punishment, you have lost a guess")
                warnings = 3
                guesses -= 1
                
        elif guess not in word and guess not in letters_guessed:
            letters_guessed.append(guess)
            if guess not in vowels:
                print("Oops! That letter is not in my word")
                print("Please guess a letter:", get_guessed_word(word, letters_guessed))
                guesses -= 1
            else:
                print("That vowel isn't in my word")
                print("Choosing an incorrect vowel costs you 2 guesses")
                print(get_guessed_word(word, letters_guessed))
                guesses -= 2

        elif guess in letters_guessed:
            warnings -= 1
            
            if warnings != 0:
                print("Oops! You've already guessed that letter. You have", warnings, "warnings left:")
                print(get_guessed_word(word, letters_guessed))
            elif warnings == 0:
                print("Oops! You've already guessed that letter. You have no warnings left")
                print("so you lose one guess:", get_guessed_word(word, letters_guessed))
                warnings = 3
                guesses -= 1
            
        if guesses > 0:
            print("---------------------")
            print("You have", guesses, "guesses left")         
            print("Available letters:", get_available_letters(letters_guessed))
        else:
            print("---------------------")
            print("Sorry, you ran out of guesses")
            print("GAME OVER")
            print("The word was", word)


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------

def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    wrong_letters = 0
    no_space_word = ""

    # removing spaces
    for l in my_word:
        if l != " ":
            no_space_word += l

    # check for length first count the number of wrong letters
    if len(no_space_word) == len(other_word):

        x = 0
        while x < len(no_space_word):
            if no_space_word[x] != "_" and no_space_word[x] != other_word[x]:
                wrong_letters += 1

            x += 1 
    else:
        return False

    if wrong_letters == 0:
        return True
    else:
        return False

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    matches = ""
    for w in wordlist:
        if match_with_gaps(my_word, w):
            matches += " " + w

    return matches

def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print("Welcome to the game Hangman!")
    

    #find the amount of unique letters
    unique_letters = []
    for l in word:
        if l not in unique_letters:
            unique_letters.extend(l)
    
    print("I am thinking of a word that is", len(word), "letters long...")
    print("---------------------")
    guesses = 6
    print("You have", guesses, "guesses left")

    lets_guessed = []

    print("Available letters:", get_available_letters(lets_guessed))
    letters_guessed = []
    vowels = ['a', 'e', 'i', 'o', 'u']

    warnings = 3
    while guesses > 0:
        
        guess = input("Please guess a letter: ").lower()

        if guess in word and guess not in letters_guessed:
            letters_guessed.append(guess)
            if '_' not in get_guessed_word(word, letters_guessed):
                total_score = guesses * len(unique_letters)
                print("Congrutulations, you won!")
                print("The word was:", get_guessed_word(word, letters_guessed))
                print("Your score was:", total_score)
                break
            
            else:
                print("Good guess:", get_guessed_word(word, letters_guessed))
            
            

        # if they guessed something that wasn't a letter   
        elif guess not in string.ascii_lowercase:
            # special character
            if guess == "*":
                print("Possible word matches are:")
                print(show_possible_matches(get_guessed_word(word, letters_guessed)))
            else:
                warnings -= 1
            # maxed out on warnings  
            if warnings != 0:
                print("Not a valid input, you have", warnings, "warnings left")

            # loose a guess on the third warning
            elif warnings == 0:
                print("That was your third warning!")
                print("As a punishment, you have lost a guess")
                warnings = 3
                guesses -= 1

        # wrong guess       
        elif guess not in word and guess not in letters_guessed:
            letters_guessed.append(guess)
            # consonant
            if guess not in vowels:
                print("Oops! That letter is not in my word")
                print("Please guess a letter:", get_guessed_word(word, letters_guessed))
                guesses -= 1
            # vowel
            else:
                print("That vowel isn't in my word")
                print("Choosing an incorrect vowel costs you 2 guesses")
                print(get_guessed_word(word, letters_guessed))
                guesses -= 2
        # guessing the same letter twice
        elif guess in letters_guessed:
            warnings -= 1
            # not third warning
            if warnings != 0:
                print("Oops! You've already guessed that letter. You have", warnings, "warnings left:")
                print(get_guessed_word(word, letters_guessed))
            # third warning
            elif warnings == 0:
                print("Oops! You've already guessed that letter. You have no warnings left")
                print("so you lose one guess:", get_guessed_word(word, letters_guessed))
                warnings = 3
                guesses -= 1
        # still playing    
        if guesses > 0:
            print("---------------------")
            print("You have", guesses, "guesses left")         
            print("Available letters:", get_available_letters(letters_guessed))
        # Game ending condition
        else:
            print("---------------------")
            print("Sorry, you ran out of guesses")
            print("GAME OVER")
            print("The word was", word)


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.

if game_mode == "Y" or game_mode == "y":
    word = choose_word(wordlist)
    hangman_with_hints(word)
    
elif game_mode == "N" or game_mode == 'n':
    word = choose_word(wordlist)
    hangman(word)
