# Goldbach: Any even number greater than 2 can be written as the sum of two prime numbers.
# Input: An even number (n).
# Output: Two prime numbers that their sum is equal to the input even number.
# Restrictions: Input must be an even numbe, int and grater than 2. This program is unstable due to its recursion process meaning large numbers may crash the program.

import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(3000)

def goldbachConjecture(n):
    if not isinstance(n, int) or n<2: #Validate restrictions
        return "Number (n) must be whole and grater or equal than 2"

    elif n%2 == 1:
        return "Number (n) must be even"

    else:
        totalPrime = primeQuantity(2, n, []) # Stores all prime numbers between 2 and input number (n)
        result = compare(totalPrime, totalPrime[1:], [], n)
        return result

def primeQuantity(A, B, primeList):
    if A == B:
        return primeList
    
    else:
        if primeValidation(A, 2, 0) == 0: 
            primeList.append(A)
            return primeQuantity(A+1, B, primeList)
        
        else:
            return primeQuantity(A+1, B, primeList)      

def primeValidation(number, dividers, dividersQuantity): #Searchs for prime numbers between 2 and number input (n).
    if number == dividers:
        return dividersQuantity
    
    else:
        if number % dividers == 0:
            return primeValidation(number, dividers+1, dividersQuantity+1)
        
        else:
            return primeValidation(number, dividers+1, dividersQuantity)

def compare(list1, list1Copy, result, number):
    if list1 == []:
        return tuple(result)
    
    else:
        if list1Copy == []:
            return compare(list1[1:], list1[1:], result, number)
        
        elif list1[0] + list1Copy[0] == number: #If the sum of both elements of each list is equal to the number, it will return those elements in a tuple. 
            result.append(list1[0])
            result.append(list1Copy[0])
            return tuple(result)
        
        else:
            return compare(list1, list1Copy[1:], result, number)  



        
