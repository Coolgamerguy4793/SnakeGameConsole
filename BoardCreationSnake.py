import random
import time
x_size = 65
y_size = 6
Board = []
Line1 = []
Line2 = []
Path = []
EndGame = 0
SnakePos = [7,5]
def createBoard():
    for i in range(x_size+x_size+1):
        Line1.append('-')
    for i in range(x_size):
        Line2.append("|")
        Line2.append(" ")
    Line2.append("|")
    for j in range(y_size):
        Board.append(Line1)
        Board.append(Line2)
        Path.append(f"{Line2}{j}")
    Board.append(Line1)
def printBoard():
    LineP = ""
    for i in range(len(Board)):
        for j in Board[i]:
            LineP += j
        print(LineP)
        """
        if i % 2 != 0:
            print(Board[i])
        else:
            pass
        """
        LineP = ""
    #print(Path)
def TestEnd(End):
    if End == 1:
        print("You Lost")
        quit()
    else:
        printBoard()
def ModifyBoard():
    SnakePos1 = SnakePos[0]
    SnakePos2 = SnakePos[1]
    if SnakePos[1] % 2 == 0:
        SnakePos[1] += 1
    elif SnakePos[1] == len(Board)-y_size:
        TestEnd(1)
    else:
        pass
    if SnakePos[0] % 2 == 0:
        SnakePos[0] += 1
    elif SnakePos[0] == len(Board[1]):
        TestEnd(1)
    else:
        pass
    Board[SnakePos[0]][SnakePos[1]] = "X"
    printBoard()
#def MoveSnake(Direction):
#    if Direction == "Up":
#        SnakePos[]
createBoard()
ModifyBoard()
#MoveSnake("Up")