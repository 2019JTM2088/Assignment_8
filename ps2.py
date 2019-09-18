#! /usr/bin/python3

print("'Welcome to the Game!'") 
# draw a board:
def draw():
    board = ''

    for i in range(-1,6):

        if i%2==0:
            board += '|      ' * 4
            board += '\n|      |      |      |'

        else:
            board += ' _____ ' * 3

        board += '\n'
    print (board)

draw()
List1=[1,3,5,7,9]
List2=[2,4,6,8]

# Check for empty places on board 
def possibilities(board): 
    l = [] 
      
    for i in range(len(board)): 
        for j in range(len(board)): 
              
            if board[i][j] == 0: 
                l.append((i, j)) 
    return(l) 
    
while not winner :
    draw()

    if playerOneTurn :
        print( "Player 1:")
    else :
        print( "Player 2:")

