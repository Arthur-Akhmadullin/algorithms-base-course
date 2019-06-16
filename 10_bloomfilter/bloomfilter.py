from BitVector import BitVector

class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.bloom_filter = BitVector(intVal=0, size=self.filter_len)
        #print(self.bloom_filter)


    def hash1(self, str1):
        # 17
        sum = 0
        for c in str1:
            code = ord(c)
            sum *= 17
            sum += code
        return sum % self.filter_len


    def hash2(self, str1):
        # 223
        sum = 0
        for c in str1:
            code = ord(c)
            sum *= 223
            sum += code
        return sum % self.filter_len


    def add(self, str1):
        slot_first = self.hash1(str1)
        slot_second = self.hash2(str1)
        self.bloom_filter[slot_first] = 1
        self.bloom_filter[slot_second] = 1
        #print(self.bloom_filter)
        #print(slot_first, slot_second)


    def is_value(self, str1):
        flag = False
        slot_first = self.hash1(str1)
        slot_second = self.hash2(str1)
        if self.bloom_filter[slot_first] == 1 and self.bloom_filter[slot_second] == 1:
            flag = True
        return flag
        # проверка, имеется ли строка str1 в фильтре