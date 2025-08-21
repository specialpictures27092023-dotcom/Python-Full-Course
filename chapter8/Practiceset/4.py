def divisible5(n):
    if(n%5==0):
        return True
    return False

a=[12,5,10,32,45,34,2,3,3,23,2,345]
f=list(filter(divisible5,a))

print(f)