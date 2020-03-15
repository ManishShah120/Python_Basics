weight=float(input("Weight: "))
choice=input("(K)g or (L)bs:")
if choice.upper()=='L':
    result=weight/2.20562
    print(f"You are {result}Kg")
else:
    result=weight*2.20462
    print(f"You are {result}Pounds")