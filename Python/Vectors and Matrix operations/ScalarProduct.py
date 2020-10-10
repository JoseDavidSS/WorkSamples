# Input: two vectors.
# Output: ordered list.
# Restrictions: input vectors must be the same size, inputs must be type list and list must be not empty.
def scalingProduct (vector1, vector2):
      vector1Length = len (vector1)
      vector2Length = len (vector2)
      if isinstance (vector1, list) and isinstance (vector2, list) and vector1Length == vector2Length:
            return scalingProductAux (vector1, vector2, vector1Length, 0, 0)
      else:
            return "Error, must check input values or restrictions"

def scalingProductAux (vector1, vector2, vectorLength, vectorIndex, resultVector):
      if vectorLength == vectorIndex:
            return resultVector
      else:
            productResult = vector1[vectorIndex] * vector2[vectorIndex]
            return scalingProductAux (vector1, vector2, vectorLength, vectorIndex+1, resultVector+productResult)

alist = [54,26,93]
blist = [10,100,1000]
print(scalingProduct(alist,blist))
