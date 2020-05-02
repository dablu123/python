from numpy import *

arr= array([9,2,5,6])

arr2= arr.view()

print(sort(arr))

arr2[1]=25
print(arr2)