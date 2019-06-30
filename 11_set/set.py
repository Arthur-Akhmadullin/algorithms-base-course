# наследуйте этот класс от HashTable
# или расширьте его методами из HashTable
from HashTable import HashTable

class PowerSet(HashTable):

    def __init__(self, size_set, step_set):
        HashTable.__init__(self, size_set, step_set)
        #self.slots = []
        # self.slots = [None] * 11 (размер массива)
        # ваша реализация хранилища

    def size(self):
        return len(self.slots)
        # количество элементов в множестве

    def put(self, value):
        position = self.seek_slot(value)

        if position == None:
            return None
        else:
            if self.find(value) == None:
                self.slots[position] = value
                return position
            else:
                return self.slots
                # Что должна возвращать переопределенная функция put?
                # Надо ли оставить последний else?

        '''
        if self.get(value) == True:
            return None
            # вместо return None надо бросить исключение
        else:
            self.slots.append(value)
        '''
        #всегда срабатывает

    def get(self, value):
        flag = True
        if self.find(value) == None:
            flag = False
        # возвращает True если value имеется в множестве,
        # иначе False
        return flag

    def remove(self, value):
        if self.find(value) != None:
            self.slots[self.find(value)] = None
            #del self.slots[self.find(value)]
            return True
        return False

        # Или же бросить исключение. Посмотреть, как правильно делается

        # возвращает True если value удалено
        # иначе False


    def intersection(self, set2):
        '''
        inter_set = []
        for i in self.slots:
            if i in set2:
                inter_set.append(i)
        # пересечение текущего множества и set2
        return inter_set
        '''
        inter_set = PowerSet(self.size(), 1)
        #inter_set = []
        for i in self.slots:
            if set2.get(i) is True and i is not None: # удалить ли сравнение с None?
                inter_set.put(i)
        return inter_set


    def union(self, set2):
        '''
        union_set = []
        for i in self.slots:
            if i != None:
                union_set.append(i)
        for i in set2:
            if i not in self.slots:
                union_set.append(i)
        # объединение текущего множества и set2
        return union_set
        '''
        union_set = PowerSet(self.size()+set2.size(), 1)
        for i in self.slots:
            union_set.put(i)
        for i in set2.slots:
            union_set.put(i)
        return union_set

    def difference(self, set2):
        #dif_set = []
        dif_set = PowerSet(self.size(), 1)
        for i in self.slots:
            if i not in set2.slots:
                #dif_set.append(i)
                dif_set.put(i)
        # разница текущего множества и set2
        return dif_set

    def issubset(self, set2):
        if set2.size() == 0:
            return False

        for i in set2.slots:
            if i not in self.slots:
                return False
        # возвращает True, если set2 есть
        # подмножество текущего множества,
        # иначе False
        return True