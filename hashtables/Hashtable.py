class Hashtable(object):
    def __init__(self):
        self.table = []

    def occupied(self, index: int):
        return self.table[index] is not None

    def hash_key(self, key: str):
        return abs(hash(key)) % len(self.table)

    # will search for the index of the key
    def find_key(self, key: str):
        hashed_key = self.hash_key(key)
        if (self.table[hashed_key] is not None) and (self.table[hashed_key].key != key):
            return hashed_key

        stop_index = hashed_key

        if hashed_key == len(self.table) - 1:
            hashed_key = 0
        else:
            hashed_key += 1

        while (hashed_key != stop_index) and (self.table[hashed_key] is not None) and (
                self.table[hashed_key].key != key):
            hashed_key = (hashed_key + 1) % len(self.table)

        # if stop_index == hashedKey, then we've looked at the entire table and did not find the value
        if stop_index == hashed_key:
            return - 1
        else:
            return hashed_key

    def put(self, key: str, value):
        hashed_key = self.hash_key(key)
        if self.occupied(hashed_key):
            stop_index = hashed_key
            if hashed_key == len(self.table) - 1:
                hashed_key = 0
            else:
                hashed_key += 1
