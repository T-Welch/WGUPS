class chainingHashTable:
    def __init__(self, initial_capacity = 10):
        
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])
            
    def insert (self, key, item):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        
        for key in bucket_list:
            if key[0] == key:
                key[1] = item
                return True
        key_value = [key, item]
        bucket_list.append(key_value)
        return True
    
    def search(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        
        for keyValue in bucket_list:
            if keyValue[0] == key:
                return keyValue[1]
        return None
    
    def remove(self,key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        
        for keyValue in bucket_list:
            if keyValue[0] == key:
                bucket_list.remove([keyValue[0],keyValue[1]])
                
    # def __repr__(self):
        