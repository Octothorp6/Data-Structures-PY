class HashTable(object):
    """"
    HashTable(): Create a new, empty map. It returns an empty map collection.
    put(key,val): Add a new key-value pair to the map. If the key is already in the map,
    then replace the old value with the new value.
    get(key): Given a key, return the value stored in the map or None otherwise.
    len(): Return the number of key-value pairs stored in the map
    in:  Return True for a statement of the form key in map, if the given key is in the map, False otherwise.
    """
    def __init__(self, total):
        self.size = total
        self.slots = [None] * total
        self.data = [None] * total

    def put(self, key, data):
        hash_value = self.hash_function(key, len(self.slots))

        # if slot is empty
        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            # If data already exists in that slot, replace old value
            if self.slots[hash_value] == key:
                self.data[hash__value] = data

            # Otherwise, find the next available slot
            next_slot = self.rehash(hash_value, len(self.slots))

            # get to the next slot
            while self.slots[next_slot] is not None and self.slots[next_slot] != key:
                next_slot = self.rehash(next_slot, len(self.slots))

                # set new key, if None
                if self.slots[next_slot] is None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                else:
                    # Otherwise replace old value
                    self.data[next_slot] = data

    def hash_function(self, key, size):
        return key % size

    def rehash(self, old_hash, size):
        return (old_hash + 1) % size

    def get(self, key):
        # Retrieving items based on a given key

        start_slot = self.hash_function(key, len(self.slots))
        data = None
        stop = False
        found = False
        position = start_slot

        # Until we confirm that it is not empty or found
        while self.slots[position] is not None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == start_slot:
                    stop = True
        return data

    # Special Methods for Python indexing
    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

    def __contains__(self, key):
        if self.get(key):
            return True
        else:
            return False