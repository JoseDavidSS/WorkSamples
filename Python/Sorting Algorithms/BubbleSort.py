# Input: disordered list.
# Output: ordered list.
# Restrictions: input must be a list and list must be not empty.
def bubbleSort(list1):
    length = len(list1) - 1
    sorted = False # Flag to see if the list is sorted

    while not sorted:
        sorted = True
        for index in range(length):
            if list1[index] > list1[index+1]:
                sorted = False
                list1[index], list1[index+1] = list1[index+1], list1[index] # Change position between both positions in list1
    return list1

alist = [54,26,93,17,77,31,44,55,20]
print(bubbleSort(alist))
