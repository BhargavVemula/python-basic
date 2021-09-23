"positional"

def sum(name,age):
    print(name,"age is",age)

sum('bhargav',20)

"keyword"

def sum(name,age=18):
    print(name,"age is",age)

sum('bhargav',20)


def sum(*a):
    c = 0 
    for i in a:
        c= c+i
    print(c)

sum(10,20,30)

