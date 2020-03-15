'''
temp=int(input("Enter temperature in Celcius:"))
if temp>=30:
    print("It's A hot Day")
elif temp<10:
    print("It's A cold Day")
else:
    print("It's Neither hot nor Cold")
'''
name=input("Enter your name: ")
print(len(name))
if len(name)<=3:
    print("Name must be atleast 3 characters")
elif len(name)>=50:
    print("Name can be maximum of 50 characters long")
else:
    print("Name looks good")