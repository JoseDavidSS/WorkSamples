# Input: list with numbers, number.
# Output: list as [greater than num, lower than num].
# Restrictions: list must be type list

def valuesQuantity (list1, number):
      if not isinstance (list1, list) and list:
            return "list must be type list, contain only numbers and must be not empty"
      
      graterQuantity = 0
      lowerQuantity = 0
      
      for index in list1:
            
            if index > number:
                  graterQuantity += 1
                  
            else:
                  lowerQuantity += 1
                  
      return [lowerQuantity, graterQuantity]

print(valuesQuantity([10, 30, 60], 50))
