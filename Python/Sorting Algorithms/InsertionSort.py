# Input: disordered list.
# Output: ordered list.
# Restrictions: input must be a list and list must be not empty.
def insertionSort(list1):
    if isinstance(list1, list) and len(list1) > 1:
        return insertionSortAux(list1)
    else:
        return print("Error")

def insertionSortAux(list1):
    listLength = len(list1)
    for index in range(1, listLength):
        
        currentValue = list1[index] # Used as a key.
        position = index # So the index won't be modificated.

        while position > 0 and list1[position-1] > currentValue:
            list1[position] = list1[position-1]
            position = position-1

        list1[position] = currentValue
    print(list1)

alist = [54,26,93,17,77,31,44,55,20]
insertionSort(alist)
