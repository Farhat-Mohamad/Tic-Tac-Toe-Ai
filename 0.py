EMPTY = ' '

def printMap(a):
    for b in a:
        print(b)

def O_is_winner(a):
    if (a[0][0]=='O' and a[0][1]=='O' and a[0][2]=='O') or ( 
    a[1][0]=='O' and a[1][1]=='O' and a[1][2]=='O') or (
    a[2][0]=='O' and a[2][1]=='O' and a[2][2]=='O') or (
    a[0][0]=='O' and a[1][0]=='O' and a[2][0]=='O') or (
    a[0][1]=='O' and a[1][1]=='O' and a[2][1]=='O') or (
    a[0][2]=='O' and a[1][2]=='O' and a[2][2]=='O') or (
    a[0][0]=='O' and a[1][1]=='O' and a[2][2]=='O') or (
    a[0][2]=='O' and a[1][1]=='O' and a [2][0]=='O'):
        return True
    else:
        return False
    
def X_is_winner(a):
    if (a[0][0]=='X' and a[0][1]=='X' and a[0][2]=='X') or ( 
    a[1][0]=='X' and a[1][1]=='X' and a[1][2]=='X') or (
    a[2][0]=='X' and a[2][1]=='X' and a[2][2]=='X') or (
    a[0][0]=='X' and a[1][0]=='X' and a[2][0]=='X') or (
    a[0][1]=='X' and a[1][1]=='X' and a[2][1]=='X') or (
    a[0][2]=='X' and a[1][2]=='X' and a[2][2]=='X') or (
    a[0][0]=='X' and a[1][1]=='X' and a[2][2]=='X') or (
    a[0][2]=='X' and a[1][1]=='X' and a[2][0]=='X'):
        return True
    else:
        return False


map = [[EMPTY for _ in range(3)] for _ in range (3)]
    
printMap(map)

while( O_is_winner(map) == False and X_is_winner(map) == False):
        
    print("X's Turn\nEnter your coordinates: ")
    x = int(input())
    y = int(input())

    while x < 0 or y < 0 or x > 2 or y > 2 or map[x][y] != EMPTY or map[x][y] == 'O':
        print("Invalid movement, try again:")
        x = int(input())
        y = int(input())
    map[x][y] = 'X'
    printMap(map)

    if X_is_winner(map) == True:
        print("The player X is the winner!!")
        break

    print("O's Turn\nEnter your coordinates: ")
    x = int(input())
    y = int(input())

    while x < 0 or y < 0 or x > 2 or y > 2 or map[x][y] != EMPTY or map[x][y] == 'X':
        print("Invalid move, try again")
        x = int(input())
        y = int(input())
    map[x][y] = 'O'
    printMap(map)

    if O_is_winner(map) == True:
        print("The player O is the winner!!")
        break
