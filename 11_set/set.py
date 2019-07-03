# наследуйте этот класс от HashTable
# или расширьте его методами из HashTable
from HashTable import HashTable

class PowerSet(HashTable):
    def __init__(self, size_set=20, step_set=1):
        HashTable.__init__(self, size_set, step_set)
        self.powerset = []
        # ваша реализация хранилища


    def size(self):
        size = 0
        for i in self.slots:
            if i is not None:
                size += 1
        return size
        #return len(self.slots)
        # количество элементов в множестве


    def put(self, value):
        if value == None:
            return None
        if self.get(value) is True:
            return self.powerset

        position = self.seek_slot(value)

        if position == None:
            return None
        else:
            self.slots[position] = value
            self.powerset.append(value) #добавил это
            #return position
            return self.powerset
        #всегда срабатывает


    def get(self, value):
        flag = True
        if self.find(value) == None:
            flag = False
        return flag
        # возвращает True если value имеется в множестве,
        # иначе False


    def remove(self, value):
        if self.find(value) != None:
            self.slots[self.find(value)] = None
            self.powerset.remove(value)
            #del self.slots[self.find(value)]
            return True
        return False
        # возвращает True если value удалено
        # иначе False


    def intersection(self, set2):
        inter_set = PowerSet(min(self.size(), set2.size()), 1)
        inter_array = []
        for i in self.slots:
            if set2.get(i) is True and i is not None: # удалить ли сравнение с None?
                inter_set.put(i)
                inter_array.append(i)
        return inter_array

    '''
        inter_set = PowerSet(min(self.size(), set2.size()), 1)
        #inter_set = []
        for i in self.slots:
            if set2.get(i) is True and i is not None: # удалить ли сравнение с None?
                inter_set.put(i)
        return inter_set
    '''
    '''
        inter_array = []
        for i in self.slots:
            if set2.get(i) is True and i is not None:
                inter_array.append(i)
        inter_set = PowerSet(len(inter_array), 1)
        for i in inter_array:
            inter_set.put(i)
        return inter_set
    '''

    def union(self, set2):
        union_set = PowerSet(2*self.size_slots, 1)
        union_array = []
        for i in self.slots:
            if i is not None:
                union_set.put(i)
                union_array.append(i)
        for i in set2.slots:
            if i is not None:
                union_set.put(i)
                union_array.append(i)
        return union_array
    '''
        union_set = PowerSet(self.size()+set2.size(), 1)
        for i in self.slots:
            union_set.put(i)
        for i in set2.slots:
            union_set.put(i)
        return union_set
    '''



    def difference(self, set2):
        dif_set = PowerSet()
        dif_array = []
        for i in self.slots:
            if i is not None and set2.get(i) is False:
                dif_set.put(i)
                dif_array.append(i)
        return dif_array
        # разница текущего множества и set2


    def issubset(self, set2):
        if self.size() == 0 or set2.size() == 0:
            return False

        for i in set2.slots:
            if self.get(i) is False:
                return False
        # возвращает True, если set2 есть
        # подмножество текущего множества,
        # иначе False
        return True