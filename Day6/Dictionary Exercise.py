Phone  = input("Phone: ")
Numbers = {
    "1":"One ",
    "2":"Two ",
    "3": "Three ",
    "4": "Four ",
    "5": "Five ",
    "6": "Six ",
    "7": "Seven ",
    "8": "Eight ",
    "9": "Nine ",
    "0": "Zero "
}
output = ""
for i in Phone:
    output += Numbers.get(i)
print(output)
