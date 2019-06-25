# наследуйте этот класс от HashTable
# или расширьте его методами из HashTable
from HashTable import HashTable

class PowerSet(HashTable):

    def __init__(self):
        HashTable.__init__(self, 20, 1)
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
            return True
        return False

        # Или же бросить исключение. Посмотреть, как правильно делается

        # возвращает True если value удалено
        # иначе False


    def intersection(self, set2):
        # пересечение текущего множества и set2
        return None

    def union(self, set2):
        # объединение текущего множества и set2
        return None

    def difference(self, set2):
        # разница текущего множества и set2
        return None

    def issubset(self, set2):
        # возвращает True, если set2 есть
        # подмножество текущего множества,
        # иначе False
        return False