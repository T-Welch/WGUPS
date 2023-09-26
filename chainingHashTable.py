class chainingHashTable:
    def __init__(self, initial_capacity = 10):
        
        self.table = [[] for _ in range(initial_capacity)]
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

    # I have to add these so I an access the packages using subscript notation which is my preference because it makes the code more readable in the truck class
    def __getitem__(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        for keyValue in bucket_list:
            if keyValue[0] == key:
                return keyValue[1]
        raise KeyError(f"{key} not found in the hash table")

    def __setitem__(self, key, value):
        self.insert(key, value)
    
    def __delitem__(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        for i, keyValue in enumerate(bucket_list):
            if keyValue[0] == key:
                del bucket_list[i]
                return
        raise KeyError(f"{key} not found in the hash table")
    def __iter__(self):
        for bucket in self.table:
            for item in bucket:
                yield item[1]
    def copy(self):
        copied_table = chainingHashTable(len(self.table))
        for bucket in self.table:
            for keyValue in bucket:
                copied_table.insert(keyValue[0], keyValue[1])
        return copied_table
