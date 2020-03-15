a = [0,2,12,9,17,91]
large = a[0]
for i in range(0,6):
    if a[i] > large:
        large = a[i]
print(large)