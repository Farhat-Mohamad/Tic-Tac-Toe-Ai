EMPTY = ' '

map = [
    [EMPTY , EMPTY , EMPTY],
    [EMPTY , EMPTY , EMPTY],
    [EMPTY , EMPTY , EMPTY],
]

def printMap(a):
    for b in a:
        print(b)
    print("\n")

def check_winner(a, player):
    if (a[0][0]==player and a[0][1]==player and a[0][2]==player) or ( 
    a[1][0]==player and a[1][1]==player and a[1][2]==player) or (
    a[2][0]==player and a[2][1]==player and a[2][2]==player) or (
    a[0][0]==player and a[1][0]==player and a[2][0]==player) or (
    a[0][1]==player and a[1][1]==player and a[2][1]==player) or (
    a[0][2]==player and a[1][2]==player and a[2][2]==player) or (
    a[0][0]==player and a[1][1]==player and a[2][2]==player) or (
    a[0][2]==player and a[1][1]==player and a[2][0]==player):
        return True
    else:
        return False
    
def no_winner(a):
    if a[0][0]!=EMPTY and a[0][1]!=EMPTY and a[0][2]!=EMPTY and a[1][0]!=EMPTY and a[1][1]!=EMPTY and a[1][2]!=EMPTY and a[2][0]!=EMPTY and a[2][1]!=EMPTY and a[2][2]!=EMPTY and check_winner(map, "X")==False and check_winner(map, "O")==False :
        return True
    return False

    
    
def minimax(map, isMaxing, depth):
    if check_winner(map,"O") == True:
        return 1
    elif check_winner(map,"X") == True:
        return -1
    elif no_winner(map)==True or depth ==0:
        return 0
    
    #if none of the above happened, then that means that the game is still going on:

    if isMaxing:  # ai to make a move (calculate the value of the move)
        value = -float('inf')
        other_value = 0

        for i in range(3):
            for j in range(3):
                if map[i][j] == EMPTY:
                    map[i][j] = "O"
                    other_value = minimax(map, False, depth-1)  # we want to see what value does this move gives us                            # we put false to let the code of other player get running to continue checking for the best value
                    value = max(value, other_value)
                    map[i][j] = EMPTY
        return value
    
    if not isMaxing:
        value = float('inf')
        other_value = 0
        for i in range(3):
            for j in range(3):
                if map[i][j] == EMPTY:
                    map[i][j] = "X"
                    other_value = minimax(map, True, depth-1)
                    value = min(value, other_value)
                    map[i][j]= EMPTY
        return value



def select_move(map):
    best_value = -float('inf')
    move = None

    for i in range(3):
        for j in range(3):
            if map[i][j]== EMPTY:
                map[i][j] = "X"
                value = minimax(map,  True, 3)
                map[i][j]= EMPTY
                if value > best_value:
                    best_value = value
                    move=(i,j)
    return move




print("Let's start the game!")
while(1):
    printMap(map)
    print("X's turn, select a move: ")
    x = int(input())
    y = int(input())

    while x < 0 or y < 0 or x > 2 or y > 2 or map[x][y] != EMPTY or map[x][y] == 'O':
        print("Invalid move, try again:")
        x = int(input())
        y = int(input())
    map[x][y] = "X"
    printMap(map)

    if check_winner(map, "X")==True:
        print("Player X is the winner")
        break
    if no_winner(map):
        print("The game ended with a draw")
        break

    print("O's turn, do a move: ")

    move = select_move(map)
    
    map[move[0]][move[1]] = "O"
    
    printMap(map)

    if check_winner(map, "O")==True:
        print("Player O is the winner")
        break
    
    if no_winner(map):
        print("The game ended with a draw")
        break