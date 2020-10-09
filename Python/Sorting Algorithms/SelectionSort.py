# Input: disordered list.
# Output: ordered list.
# Restrictions: input must be a list and list must be not empty.
def selectionSort(list1):
    listLength = len(list1)
    
    for index in range(listLength-1):
        minValue = index # We first assume that the first element is the lowest.
        
        for auxIndex in range(index+1, listLength-1): # We then use auxIndex to loop through the remaining elements.
            if list1[auxIndex] < list1[minValue]: # Update the minValue if the element at auxIndex is lower than it.
                minValue = auxIndex
        
        list1[index], list1[minValue] = list1[minValue], list1[index] # After finding the lowest item of the unsorted regions, swap with the first unsorted item.
    return list1

alist = [54,26,93,17,77,31,44,55,20]
print(selectionSort(alist))
