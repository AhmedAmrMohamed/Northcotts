def logtime():
    import time
    f=open('log.txt','a')
    print(time.ctime(),file=f)
    f.close()
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
                out[-1].append('w')
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
    if(row<1 or row>8):
        print('Invalid row number')
        return False
    row-=1
    orgw=board[row][0]
    orgb=board[row][1]
    turn=turn.lower()
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
def end():
    '''
    return false if there is no more valid moves.
    Otherwise return true.
    '''
    for row in board:
        if row[1]-row[0]>1:
            return False
    else:
        return True
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
def iturn(x):
    '''
    inverse the turn for black to white and vice versa
    '''
    if x=='w':
        return 'b'
    else:
        return 'w'
def getinp(turn):
    while True:
        inp = input('{} play:'.format(turn)).split()
        if len(inp)==2:
            f=open('log.txt','a')
            print('{} {}'.format(inp[0],inp[1]),file=f)
            return int(inp[0]),int(inp[1])
            print('invalid input\nPlease enter the row number of the piece you want to move and it\'s destination\n')

def main():
    print('Welcom to northcotts\n')
    logtime()
    turn='b'
    while not end():
        turn=iturn(turn)
        dis()
        row,to=getinp(turn)
        if not play(turn,row,to):
            turn=iturn(turn)
    dip()
    terminate(turn)
main()
