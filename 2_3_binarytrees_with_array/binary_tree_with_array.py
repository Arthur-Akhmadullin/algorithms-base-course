class aBST:

    def __init__(self, depth):
        # правильно рассчитайте размер массива для дерева глубины depth:
        tree_size = 2**(depth+1) - 1
        self.Tree = [None] * tree_size # массив ключей

    def FindKeyIndex(self, key):
        # ищем в массиве индекс ключа
        return self._FindKeyIndex(0, key)


    def AddKey(self, key):
        # добавляем ключ в массив
        resultOfFind = self.FindKeyIndex(key)
        if resultOfFind is None:
            return -1
        if resultOfFind < 0:
            return self._AddKey(-1 * resultOfFind, key)
            # index = -1 * resultOfFind
            # self.Tree[index] = key
            # return index
        elif resultOfFind == 0:
            if self.Tree[0] == key:
                return 0
            else:
                return self._AddKey(0, key)
        else:
            return resultOfFind
        # индекс добавленного/существующего ключа или -1 если не удалось


    def parent(self, i):
        return (i - 1) / 2


    def left(self, i):
        return 2 * i + 1


    def rigth(self, i):
        return 2 * i + 2


    def _FindKeyIndex(self, i, key):
        if i < len(self.Tree):
            if self.Tree[i] == key:
                return i
            elif self.Tree[i] == None:
                return i*(-1)
            elif key < self.Tree[i]:
                return self._FindKeyIndex(self.left(i), key)
            elif key > self.Tree[i]:
                return self._FindKeyIndex(self.rigth(i), key)
        else:
            return None

    def _AddKey(self, i, key):
        self.Tree[i] = key
        return i