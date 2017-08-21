RowNum = int(input("Row: "))
ColumnNum = int(input("Column: "))
MatrixRow = []
MatrixColumn = []
for i in range(0, RowNum):
    for j in range(0, ColumnNum):
        MatrixColumn.append(j)
    MatrixRow.append(MatrixColumn)
    MatrixColumn = []
print(MatrixRow)
LineIndex = 0
j = 1
Max = ColumnNum *  RowNum
while 1:
    for i in range(LineIndex, ColumnNum-1-LineIndex):
        MatrixRow[LineIndex][i] = j
        j = j + 1
        if j > Max:
            break
    for i in range(LineIndex, RowNum-1-LineIndex):
        MatrixRow[i][ColumnNum-1-LineIndex] = j
        j = j + 1
        if j > Max:
            break
    for i in range(LineIndex+1, ColumnNum-LineIndex):
        MatrixRow[RowNum-1-LineIndex][ColumnNum-i] = j
        j = j + 1
        if j > Max:
            break
    for i in range(LineIndex+1, RowNum-LineIndex):
        MatrixRow[RowNum-i][LineIndex] = j
        j = j + 1
        if j >= Max:
            break
    LineIndex = LineIndex + 1
    if ColumnNum%2 == 1 and ColumnNum == RowNum:
        MatrixRow[(RowNum//2)][(ColumnNum//2)]=Max
        if j == Max:
            break
    if j > Max:
        break
for i in range(0, RowNum):
    for j in range (0, ColumnNum):
        print(MatrixRow[i][j], end=" ")
    print(" ")
