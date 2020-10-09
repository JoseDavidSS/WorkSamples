class Node:
    def __init__ (self, value = None):
        self.next = None # Pointer attched to forward node.
        self.prev = None # Pointer attched to preview node.
        self.value = value # Pointer attched to next node.

    # Output: Node value as a string.
    # Restrictions: value must be a whole number so it can be transformed into a string type.
    def __str__ (self):
        return str(self.value)

    # Output: raw node value.
    # Restriction: value must be a whole number.
    def __int__ (self):
        return self.value

        
    
