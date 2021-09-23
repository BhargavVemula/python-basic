a = 10


def something():
    a = 8
    x = globals()['a']
    globals()['a'] = 10
    print("local variable", a)


something()
print("outside",a)
