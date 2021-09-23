from functools import reduce
lst = [1, 5, 20, 12, 32, 56, 45]

evens = list(filter(lambda n: n % 2 == 0, lst))

double = list(map(lambda n: n*2, evens))

sum = reduce(lambda a, b: a+b, double)
print(evens)
print(double)
print(sum)
eve = 'evening'
a = ','.join(eve)
print(a)
a = eve.split(',')
print(a)
s = 'aaa bbb ccc'
s1 = s.replace(' ', '')
print(s1)
