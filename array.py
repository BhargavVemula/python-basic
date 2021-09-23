from array import *

arr = array('I',[10,20,30,50,60])
for i in arr:
    print(i)
Narr = array(arr.typecode,[a**3 for a in arr])
print(Narr)