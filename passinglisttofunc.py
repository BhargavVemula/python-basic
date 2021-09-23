lst = eval(input("enter name:"))


def count(lst):
    above = 0
    below = 0
    for i in lst:
        if len(i) > 5:
            above = above+1
        else:
            below = below+1
    return above, below


a, b = count(lst)
print("the length of name above 5 characters is:{} and below is {}".format(a, b))
