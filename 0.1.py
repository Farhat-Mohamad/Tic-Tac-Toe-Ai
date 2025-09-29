EMPTY = ' '

map = [[EMPTY for _ in range(9)] for _ in range (9)]


def printMap(a):
    for i in range(9):
        cell = " | ".join(a[i])
        print (cell)


def box1_winner(a, player):
    for i in range(3):
        if (a[i][0] == a[i][1] == a[i][2] == player) or (
        a[0][i] == a[1][i] == a[2][i] == player ) or (
        a[0][0] == a[1][1] == a[2][2] == player) or (
        a[0][2] == a[1][1] == a[2][0] == player):
            return True
    return False

def box4_winner(a, player):
    for i in range(3,6):
            if (a[i][0] == a[i][1] == a[i][2] == player) or (
            a[0][i] == a[1][i] == a[2][i] == player ) or (
            a[0][0] == a[1][1] == a[2][2] == player) or (
            a[0][2] == a[1][1] == a[2][0] == player):
                return True
    return False

def box7_winner(a, player):
    for i in range(6,9):
            if (a[i][0] == a[i][1] == a[i][2] == player) or (
            a[0][i] == a[1][i] == a[2][i] == player ) or (
            a[0][0] == a[1][1] == a[2][2] == player) or (
            a[0][2] == a[1][1] == a[2][0] == player):
                return True
    return False

def box2_winner(a, player):
    for i in range(3):
        if (a[i][3] == a[i][4] == a[i][5] == player) or (
        a[0][3] == a[1][3] == a[2][3] == player ) or (
        a[0][4] == a[1][4] == a[2][4] == player ) or (
        a[0][5] == a[1][5] == a[2][5] == player ) or (

        a[0][3] == a[1][4] == a[2][5] == player) or (
        a[2][3] == a[1][4] == a[0][5] == player):
            return True
    return False

def box3_winner(a, player):
    for i in range(3):
        if (a[i][6] == a[i][7] == a[i][8] == player) or (
        a[0][6] == a[1][6] == a[2][6] == player ) or (
        a[0][7] == a[1][7] == a[2][7] == player ) or (
        a[0][8] == a[1][8] == a[2][8] == player ) or (

        a[0][3] == a[1][4] == a[2][5] == player) or (
        a[2][3] == a[1][4] == a[0][5] == player):
            return True
    return False

def box5_winner(a, player):
    for i in range(3,6):
        if (a[i][3] == a[i][4] == a[i][5] == player) or (
        a[3][3] == a[4][3] == a[5][3] == player ) or (
        a[3][4] == a[4][4] == a[5][4] == player ) or (
        a[3][5] == a[4][5] == a[5][5] == player ) or (

        a[3][3] == a[4][4] == a[5][5] == player) or (
        a[3][5] == a[4][4] == a[5][3] == player):
            return True
    return False

def box6_winner(a, player):
    for i in range(3,6):
        if (a[i][6] == a[i][7] == a[i][8] == player) or (
        a[3][6] == a[4][6] == a[5][6] == player ) or (
        a[3][7] == a[4][7] == a[5][7] == player ) or (
        a[3][8] == a[4][8] == a[5][8] == player ) or (

        a[3][6] == a[4][7] == a[5][8] == player) or (
        a[5][6] == a[4][7] == a[3][8] == player):
            return True
    return False

def box8_winner(a, player):
    for i in range(6,9):
        if (a[i][3] == a[i][4] == a[i][5] == player) or (
        a[6][3] == a[7][3] == a[8][3] == player ) or (
        a[6][4] == a[7][4] == a[8][4] == player ) or (
        a[6][5] == a[7][5] == a[8][5] == player ) or (

        a[6][3] == a[7][4] == a[8][5] == player) or (
        a[6][8] == a[7][4] == a[8][3] == player):
            return True
    return False

def box9_winner(a, player):
    for i in range(6,9):
        if (a[i][6] == a[i][7] == a[i][8] == player) or (
        a[6][6] == a[7][6] == a[8][6] == player ) or (
        a[6][7] == a[7][7] == a[8][7] == player ) or (
        a[6][8] == a[7][8] == a[8][8] == player ) or (

        a[6][6] == a[7][7] == a[8][8] == player) or (
        a[8][6] == a[7][7] == a[6][8] == player):
            return True
    return False

def small_box_winner(a):
    for t in range(1,4):
        for i in range(3*t):
            for j in range(9):
                a[i][j]="M"

small_box_winner(map)
printMap(map)

#def X_is_winner(a):
    # if (a[0][0]=='X' and a[0][1]=='X' and a[0][2]=='X') or ( 
    # a[1][0]=='X' and a[1][1]=='X' and a[1][2]=='X') or (
    # a[2][0]=='X' and a[2][1]=='X' and a[2][2]=='X') or (
    # a[0][0]=='X' and a[1][0]=='X' and a[2][0]=='X') or (
    # a[0][1]=='X' and a[1][1]=='X' and a[2][1]=='X') or (
    # a[0][2]=='X' and a[1][2]=='X' and a[2][2]=='X') or (
    # a[0][0]=='X' and a[1][1]=='X' and a[2][2]=='X') or (
    # a[0][2]=='X' and a[1][1]=='X' and a[2][0]=='X'):
    #     return True
#     else:
#         return False


# map = [[EMPTY for _ in range(3)] for _ in range (3)]
    
# printMap(map)

# while( O_is_winner(map) == False and X_is_winner(map) == False):
        
#     print("X's Turn\nEnter your coordinates: ")
#     x = int(input())
#     y = int(input())

#     while x < 0 or y < 0 or x > 2 or y > 2 or map[x][y] != EMPTY or map[x][y] == 'O':
#         print("Invalid movement, try again:")
#         x = int(input())
#         y = int(input())
#     map[x][y] = 'X'
#     printMap(map)

#     if X_is_winner(map) == True:
#         print("The player X is the winner!!")
#         break

#     print("O's Turn\nEnter your coordinates: ")
#     x = int(input())
#     y = int(input())

#     while x < 0 or y < 0 or x > 2 or y > 2 or map[x][y] != EMPTY or map[x][y] == 'X':
#         print("Invalid move, try again")
#         x = int(input())
#         y = int(input())
#     map[x][y] = 'O'
#     printMap(map)

#     if O_is_winner(map) == True:
#         print("The player O is the winner!!")
#         break
