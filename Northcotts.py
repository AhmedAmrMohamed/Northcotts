board=[[1,8] for i in range(8)]
def build_board():
    '''
    return a list of 8 lists each represent a row.
    '''
    out=[]
    for row in board:
        out.append([])
        for cell in range(1,9):
            if cell ==row[0]:
                out[-1].append('W')
            elif cell==row[1]:
                out[-1].append('B')
            else:
                out[-1].append('.')
    return out
def dis():
    '''
    print the board
    '''
    for i in build_board():
        print(' '.join(i))
def numsum():
    '''
    return the num sum of the boad
    used to calculate the best winning moves.
    '''
    sum=0
    for row in board:
        sum^=abs(row[0]-row[1]-1)
    return sum
def valid(w,b):
    '''
    return True if a move is valid; Otherwise
     prints an error msg and return False.
     '''
    if w>=b:
        print('A piece may not jump over or onto the other.')
        return False
    elif not(w>0 and w<9 and b>0 and b<9):
        print('Yoy need to play inside the board')
        return False
    return True

def play(turn,row,to):
    '''
    update the board and return tur if the move is valid.
    Otherwise return false
    '''
    if(row<0 or row>7):
        print('Invalid row number')
        return False
    orgw=board[row][0]
    orgb=board[row][1]
    turn=turn.lower()
    row-=1
    if(turn=='w'):
        if valid(to,orgb):
            board[row][0]=to
        else:
            return False
    elif(turn=='b'):
        if valid(orgw,to):
            board[row][1]=to
        else:
            return False
    else:
        return False
        print('Invalid Turn Choice')
    return True
def checkend():
    '''
    return false if there is no more valid moves.
    Otherwise return true.
    '''
    for row in board:
        if row[1]-row[0]>1:
            return True
    else:
        return False
def terminate(turn):
    '''
    output the result. And terminate the program.
    '''
    turn=turn.lower()
    if turn=='w':
        turn='White'
    else:
        turn='Black'
    input('{} Has won\npress any key to exit.\n'.format(turn))
    quit()
