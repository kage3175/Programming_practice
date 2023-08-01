lst = [[(1,1)], [(1,2), (1,3), (1,4)], [(5,6)]]
temp = []
for cluster in lst:
    print(cluster)
    temp.append(cluster)

for cluster in temp:
    lst.remove(cluster)

print(1,lst)