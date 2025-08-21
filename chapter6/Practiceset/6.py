Marks=int(input("Enter Your Marks:"))

if((Marks>89) and (Marks<101)):
    Grade="Ex"
elif((Marks>79) and (Marks<91)):
    Grade="A"
elif((Marks>69) and (Marks<81)):
    Grade="B"
elif((Marks>59) and (Marks<71)):
    Grade="C"
elif((Marks>49) and (Marks<61)):
    Grade="D"
else:
    Grade="F"

print(f"Your Grade Is {Grade}")