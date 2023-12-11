class MyHashTable:

    # Constructor for the hash table
    def __init__(self, initial_capacity=10):
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # Updates an item in the hash table or inserts a new item if not found
    def update(self, key, value):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for key_value in bucket_list:
            if key_value[0] == key:
                key_value[1] = value
                return True

        key_value = [key, value]
        bucket_list.append(key_value)
        return True

    # Returns an item from the hash table or None if not found
    def get(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for key_value in bucket_list:
            if key_value[0] == key:
                return key_value[1]
        return None
