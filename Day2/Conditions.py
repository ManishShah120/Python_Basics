'''
is_hot=False
is_cold=False
if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Were Warm cloths")
else:
    print("Enjoy your day")
print("It's a Lovely Day")
'''

#Exercise
price_house=1000000
good_credit=True
if good_credit:
    down_payment=0.1*price_house
else:
    down_payment=0.2*price_house
#print("Down Payment: $" + str(down_payment))
print(f"Down Payment: ${down_payment}")