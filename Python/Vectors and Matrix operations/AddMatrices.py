# Input: matrixA, matrixB.
# Output: matrixA + matrixB.
# Restrictions: A, B must be the same size.
def addMatrices (matrixA, matrixB):
      rowsQuantity = len(matrixA)
      columnsQuantity = len(matrixA[0])
      
      if rowsQuantity == len(matrixB) and columnsQuantity == len (matrixB[0]):
            return addMatricesAux(matrixA, matrixB, rowsQuantity, columnsQuantity, 0, 0, [], [])
      else:
            return "Matrices given are not the same size"

def addMatricesAux (matrixA, matrixB, rowsQuantity, columnsQuantity, rowIndex, columnIndex, vec, matrixAB):
    
      if rowIndex == rowsQuantity:
            return matrixAB
        
      elif columnIndex == columnsQuantity:
            matrixAB.append(vec)
            vec = []
            return addMatricesAux(matrixA, matrixB, rowsQuantity, columnsQuantity, rowIndex+1, 0, vec, matrixAB)
        
      else:
            vec.append (matrixA[rowIndex][columnIndex] + matrixB[rowIndex][columnIndex])
            return addMatricesAux(matrixA, matrixB, rowsQuantity, columnsQuantity, rowIndex, columnIndex+1, vec, matrixAB)

A = [[1, 2], [2, 3]]
B = [[20, 50], [70, 10]]
print(addMatrices(A,B))
