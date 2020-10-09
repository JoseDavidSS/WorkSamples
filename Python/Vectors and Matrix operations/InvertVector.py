# Input: matrixA, matrixB.
# Output: matrixA + matrixB.
# Restrictions: A, B must be the same size.
def invertVector (vector):
      if isinstance (vector, list):
            vectorSize = len(vector)
            return invertVectorAux (vector, vectorSize, [])
      else:
            return "error"
      
def invertVectorAux (vector, vectorIndex, invertedVector):
      if vectorIndex == 0:
            return invertedVector
      else:
            vectorIndex = vectorIndex-1
            invertedVector.append(vector[vectorIndex])
            return invertVectorAux (vector, vectorIndex, invertedVector)
        
A = [1,3,5,7,8,9]
print(invertVector(A))
