class chainingHashTable:
    def __init__(self, initial_capacity = 10):
        
        # Use list comprehension to create 'initial_capacity' empty lists
        self.table = [[] for _ in range(initial_capacity)]
            
    # def insert (self, key, item):
    #     bucket = hash(key) % len(self.table)
    #     bucket_list = self.table[bucket]
        
    #     for key in bucket_list:
    #         if key[0] == key:
    #             key[1] = item
    #             return True
    #     key_value = [key, item]
    #     bucket_list.append(key_value)
    #     return True
    
    def insert(self, key, item):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for entry in bucket_list:   # Changed 'key' to 'entry' to prevent conflict
            if entry[0] == key:
                entry[1] = item
                return True
        bucket_list.append([key, item])
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
                
    def printAll(self):
        # Create a list to store (original key, value) pairs
        sorted_entries = []
        
        for bucket in self.table:
            for keyValue in bucket:
                # Since all keys are hashes of integers, we will append a tuple containing
                # the original integer (which is the value of the key) and its corresponding value
                sorted_entries.append((keyValue[0], keyValue[1]))

        # Sort the list based on the original integer values
        sorted_entries.sort()

        # Print the sorted entries
        for entry in sorted_entries:
            print(f'{entry[1]}')


    def __repr__(self):
        entries = []
        for bucket in self.table:
            for keyValue in bucket:
                entries.append(f"{keyValue[0]}: {keyValue[1]}")
        return "{" + ", ".join(entries) + "}"

        