List = [1,8,2,2,3,3,4,5,6,7]
print(List)
for i in List:
    if List.count(List[i]) > 1:
        List.remove(List[i])
List.sort()
print(List)