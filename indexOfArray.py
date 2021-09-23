from array import *

n = int(input('enter length of an array'))
arr = array('i',[])
for i in range(n):
    x = int(input('enter next value'))
    arr.append(x)

print(arr)

val = int(input('enter value to search'))

k = 0
for e in arr:
    if e == val:
        print(k)

    k= k+1

a = arr.index(val)
print(a)
print(arr[1])
    
