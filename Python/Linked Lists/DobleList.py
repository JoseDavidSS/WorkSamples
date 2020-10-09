from Node import Node

class DobleList:
    def __init__ (self):
        self.head = None # First DobleList node
        self.tail = None # Last DobleList node
        self.length = 0 # DobleList length

    # Output: DobleList length.
    # Restriction: length must be a whole number.
    def __len__ (self):
        return self.length

    # Input: A whole number.
    # Output: Append node to the end of the DobleList and replace tail node from DobleList.
    # Restriction: value must be a whole number.
    def appendValue(self, value):
     if isinstance (value, int):
         self.length += 1
         if self.head == None:
             self.head = Node(value)
             self.tail = self.head
         else:
             node = self.head
             while node.next != None:
                 node = node.next
             node.next = Node(value)
             node.next.prev = node
             self.tail = node.next
     else:
         print("Error")

    # Output: DobleList view as a Python list.
    # Restriction: must be equal to a Python list to the eye.
    def printAsPythonList (self):
        node = self.head
        txt = "["
        while node != None:
            txt += node.__str__()
            if node.next != None:
                txt += ", "
            node = node.next
        print(txt + "]")

    # Output: DobleList in reverse view as a Python list.
    # Restriction: must be equal to a reverse Python list to the eye.
    def reverseListAsPythonList (self):
        node = self.tail
        txt = "["
        while node != None:
            txt += node.__str__()
            if node.prev != None:
                txt += ", "
            node = node.prev
        print(txt + "]")

    # Output: Python list with DobleList nodes values.
    # Restriction: must return a Python list.
    def convertDobleListToPythonList():
        node = self.head
        list1 = []
        while node != None:
            list1.append(node.__int__())
            node = node.next
        return list1

    # Input: A whole number.
    # Output: DobleList without nodes having the same value as the value input
    # Restriction: DobleList must be not null and value input must be whole number.
    def deleteNodeByValue(self, value):
        if isinstance(value, int) and self.head != None:
            if self.head.__int__() == value:
                if self.head.next == None:
                    self.length -= 1
                    self.head = None
                    self.tail = None
                else:
                    self.length -= 1
                    self.head = self.head.next
                    self.head.prev = None
            elif self.tail.__int__() == value:
                self.length -= 1
                self.tail = self.tail.prev
                self.tail.next = None
            else:
                node = self.head
                while node.next != None:
                    if node.__int__() == value:
                        node.prev.next = node.next
                        node.next.prev = node.prev
                        break
                    else:
                        node = node.next
        else:
            print("Error")
                        



















        
