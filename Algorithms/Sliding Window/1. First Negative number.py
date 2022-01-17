Given a list of numbers, print all the first negative numbers in a window of size k.

A = [1, -2, -3, 5, 6, -7, 8, 9, 10]
Output = [-2, -2, -3, -7, -7, 0]

====================================================================================
# This is the problem of sliding window


from collections import deque
k = 3
A = [1, -2, -3, 5, 6, -7, 8, 9, 10]
n = len(A)

i = 0
j = 0
output = []
Q = deque([])

while j < n:
    
    if A[j] < 0:
        Q.append(A[j])
    
    if j - i + 1 < k:
        j += 1
    elif j - i + 1 == k:
        if len(Q) == 0:
            output.append(0)
        else:
            output.append(Q[0])
            if A[i] == Q[0]:
                Q.popleft()
        i += 1
        j += 1
            
print(output)
