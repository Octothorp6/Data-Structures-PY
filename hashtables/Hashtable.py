
class HashEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return "HashEntry { Key: {0}, Value: {1} }".format(self.key, self.value)


class Hashtable:
    def __init__(self):
        self.table = []

    def occupied(self, index: int):
        return self.table[index] is not None

    def hash_key(self, key: str):
        return abs(hash(key)) % len(self.table)

    @staticmethod
    def test_key(key, length):
        if key == length - 1:
            key = 0
        else:
            key += 1
        return key

    # will search for the index of the key
    def find_key(self, key: str):
        hashed_key = self.hash_key(key)
        if (self.table[hashed_key] is not None) and (self.table[hashed_key].key != key):
            return hashed_key

        stop_index = hashed_key

        hashed_key = self.test_key(hashed_key, len(self.table))

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
            hashed_key = self.test_key(hashed_key, len(self.table))

            # perform linear probing until we find an empty spot to enter our
            while self.occupied(hashed_key) and hashed_key != stop_index:
                hashed_key = (hashed_key + 1) % len(self.table)

        self.table[hashed_key] = HashEntry(key, value)

    def get(self, key: str):
        hashed_key = self.find_key(key)
        if hashed_key == -1:
            return None

        return self.table[hashed_key]

    def remove(self, key: str):
        hashed_key = self.find_key(key)
        if hashed_key == -1:
            return None

        value = self.table[hashed_key].value
        self.table[hashed_key] = None

        old_table = self.table
        self.table = []

        for i in range(len(old_table)):
            if old_table[i] is not None:
                self.put(old_table[i].key, old_table[i].value)

        return value

    def print_table(self):
        for i in range(len(self.table)):
            print(self.table[i])
