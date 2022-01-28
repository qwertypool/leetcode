Find the maximum and minimum in an array using recursion:
  
  
  
  
def maxmin(arr,maxm,minm):
    if len(arr)==0:
        print("Maximum = ",maxm," Minimum = ",minm)
        return 
    maxm = max(arr[0],maxm)
    minm = min(arr[0],minm)
    maxmin(arr[1:],maxm,minm)
    
    
maxmin([1,5,44,12,-6,99,87],-9999,9999) 
