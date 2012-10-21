def lenIter(aStr):
    length = 0
    for char in aStr:
        length += 1
    return length

def lenRecur(aStr):
    if aStr == '':
        return 0
    return 1 + lenRecur(aStr[1:])
