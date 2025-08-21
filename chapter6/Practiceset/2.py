a=int(input("Enter 1 Marks:"))
b=int(input("Enter 2 Marks:"))
c=int(input("Enter 3 Marks:"))

T=int(a+b+c)
Total=T/3

if(a>32 and b>32 and c>32 and Total>39):
    print(f"Pass,{a,b,c,Total}")

else:
    print(f"Fail {a,b,c,Total}")
