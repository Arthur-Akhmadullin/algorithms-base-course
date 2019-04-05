from dynarray import DynArray

da = DynArray()
for i in range(5):
    da.append(i)
    print (da[i])
print("---------")
print("Count", da.count)
print("Capacity", da.capacity)

'''
print("---------")
print("Вставка мимо массива")
da.insert(-1, 77)
'''

print("---------")
print("Вставка внутри массива, когда размер буфера не превышен")
da.insert(0, 777)
for i in range(da.__len__()):
    print(da[i])
print("---------")
print("Count", da.count)
print("Capacity", da.capacity)


print("---------")
print("Повторим вставку")
da.insert(5, 888)
da.insert(5, 999)
for i in range(da.__len__()):
    print(da[i])
print("---------")
print("Count", da.count)
print("Capacity", da.capacity)


print("---------")
print("Вставка, когда размер буфера превышен")
da.insert(7, 1111)
for i in range(da.__len__()):
    print(da[i])
print("---------")
print("Count", da.count)
print("Capacity", da.capacity)


'''
print("---------")
print("Удаление за пределами массива")
da.delete(6)
'''

'''
print("---------")
print("Удаление, когда размер буфера остается прежним")
da.delete(3)
for i in range(da.__len__()):
    print(da[i])
print("---------")
print("Count", da.count)
print("Capacity", da.capacity)
'''

'''
print("---------")
print("Удаление, когда размер буфера уменьшается")
da.insert(2, 5)
da.insert(2, 55)
da.insert(2, 5555)
da.insert(2, 55555)
da.insert(2, 555555)
da.insert(2, 5555555)
da.insert(2, 55555555)
for i in range(da.__len__()):
    print(da[i])
print("---------")
print("Count", da.count)
print("Capacity", da.capacity)
print("---------")
da.delete(3)
da.delete(3)
da.delete(3)
da.delete(3)
da.delete(3)
for i in range(da.__len__()):
    print(da[i])
print("---------")
print("Count", da.count)
print("Capacity", da.capacity)
da.delete(4)
for i in range(da.__len__()):
    print(da[i])
print("---------")
print("Count", da.count)
print("Capacity", da.capacity)
'''