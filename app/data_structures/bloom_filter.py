import math 
import array
import mmh3

class BloomFilter:
    def __init__(self, num_items: int , false_positive_prob: float):
        m = -(num_items * math.log(false_positive_prob)) / (math.log(2) ** 2)
        self.size = int(m)
        
        # Calculate optimal number of hash functions (k)
        k = (m / num_items) * math.log(2)
        self.num_hash_funcs = int(k)

        self.bit_array = array.array('B', [0]) * (int(self.size / 8) + 1)
    
    def add(self, item:str) -> None:
        
        for i in range(self.num_hash_funcs):
            # Generate hash using MurmurHash3 with different seeds
            hash_value = mmh3.hash(item, seed=i)
            index = hash_value % self.size
            
            # Set the bit at the calculated index
            self.bit_array[index // 8] |= 1 << (index % 8)

    
    def __contains__(self, item:str) -> bool:
        
        for i in range(self.num_hash_funcs):
            # Generate the same hash sequence as in add()
            hash_value = mmh3.hash(item, seed=i)
            index = hash_value % self.size
            
            # Check if the bit at this index is set
            if not (self.bit_array[index // 8] & (1 << (index % 8))):
                # If any bit is 0, item is definitely not in the set
                return False
        
        # All bits were 1, so item is probably in the set
        return True