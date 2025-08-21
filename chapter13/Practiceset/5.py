from functools import reduce
l=[12,5,10,32,45,34,2,3,3,23,2,345]

def greater(a,b):
    if(a>b):
        return a
    return b

print(reduce(greater,l))