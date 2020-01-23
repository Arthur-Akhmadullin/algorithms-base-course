class Heap:

    def __init__(self):
        self.HeapArray = [] # хранит неотрицательные числа-ключи


    def MakeHeap(self, a, depth):
        # создаём массив кучи HeapArray из заданного
        # размер массива выбираем на основе глубины depth
        self.heapsize = 2**(depth+1) - 1
        if len(a) > self.heapsize:
            a = a[:self.heapsize]
        if len(a) > 0:
            for i in range(len(a)):
                self.HeapArray.append(a[i])
            for i in range((len(self.HeapArray))//2, -1, -1):
                self.HeapOrderingDown(i)
        #return self.HeapArray


    def GetMax(self):
        # вернуть значение корня и перестроить кучу
        if len(self.HeapArray) == 0:
            return -1 # если куча пуста
        else:
            max_elem = self.HeapArray.pop(0)
            self.HeapArray.insert(0, self.HeapArray.pop(len(self.HeapArray) - 1))
            self.HeapOrderingDown(0)
            return max_elem


    def Add(self, key):
        # добавляем новый элемент key в кучу и перестраиваем её
        if len(self.HeapArray) == self.heapsize:
            return False # если куча вся заполнена
        else:
            self.HeapArray.append(key)
            if len(self.HeapArray) > 1:
                self.HeapOrderingUp(len(self.HeapArray) - 1)
            return True



    def HeapOrderingDown(self, i):
        while i * 2 + 1 < len(self.HeapArray):
            i_left = i * 2 + 1
            i_right = i * 2 + 2
            i_large = i_left
            if i_right < len(self.HeapArray) and \
                    self.HeapArray[i_right] > self.HeapArray[i_left]:
                i_large = i_right
            if self.HeapArray[i] >= self.HeapArray[i_large]:
                break
            self.HeapArray[i], self.HeapArray[i_large] = \
                self.HeapArray[i_large], self.HeapArray[i]
            i = i_large


    def HeapOrderingUp(self, i):
        while self.HeapArray[i] > self.HeapArray[int((i - 1) / 2)]:
            self.HeapArray[i], self.HeapArray[int((i - 1) / 2)] = \
                self.HeapArray[int((i - 1) / 2)], self.HeapArray[i]
            i = int((i - 1) / 2)