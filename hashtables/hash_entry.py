

class HashEntry(object):
    def __init__(self,key,value):
        self.key = key
        self.value = value

    def __repr__(self):
        return "HashEntry { Key: {0}, Value: {1} }".format(self.key,self.value)
