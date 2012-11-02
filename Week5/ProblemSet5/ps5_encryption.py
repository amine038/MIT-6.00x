# 6.00x Problem Set 5
#
# Part 1 - HAIL CAESAR!

# edX MIT 6.00x Week 5
# Jaskirat Singh
# 02 November, 2012


import string
import random

WORDLIST_FILENAME = "words.txt"

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = inFile.read().split()
    print "  ", len(wordList), "words loaded."
    return wordList

def isWord(wordList, word):
    """
    Determines if word is a valid word.

    wordList: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordList.

    Example:
    >>> isWord(wordList, 'bat') returns
    True
    >>> isWord(wordList, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in wordList

def randomWord(wordList):
    """
    Returns a random word.

    wordList: list of words  
    returns: a word from wordList at random
    """
    return random.choice(wordList)

def randomString(wordList, n):
    """
    Returns a string containing n random words from wordList

    wordList: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([randomWord(wordList) for _ in range(n)])

def randomScrambled(wordList, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordList: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words

    NOTE:
    This function will ONLY work once you have completed your
    implementation of applyShifts!
    """
    s = randomString(wordList, n) + " "
    shifts = [(i, random.randint(0, 25)) for i in range(len(s)) if s[i-1] == ' ']
    return applyShifts(s, shifts)[:-1]

def getStoryString():
    """
    Returns a story in encrypted text.
    """
    return open("story.txt", "r").read()


# (end of helper code)
# -----------------------------------


#
# Problem 1: Encryption
#
def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    import string
    dict_mapping = {}
    alphabet = string.ascii_uppercase + string.ascii_lowercase
    for char in alphabet:
        flag = -1
        # get ascii value of character
        ascii_char = ord(char)

        # get value in 0 - 26
        if ascii_char <= 90:
            ascii_char -= 65
            flag = 1 #uppercase
        else:
            ascii_char -= 97
            flag = 0 #lowercase

        # apply shift
        shifted_char_ascii = ascii_char + shift

        # wrap around
        shifted_char_ascii %= 26

        # get ascii values
        if flag == 1:
            shifted_char_ascii += 65  #uppercase
        elif flag == 0:
            shifted_char_ascii += 97  #lowercase

    
        shifted_char = chr(shifted_char_ascii)
        
        # add mapping to dictionary
        dict_mapping[char] = shifted_char

    return dict_mapping


def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    # change into list
    text = list(text)

    for index in range(0, len(text)):
        # transform alphabet characters only
        text[index] = coder.get(text[index], text[index])

    # change back to string
    return "".join(text)
            
    

def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    return applyCoder(text, buildCoder(shift))
    

#
# Problem 2: Decryption
#
def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    max_valid_words = 0
    best_shift = 0
    
    for shift in range(0, 26):
        valid_words = 0
        # decrypt text
        decrypted_text = applyShift(text, shift)
        # split into list, spaces based
        decrypted_text = decrypted_text.split()

        for word in decrypted_text:
            #change to lowercase
            word = word.lower()
            # strip punctuations
            word = word.translate(None, string.punctuation)
            if word in wordList:
                valid_words += 1
        if valid_words > max_valid_words:
            max_valid_words = valid_words
            best_shift = shift
    return best_shift


def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Use the functions getStoryString and loadWords to get the
    raw data you need.

    returns: string - story in plain text
    """
    text = getStoryString()
    shift = findBestShift(wordList, text)
    print applyShift(text, shift)    
    
#
# Build data structures used for entire session and run encryption
#

if __name__ == '__main__':
    wordList = loadWords()
    decryptStory()


################
##DECRYPTED TEXT
################

##Jack Florey is a mythical character created on the spur of a moment
##to help cover an insufficiently planned hack. He has been registered
##for classes at MIT twice before, but has reportedly never passed a
##class. It has been the tradition of the residents of East Campus to
##become Jack Florey for a few nights each year to educate incoming
##students in the ways, means, and ethics of hacking.
