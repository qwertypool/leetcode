1. Sum triangle from array
Given an array of integers, print a sum triangle from it such that the first level has all array elements. From then, at each level number of elements is one less than the previous level and elements at the level is be the Sum of consecutive two elements in the previous level. 
Example :
 

Input : A = {1, 2, 3, 4, 5}
Output : [48]
         [20, 28] 
         [8, 12, 16] 
         [3, 5, 7, 9] 
         [1, 2, 3, 4, 5] 

Explanation :
Here,   [48]
        [20, 28] -->(20 + 28 = 48)
        [8, 12, 16] -->(8 + 12 = 20, 12 + 16 = 28)
        [3, 5, 7, 9] -->(3 + 5 = 8, 5 + 7 = 12, 7 + 9 = 16)
        [1, 2, 3, 4, 5] -->(1 + 2 = 3, 2 + 3 = 5, 3 + 4 = 7, 4 + 5 = 9)
        
# 1. Recursive Approach:
# Python3 program to create Special triangle.
# Function to generate Special Triangle.
def printTriangle(A):
           
        # Base case
        if (len(A) < 1):
            return
   
        # Creating new array which contains the
        # Sum of consecutive elements in
        # the array passes as parameter.
        temp = [0] * (len(A) - 1)
        for i in range( 0, len(A) - 1):
           
            x = A[i] + A[i + 1]
            temp[i] = x
           
   
        # Make a recursive call and pass
        # the newly created array
        printTriangle(temp)
           
        # Print current array in the end so
        # that smaller arrays are printed first
        print(A)
       
   
# Driver function
A = [ 1, 2, 3, 4, 5 ]
printTriangle(A)

================================================================
================================================================
# Iterative Approach:
def triange(arr):
    ans = []
    ls = arr
    ans.append(arr)
    for i in range(len(arr)-1):
        ls1 = []
        i = 0
        while(i < len(ls)-1):
            s = ls[i] + ls[i+1]
            i += 1
            ls1.append(s)
        ls = ls1
        ans.append(ls)
    return ans
    

a = triange([1,2,3,4,5])
for i in a[::-1]:
    print(i)
