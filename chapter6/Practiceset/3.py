p1="Make a lot of money"
p2="Buy now"

Message=input("Enter Message:")

##if(a==p1 or a==p2):
##   print("Spam Message")

if((p1 in Message) or (p2 in Message)):
    print("Spam")
else:
    print("You recieved a message")