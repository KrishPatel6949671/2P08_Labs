# ASSIGNMENT 01: ARRAYS
# An array is a special variable, which can hold more than one value at a time. Arrays are 
# the most commonly used data structure for many reasons.
# First, we look at the basics of how data is inserted, searched, and deleted from arrays. 
# Then, we look how the data can be stored in ascending (or descending) key order. This arrangement makes possible a fast way of searching for a data item: the binary search.

#Exercise 1: implement a function that iterates thourgh the array and prints every time in the array
def printArray(array):  
    print(array)
    
#Exercise 2: implement a function that returns number of items in the array
def getCount(array):
   return len(array)
   

#Exercise 3: implement a function that returns the value at index n
def getItem(array, index):
     return array[index]

#Exercise 4: implement a function that replaces an item at index n and return the array. return -1 if index is out of bound e.g., larger than the array size (do not use any python built-in function)
def replaceItem(array, index, item):
    if index > len(array)-1:
        return -1
    else:
        array[index] = item
    return array

#Exercise 5: implement a function that adds an item at the end of the list (do not use any python built-in function e.g. append)
def addItemAtEnd(array, item):
    length = len(array)
    newArray = [None] * (length+1)
    for i in range(0,length):
        newArray[i] = array[i]
    newArray[length] = item
    return newArray

#Exercise 6: implement a function that adds an item at index n and return the array, if n is larger than the size of the array, then insert the item at the end of the array (do not use any python array built-in function e.g. insert)
def addItem(array, index, item):
    length = len(array)
    newArray = [None] * (length+1)
    if index > length:
        newArray[length] = item

    for i in range(0,length+1):
        if i<index:
            newArray[i] = array[i]
        elif i==index:
            newArray[i]=item
        else:
            newArray[i] = array[i-1]
    return newArray

#Exercise 7: implement a function that returns the index of the (first) element with the specified value. Return -1 if the value was not found (do not use any python built-in function e.g. index)
def findIndex(array, item):
    for i in range(0,len(array)):
        if array[i] == item:
            return i        
    return -1

#Exercise 8: implement a function that deletes the first item with the specified value, return the array if value was found and deleted, -1 otherwise. (do not use any python built-in function)
def delete(array, item):             # Delete first occurrence
    newArray = [None] * (len(array)-1)
    for i in range(0,len(array)):
        if(array[i]==item):
            array[i] = None
            return array       
    return -1

#Exercise 9: implement a function that removes the element at the specified position. Default position value is -1, which returns the last item. The function returns removed value. (do not use any python built-in function)
def deleteAt(array, index= -1):
    if index==-1 or index>len(array)-1:
        item = array[len(array)-1]
        for i in range(0,len(array)-1):
            array[i] = array[i+1]
        return item
    else:
        item = array[index]
        for i in range(index,len(array)-1):
            array[i] = array[i+1]
        return item

#Exercise 10: implement a function that sorts the list in ascending order.(do not use any python built-in function)

def swap(array, j, k):# Swap the values at 2 indices
    if (0 <= j and j < len(array) and 0 <= k and k < len(array)): 
        array[j], array[k] = array[k], array[j]
         
#Exercise 10_1: implement a function that implement bubble sorting
#def bubbleSort(array):               # Sort comparing adjacent vals

            
#Exercise 10_2: implement a function that implement selection sorting
#def selectionSort(array):           # Sort by selecting min and 
    ## ADD YOUR CODE HERE

#Exercise 11: You are asked to improve the find_index function of Exercise 7. Assuming the array is sorted, implement binary search to returns the index of the (first) element with the specified value. Return -1 if the value was not found (do not use any python built-in function)
#def findSortedArray(array, item):             # Find index at or just below key
    ## ADD YOUR CODE HERE

