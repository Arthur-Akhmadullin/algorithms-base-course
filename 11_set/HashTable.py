class HashTable:
    def __init__(self, sz, stp):
        self.size_slots = sz
        self.step = stp
        self.slots = [None] * self.size_slots


    def hash_fun(self, value):
        b = bytearray(str(value).encode('utf-8'))
        sum = 0
        for i in range(len(b)):
            sum += b[i]
        return sum % self.size_slots


    def seek_slot(self, value):
        hash_index = self.hash_fun(value)

        count_full_slots = 0
        while True:
            if count_full_slots == self.size_slots:
                return None
            elif self.slots[hash_index] == None:
                return hash_index
            else:
                count_full_slots += 1
                hash_index = (hash_index + self.step) % self.size_slots


    def put(self, value):
        position = self.seek_slot(value)

        if position == None:
            return None
        else:
            self.slots[position] = value
            return position
        # записываем значение по хэш-функции

        # возвращается индекс слота или None,
        # если из-за коллизий элемент не удаётся
        # разместить


    def find(self, value):
        '''
        for i in range(len(self.slots)):
            if self.slots[i] == value:
                return i
        # находит индекс слота со значением, или None
        return None
        '''

        startslot = self.hash_fun(value)

        find_pos = startslot
        while self.slots[find_pos] != None:
            if self.slots[find_pos] == value:
                return find_pos
            else:
                find_pos = (find_pos + self.step) % self.size_slots
                if find_pos == startslot:
                    return None