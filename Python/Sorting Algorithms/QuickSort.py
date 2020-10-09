# Input: disordered list.
# Output: ordered list.
# Restrictions: input must be a list and list must be not empty.
def quickSort(list1):
    less = []
    equal = []
    greater = []

    listLength = len(list1)

    if listLength > 1:
        pivot = list1[0]
        
        for index in list1:
            if index < pivot:
                less.append(index)
                
            elif index == pivot:
                equal.append(index)
                
            elif index > pivot:
                greater.append(index)
                
        return quickSort(less) + equal + quickSort(greater) # Just use the + operator to join lists.
    
    else: # You need to handle the part at the end of the recursion - when you only have one element in your array, just return the array.
        return list1

alist = [54,26,93,17,77,31,44,55,20]
print(quickSort(alist))
