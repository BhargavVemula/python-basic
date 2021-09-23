from numpy import *

arr1 = array([[10,20,30,40,50],
[11,22,33,44,55]])

m1 = arr1.flatten()
m2 = arr1.reshape(5,2)
print(arr1)
print(m1)
print(m2)
print(max(m1))
print(min(m1))

ar3 = matrix('1,2,3 ;4,5,6; 7,8,9')

m2 = ar3 * ar3
s1 = ar3 + ar3
print(m2)
print(ar3)
print(s1)
