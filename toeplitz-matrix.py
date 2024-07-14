
    
def checkDiagonal(startColumn,startRow, rows,cols,matrix):
    firstElement=matrix[startRow][startColumn]
    colIndex=startColumn
    for i in range(startRow,rows):
        if(colIndex>cols-1):
            break
        if(matrix[i][colIndex]!=firstElement):
            return False
        colIndex+=1
    return True
def isToeplitzMatrix(matrix): 
    rows=len(matrix)
    cols=len(matrix[0])
    for i in range(0,cols):
        if(not checkDiagonal(i,0,rows,cols,matrix)):
            return False
    for i in range(1,rows):
        if(not checkDiagonal(0,i,rows,cols,matrix)):
            return False
    return True

print(isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]])) #True


