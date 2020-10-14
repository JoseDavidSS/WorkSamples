# Input: list with numbers.
# Output: last even element in input list.
# Restrictions: list must be type list and not empty.

def lastEvenValue (list1):
    if not isinstance (list1, list) and list1 != []:
        return "List must be type list and must be not empty"
    
    length = len(list1)
    lastEvenValue = 0
    
    for index in range (0, length):
        
        if index == length - 1:
            return lastEvenValue
        
        elif list1[index] % 2 == 0:
            lastEvenValue = list1[index]

print(lastEvenValue([10, 20, 30, 15, 15, 32]))
