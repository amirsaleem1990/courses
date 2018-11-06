def insert_sequence(sq1, sq2, ind):
    '''
    (str, str, int) -> str
    '''

    s = sq1[ :ind]
    g = sq1[(len(s) + ind):-1]
    
    
