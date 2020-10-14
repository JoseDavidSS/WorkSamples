# Input: list with numbers.
# Output: boolean value, true if halfs are equal or false if not.
# Restrictions: list must be type list and not empty.

def equivalentHalfs (list1):
    if not isinstance (list1, list) and list1 != []:
        return "List must be type list and must be not empty"
    
    half1 = 0
    half2 = 0
    length = len(list1)
    
    for index in range (0, length):
          
        if index != length // 2:
            half1 += list1[index]
            half2 += list1[length - 1 - index]
        else:
            return half1 == half2

print(equivalentHalfs([10, 20, 30, 15, 15, 32]))
