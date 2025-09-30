import random
EMPTY = ' '

map = [[EMPTY for _ in range(9)] for _ in range (9)]

def printMap(a):
    for i in range(9):
        cell = " | ".join(a[i])
        print (cell)
    print("\n")

def box1_winner(a, player):
    for i in range(3):
        if (a[i][0] == a[i][1] == a[i][2] == player) or (
        a[0][i] == a[1][i] == a[2][i] == player ) or (
        a[0][0] == a[1][1] == a[2][2] == player) or (
        a[0][2] == a[1][1] == a[2][0] == player):
            return True
    return False
#kamen 3m yotba3 l map 3 marrat lamma ykoun fi case enno small box winner, lezem bs marten
def box4_winner(a, player):
    for i in range(3,6):
            if (a[i][0] == a[i][1] == a[i][2] == player) or (
            a[3][0] == a[4][0] == a[5][0] == player ) or (
            a[3][1] == a[4][1] == a[5][1] == player ) or (
            a[3][2] == a[4][2] == a[5][2] == player ) or (

            a[3][0] == a[4][1] == a[5][2] == player) or (
            a[5][0] == a[4][1] == a[3][2] == player):
                return True
    return False

def box7_winner(a, player):
    for i in range(6,9):
            if (a[i][0] == a[i][1] == a[i][2] == player) or (
            a[6][0] == a[7][0] == a[8][0] == player ) or (
            a[6][1] == a[7][1] == a[8][1] == player ) or (
            a[6][2] == a[7][2] == a[8][2] == player ) or (

            a[6][0] == a[7][1] == a[8][2] == player) or (
            a[8][0] == a[7][1] == a[6][2] == player):
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

def map_is_full(a):
    for i in range(9):
        for j in range(9):
            if a[i][j] == EMPTY:
                return False
    return True

def fill_small_box(a, player):
    if box1_winner(a, player):
        for i,j in get_box_cells(1):
            a[i][j] = player
        printMap(a)
    if box2_winner(a, player):
        for i, j in get_box_cells(2):
            a[i][j] = player
        printMap(a)
    if box3_winner(a, player):
        for i, j in get_box_cells(3):
            a[i][j] = player
        printMap(a)

    if box4_winner(a, player):
        for i, j in get_box_cells(4):
            a[i][j] = player
        printMap(a)

    if box5_winner(a, player):
        for i, j in get_box_cells(5):
            a[i][j] = player
        printMap(a)

    if box6_winner(a, player):
        for i, j in get_box_cells(6):
            a[i][j] = player
        printMap(a)

    if box7_winner(a, player):
        for i, j in get_box_cells(7):
            a[i][j] = player
        printMap(a)

    if box8_winner(a, player):
        for i, j in get_box_cells(8):
            a[i][j] = player
        printMap(a)

    if box9_winner(a, player):
        for i, j in get_box_cells(9):
            a[i][j] = player
        printMap(a)

def game_winner(a,player):
   if (box1_winner(a,player) and box2_winner(a,player) and box3_winner(a,player) ) or (
        box4_winner(a,player) and box5_winner(a,player) and box6_winner(a,player) ) or (
        box7_winner(a,player) and box8_winner(a,player) and box9_winner(a,player) ) or (
        box1_winner(a,player) and box4_winner(a,player) and box7_winner(a,player) ) or (
        box2_winner(a,player) and box5_winner(a,player) and box8_winner(a,player) ) or (
        box3_winner(a,player) and box6_winner(a,player) and box9_winner(a,player) ) or (
        box1_winner(a,player) and box5_winner(a,player) and box9_winner(a,player) ) or (
        box7_winner(a,player) and box5_winner(a,player) and box3_winner(a,player) ):
            return True
   return False

def boxes_number(a):
    label = 0
    for i in range(6,9):
        for j in range(9):
            if (j>= 6 and j<9):
                label = 9
            if (j>= 3 and j<6):
                label = 8
            if (j<3):
                label = 7
    for i in range(3,6):
        for j in range(9):
            if (j>= 6 and j<9):
                label = 6
            if (j>= 3 and j<6):
                label = 5
            if (j<3):
                label = 4
    for i in range(3):
        for j in range(9):
            if (j>= 6 and j<9):
                label = 3
            if (j>= 3 and j<6):
                label = 2
            if (j<3):
                label = 1    


def get_box_cells(label):
    first_i = ((label - 1) // 3) * 3 
    first_j = ((label - 1) %  3) * 3

    return [(i,j) for i in range(first_i, first_i + 3)
            for j in range(first_j, first_j + 3)]

def get_box_from_move(i, j):
    row_block = i // 3
    col_block = j // 3
    box_label = row_block * 3 + col_block + 1
    return box_label

def cell_number_in_box(i, j):
    row_in_box = i % 3
    col_in_box = j % 3
    return row_in_box * 3 + col_in_box + 1

def is_in_box(i, j, label):  # boolean value
    return (i, j) in get_box_cells(label)

def label_of_next_box(i_prev, j_prev):
    cell_num = cell_number_in_box(i_prev, j_prev)
    return cell_num

def valid_move(i,j, i_prev, j_prev,a):
    if a[i][j] != EMPTY:
        return False
    if not is_in_box(i, j, label_of_next_box(i_prev, j_prev)):
        return False
    if i>9 or i<0 or j>9 or j<9:
        return True
    return True

#the first to play within is randomly selected by the computer
x0 = random.randint(0,8)
y0 = random.randint(0,8)
print("Let's play!")
print("Start the game at box number: ", label_of_next_box(x0,y0) )

printMap(map)

while(1):
    print("X's turn, select a move: ")
    x1 = int(input())
    y1 = int(input())

    while valid_move(x1, y1, x0, y0, map):
        print("Invalid move, try again:")
        x1 = int(input())
        y1 = int(input())
    map[x1][y1] = "X"

    fill_small_box(map,"X")

    if(game_winner(map,"X")):
        print("Player X is the winner!!!")
        break
    printMap(map)

    if map_is_full(map):
        print("The game ended with a draw")
        break

    print("O's turn, do a move: ")
    x2 = int(input())
    y2 = int(input())

    while not valid_move(x2, y2, x1, y1, map):
        print("Invalid move, try again:")
        x2 = int(input())
        y2 = int(input())
    map[x2][y2] = "O"

    x0 = x2  ## new
    y0 = y2

    fill_small_box(map,"O")

    if(game_winner(map,"O")):
        print("Player O is the winner!!!")
        break

    printMap(map)

    if map_is_full(map):
        print("The game ended with a draw")
        break

