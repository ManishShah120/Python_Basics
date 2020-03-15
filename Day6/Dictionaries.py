'''
Dictionaries in Python is similar to STRUCTURE in C
Dictionaries contains
Dictionary = {"KEY":"Values",}
'''
Customer = {
    "Name":"Manish",
    "Age":21,
    "Gender":"Male",
    "Is_Verified": True
}
#print(Customer.get("name"))#None is an object with no value
Customer["Name"] = "Kumar"
print(Customer.get("Birthdate","Oct 14 1999"))
print(Customer["Name"])
Customer["Country"] = "India"
print(Customer["Country"])











