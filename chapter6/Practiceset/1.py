n1=int(input("Enter 1 Number:"))
n2=int(input("Enter 2 Number:"))
n3=int(input("Enter 3 Number:"))
n4=int(input("Enter 4 Number:"))

if(n1>n2 and n1>n3 and n1>n4):
    print(f"n1 is Greater,{n1}")

elif(n2>n1 and n2>n3 and n2>n4):
    print(f"n2 is Greater,{n1}")

elif(n3>n1 and n3>n2 and n3>n4):
    print(f"n3 is Greater,{n1}")

else:
    print(f"n4 is Greater,{n1}")