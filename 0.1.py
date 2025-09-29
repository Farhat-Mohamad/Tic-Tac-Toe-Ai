map = [[EMPTY for _ in range(9)] for _ in range (9)]


def printMap(a):
    for i in range(9):
        cell = " | ".join(a[i])
        print (cell)