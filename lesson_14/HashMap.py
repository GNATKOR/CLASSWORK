class MyHashMap:
    def __init__(self):
        self.hashmap = []

    def put(self, key, value):
        for i in self.hashmap:
            if i[0] == key:
                i[1] = value
        self.hashmap.append([key, value])

    def get(self, key):
        for i in self.hashmap:
            if i[0] == key:
                return i[1]
        return -1

    def remove(self, key):
        for i, value in enumerate(self.hashmap):
            if value[0] == key:
                self.hashmap.pop(i)

