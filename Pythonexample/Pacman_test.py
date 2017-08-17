import os
import time

delay = float((input("Delay? :")))
os.system('cls')
print("Happy")
for i in range(1, 4):
    time.sleep(delay)
    os.system('cls')
    print("%d sec" % int(i))
time.sleep(delay)
print("END")
os.system('cls')


def BackGround():
    BGmatrix = []
    MatrixRow = []
    for i in range(0, 20):
        for j in range(0, 50):
            MatrixRow.append("⃞")
        BGmatrix.append(MatrixRow)
        MatrixRow = []
    return BGmatrix


def draw(Matrix_todraw):
    for i in range(0, len(Matrix_todraw)):
        for j in range(0, len(Matrix_todraw[0])):
            print(Matrix_todraw[i][j], end="")
        print(" ")


def PacMan(row, column, Matrix):
    for i in range(row - 2, row + 2):
        for j in range(column - 2, column + 2):
            Matrix[i][j] = '0'
    return Matrix


draw(BackGround())
time.sleep(delay)
os.system('cls')

'''
while 1:
    Current
    draw(PacMan(10, 25, BackGround()))
    print("\n\n\n\n")
    Useract =


'''