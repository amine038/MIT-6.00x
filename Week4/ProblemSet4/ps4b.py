# Problem #6: Computer chooses a word
# edX PSET 4
#
# Jaskirat Singh
# 27 October, 2012

#####################################################################
# This code works fine(the functional parts),
# but is still buggyin function playHand().
# Need to configure the user input correctly.
# It's not very interesting, so I'm not going to fix it.
# Again, the functional parts work just fine.
#####################################################################

from ps4a import *
import time

def compChooseWord(hand, wordList):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    returns: string or None
    """
    best_score = 0
    best_word = None
    iters = 0
    for word in wordList:
        iters += 1
        if isValidWord(word, hand, wordList) == True:
            score = getWordScore(word, HAND_SIZE)
            if score > best_score:
                best_score = score
                best_word = word
    #print iters
    return best_word

#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList):
    """
    hand: dictionary (string -> int)
    wordList: list (string)
    """
    score = 0
    letters_left = calculateHandlen(hand)
        
    while(letters_left > 0):
        # Display the hand
        print 'Current hand: ',
        displayHand(hand)
        
        # Ask user for input
        computer_word = compChooseWord(hand, wordList)

        # end game if no valid word is chosen from the hand
        if computer_word == None:
            computer_word = '.'

        # If the input is a single period:
        if computer_word == '.':
            break
        
        if (isValidWord(computer_word, hand, wordList) == False):
            print 'Invalid word, please try again.'
            print
        else:
            word_score = getWordScore(computer_word, HAND_SIZE)
            score += word_score
            print computer_word, 'earned', word_score, 'points. Total:', score, 'points.'
            print
            hand = updateHand(hand, computer_word)
            letters_left = calculateHandlen(hand)
            if letters_left == 0:
                print 'Run out of letters. Total Score:', score
                return

    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    print 'Goodbye. Total score:', score, 'points.'
    
#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    #initialise hand
    hand = {}
    user_input_valid = 'nre'
    game_input_valid = 'cu'
    while(True):
        user_input = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if user_input not in user_input_valid:
            continue
        
        # exit game for e
        if user_input == 'e':
            return

        game_input = raw_input('Enter u to play, c to watch the computer play: ')
        if game_input not in game_input_valid:
            print 'Invalid command.'
            continue
        else:
            if game_input == 'c':
                user_input = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
                hand = dealHand(HAND_SIZE)
                copy_hand = copy.deepcopy(hand)
                compPlayHand(copy_hand, wordList)
                continue
            else:
                if hand == {}:
                    print 'You have not played a hand yet. Please play a new hand first!'
                    continue
                else:
                    copy_hand = copy.deepcopy(hand)
                    playHand(copy_hand, wordList, HAND_SIZE)
                    continue

        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)


#HAND_SIZE = 15
#hand = dealHand(HAND_SIZE)
#compPlayHand(hand, wordList)
