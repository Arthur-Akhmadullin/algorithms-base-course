class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        # from NativeCashe
        self.hits = [0] * self.size

    def hash_fun(self, key):
        b = bytearray(key.encode('utf-8'))
        sum = 0
        for i in range(len(b)):
            sum += b[i]
        return sum % self.size

    def is_key(self, key):
        if key in self.slots:
            return True
        else:
            return False
        # возвращает True если ключ имеется,
        # иначе False


    def put(self, key, value):
        slot = self.hash_fun(key)

        if self.slots[slot] == None:
            self.slots[slot] = key
            self.values[slot] = value

        else:
            if self.slots[slot] == key:
                self.values[slot] = value
            else:
                new_slot = (slot + 1) % self.size
                while self.slots[new_slot] != None and self.slots[new_slot] != key:
                    new_slot = (new_slot + 1) % self.size
                    if new_slot == slot:
                        break


                if self.slots[new_slot] == None:
                    self.slots[new_slot] = key
                    self.values[new_slot] = value
                    self.hits[slot] += 1 #add
                elif self.slots[new_slot] == key:
                    self.values[new_slot] = value
                    self.hits[slot] += 1 #add
                else:
                    min_key_slot = self.hits.index(min(self.hits))
                    self.slots(min_key_slot) = key
                    self.values(min_key_slot) = value


        # гарантированно записываем
        # значение value по ключу key

    def get(self, key):

        value = None
        if self.is_key(key) == True:
            slot = self.hash_fun(key)

            while self.slots[slot] != key:
                slot = (slot + 1) % self.size

            value = self.values[slot]
            self.hits[slot] += 1 #add

        return value
        # возвращает value для key,
        # или None если ключ не найден