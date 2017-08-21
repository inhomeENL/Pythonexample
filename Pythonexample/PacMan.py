import os
import time
import msvcrt

delay = float((input("Delay?: ")))
os.system('cls')
print("Happy")
for i in range(1, 4):
    time.sleep(delay)
    os.system('cls')
    print("%d sec" % int(i))
time.sleep(delay)
print("END")
os.system('cls')
wide = int(input("Wide?: "))
high = int(input("High?: "))

def BackGround(wide, high):
    BGmatrix = []
    MatrixRow = []
    for i in range(0, high):
        for j in range(0, wide):
            MatrixRow.append("□")
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
            Matrix[i][j] = '■'
    return Matrix


draw(BackGround(wide, high))

time.sleep(delay)
os.system('cls')


draw(PacMan(int(wide/2), int(high/2), BackGround(wide, high)))
print("\n\n\n\n")
CurrentRow = int(wide/2)
CurrentColumn = int(high/2)
while 1:
	Useract = msvcrt.getwch()
	if Useract == 'w':
		if CurrentRow == 2:
			continue
		else:
			CurrentRow = CurrentRow - 1
	elif Useract == 's':
		if CurrentRow == wide-2:
			continue
		else:
			CurrentRow = CurrentRow + 1 
	elif Useract == 'a':
		if CurrentColumn == 2:
			continue
		else:
			CurrentColumn = CurrentColumn - 1
	elif Useract == 'd':
		if CurrentColumn == high-2:
			continue
		else:
			CurrentColumn = CurrentColumn + 1
	elif Useract == 'e':
		break
	else:
		continue
	time.sleep(delay/5)
	os.system('cls')
	draw(PacMan(CurrentRow, CurrentColumn, BackGround(wide, high)))
	print("\n\n\n\n")
	print(CurrentRow, CurrentColumn)

