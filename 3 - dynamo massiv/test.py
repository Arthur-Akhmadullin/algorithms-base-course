from dynarray import DynArray

da = DynArray()
for i in range(8):
    da.append(i)
    print (da[i])
print("---------")
print("Count", da.count)
print("Capacity", da.capacity)
print("---------")
da.insert(5,77)
for i in range(da.__len__()):
    print(da[i])
print("---------")
print("Count", da.count)
print("Capacity", da.capacity)
print("---------")

da.delete(4)
for i in range(da.__len__()):
    print(da[i])
print("---------")
print("Count", da.count)
print("Capacity", da.capacity)
print("---------")

print("---------")
da.insert(5,78)
for i in range(da.__len__()):
    print(da[i])
print("---------")
print("Count", da.count)
print("Capacity", da.capacity)
print("---------")

print("---------")
da.insert(3,555)
for i in range(da.__len__()):
    print(da[i])
print("---------")
print("Count", da.count)
print("Capacity", da.capacity)
print("---------")

print("---------")
da.insert(4, 222)
for i in range(da.__len__()):
    print(da[i])
print("---------")
print("Count", da.count)
print("Capacity", da.capacity)
print("---------")