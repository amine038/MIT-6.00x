def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    s1 = list(s1)
    s2 = list(s2)
    new_str = list()
    index_s1 = 0
    index_s2 = 0

    while True:
        if index_s1 < len(s1):
            new_str.append(s1[index_s1])
            index_s1 += 1
        if index_s2 < len(s2):
            new_str.append(s2[index_s2])
            index_s2 += 1
        if len(new_str) == len(s1) + len(s2):
            s1 = "".join(s1)
            s2 = "".join(s2)
            return "".join(new_str)
