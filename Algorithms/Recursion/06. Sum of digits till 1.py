Finding sum of digits of a number until sum becomes single digit
Input : 1234
Output : 1
Explanation : The sum of 1+2+3+4 = 10, 
              digSum(x) == 10
              Hence ans will be 1+0 = 1

Input : 5674
Output : 4 
  
=====================================================================

import math

def sod1(num):
    if int(math.log10(num))+1 == 1:
        return num
    s = 0
    while num!=0:
        d = num % 10
        s = s + d
        num = num // 10
    return sod1(s)
    
    
print(sod1(9999999))

=======================================================================
GOOOOOOOOD SOLUTION
=======================================================================
def digSum(n):
 
    if (n == 0):
        return 0
    if (n % 9 == 0):
        return 9
    else:
       return (n % 9)
 
# Driver program to test the above function
n = 9999
print(digSum(n))
 
# This code is contributed by
# Smitha Dinesh Semwal
