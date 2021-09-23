def person(name, **data):
    print(name)
    for k, v in data.items():
        print(k, v)


person('bhargav', age=25, city='anantapur', cell=8309858929)
