def fact(n):
    if n == 0:
        print(1)
    else:
        f = 1
        for i in range(1, n+1):
            f = f*i

        return f


result = fact(5)
print(result)
