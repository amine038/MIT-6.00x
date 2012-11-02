def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    a_max = n / 6
    b_max = n / 9
    c_max = n / 20
    flag = 0
    for a in range(0, a_max + 1):
        for b in range(0, b_max + 1):
            for c in range(0, c_max + 1):
                if n == (6 * a) + (9 * b) + (20 * c):
                    flag = 1
                    break
    if flag == 1:
        return True
    else:
        return False
    
