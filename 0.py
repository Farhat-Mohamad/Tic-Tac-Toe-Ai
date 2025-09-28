EMPTY = ' '

map = [
    [EMPTY,EMPTY,EMPTY],
    [EMPTY,EMPTY,EMPTY],
    [EMPTY,EMPTY,EMPTY],
]

def printMap(a):
    for b in a:
        print(b)

def check_winner(a, player):
    if (a[0][0]=='player' and a[0][1]=='player' and a[0][2]=='player') or ( 
    a[1][0]=='player' and a[1][1]=='player' and a[1][2]=='player') or (
    a[2][0]=='player' and a[2][1]=='player' and a[2][2]=='player') or (
    a[0][0]=='player' and a[1][0]=='player' and a[2][0]=='player') or (
    a[0][1]=='player' and a[1][1]=='player' and a[2][1]=='player') or (
    a[0][2]=='player' and a[1][2]=='player' and a[2][2]=='player') or (
    a[0][0]=='player' and a[1][1]=='player' and a[2][2]=='player') or (
    a[0][2]=='player' and a[1][1]=='player' and a[2][0]=='player'):
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
    
    if isMaxing:
        value = ('-Infinity')
        for i in range(3):
            for j in range(3):
                if map[i][j] == EMPTY:
                    map[i][j] = "O"
                    other_value = minimax(map, False, depth-1)
                    value = max(value, other_value)
                    map[i][j] = EMPTY
        return value
    
    if not isMaxing:
        value = ('+Infinity')
        for i in range(3):
            for j in range(3):
                if map[i][j] == EMPTY:
                    map[i][j] = "X"
                    other_value = minimax(map, True, depth-1)
                    value = min(value, other_value)
                    map[i][j]= EMPTY
        return value



