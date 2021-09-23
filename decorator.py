def div(a,b):
    print(a/b)


def deco_div(func):

    def inner(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)

    return inner


div1 = deco_div(div)
div1(2, 4)

