def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    newTup = ()
    for index in range(0, len(aTup), 2):
        newTup = newTup + (aTup[index],)
    return newTup
