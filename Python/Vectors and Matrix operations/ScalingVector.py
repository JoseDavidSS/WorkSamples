# Input: number and vector.
# Output: scaled vector.
# Restrictions: input number must be integer, input vector must be a list and list must be not empty.
def scalingVector (number, vector):
      if isinstance (vector, list) and vector != None and vector != []:
            vectorLength = len(vector)
            return scalingVectorAux (number, vectorLength, vector, 0, [])
      else:
            return "Vector must be a list and must be not empty"

def scalingVectorAux (number, vectorLength, vector, vectorIndex, newVector):
      if vectorLength == vectorIndex:
            return newVector
      else:
            newVector.append (number*(vector[vectorIndex]))
            return scalingVectorAux (number, vectorLength, vector, vectorIndex+1, newVector)

alist = [54,26,93,17,77,31,44,55,20]
print(scalingVector(100,alist))
