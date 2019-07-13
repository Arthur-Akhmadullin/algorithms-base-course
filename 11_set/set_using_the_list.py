class PowerSet():
    def __init__(self):
        self.powerset = []
        # ваша реализация хранилища


    def size(self):
        return len(self.powerset)
        # количество элементов в множестве


    def put(self, value):
        if self.get(value) is False:
            self.powerset.append(value)
        else:
            return None
        #всегда срабатывает


    def get(self, value):
        if value in self.powerset:
            return True
        else:
            return False
        # возвращает True если value имеется в множестве,
        # иначе False


    def remove(self, value):
        if self.get(value):
            self.powerset.remove(value)
            return True
        return False
        # возвращает True если value удалено
        # иначе False


    def intersection(self, set2):
        inter_set = PowerSet()
        for i in self.powerset:
            if set2.get(i) is True:
                inter_set.put(i)
        return inter_set


    def union(self, set2):
        union_set = PowerSet()
        union_set.powerset = self.powerset.copy()
        #for i in self.powerset:
            #union_set.put(i)
        for i in set2.powerset:
            union_set.put(i)
        return union_set


    def difference(self, set2):
        dif_set = PowerSet()
        dif_set.powerset = self.powerset.copy()
        for i in set2.powerset:
            dif_set.remove(i)
            if dif_set.size() == 0:
                break
        '''
        for i in self.powerset:            
            if not set2.get(i):
                dif_set.put(i)
        '''
        return dif_set
        # разница текущего множества и set2


    def issubset(self, set2):
        flag = True
        if set2.size() > self.size():
            flag = False
        elif set2.size() == 0:
            flag = True
        else:
            for i in set2.powerset:
                if self.get(i) is False:
                    flag = False
                    break
        return flag
        # возвращает True, если set2 есть
        # подмножество текущего множества,
        # иначе False