# 6.00x Problem Set 5
#
# Part 2 - RECURSION

#
# Problem 3: Recursive String Reversal
#
def reverseString(aStr):
    """
    Given a string, recursively returns a reversed copy of the string.
    For example, if the string is 'abc', the function returns 'cba'.
    The only string operations you are allowed to use are indexing,
    slicing, and concatenation.
    
    aStr: a string
    returns: a reversed string
    """
    if len(aStr) == 0:
        return ""
    return aStr[-1] + reverseString(aStr[:len(aStr) - 1])

#
# Problem 4: Erician
#
def x_ian(x, word):
    """
    Given a string x, returns True if all the letters in x are
    contained in word in the same order as they appear in x.

    >>> x_ian('eric', 'meritocracy')
    True
    >>> x_ian('eric', 'cerium')
    False
    >>> x_ian('john', 'mahjong')
    False
    
    x: a string
    word: a string
    returns: True if word is x_ian, False otherwise
    """
    ##ITERATIVE APPROACH
##    tmp = list()
##    index = 0
##    x = list(x)
##    for char in word:
##        if char == x[index]:
##            tmp.append(char)
##            index += 1
##            if len(tmp) == len(x):
##                break
##    print tmp
##    if tmp == x:
##        return True
##    else:
##        return False

    # RECURSIVE APPROACH
    if len(x) == 0:
        return True
    elif len(word) == 0:
        return False
        
    word = list(word)
    x = list(x)
    if x[0] == word[0]:
        x.pop(0)
        return x_ian("".join(x), "".join(word))
    else:
        word.pop(0)
        return x_ian("".join(x), "".join(word))
            

#
# Problem 5: Typewriter
#
def insertNewlines(text, lineLength):
    """
    Given text and a desired line length, wrap the text as a typewriter would.
    Insert a newline character ("\n") after each word that reaches or exceeds
    the desired line length.

    text: a string containing the text to wrap.
    line_length: the number of characters to include on a line before wrapping
        the next word.
    returns: a string, with newline characters inserted appropriately. 
    """
    def insertNewlinesRec(text, lineLength):
        #base cases
        if len(text) <= lineLength:
            return text
        
        #insert new line after space
        if text[lineLength - 1] == " ":
            return text[:lineLength] + "\n" + insertNewlinesRec(text[lineLength:], lineLength)
        else:
            return text[0] + insertNewlinesRec(text[1:], lineLength)
    return insertNewlinesRec(text, lineLength)
