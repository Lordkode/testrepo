import hashlib
from math import log, ceil
class BloomFilter:
    def __init__(self, n, p):
        self.m = 16384 
        self.k = 11

        self.bit_array = [False]*self.m

    def _get_hashes(self, element):
        element_bytes = str(element).encode('utf-8')
        h = hashlib.sha512(element_bytes).digest()

        h_a = int.from_bytes(h[0:8], byteorder='big')
        h_b = int.from_bytes(h[8:16], byteorder='big')

        return h_a, h_b
    
    def add(self, element):
        h_a, h_b = self._get_hashes(element)
        m_mask = self.m - 1

        for i in range(self.k):
            index = (h_a + i*h_b) & m_mask
            self.bit_array[index] = True

    def check(self, element):
        h_a, h_b = self._get_hashes(element)
        m_mask = self.m - 1

        for i in range(self.k):
            index = (h_a + i*h_b) & m_mask
            if not self.bit_array[index]:
                return False
        return True
    
bf = BloomFilter(n=1000, p=0.001)

# Ajout d'éléments
bf.add("pomme")
bf.add("banane")
bf.add("cerise")

# Vérification 
print(bf.check("pomme"))
print(bf.check("orange"))
print(bf.check("banane"))
print(bf.check("ceris"))