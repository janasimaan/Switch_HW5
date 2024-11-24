class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * self.size

    def _hash(self, key):
        return hash(key) % self.size

    def _open_addressing(self, key):
        index = self._hash(key)
        while self.table[index] is not None and self.table[index][0] != key:
            index = (index + 1) % self.size
        return index

    def set(self, key, value):
        index = self._open_addressing(key)
        self.table[index] = (key, value)

    def get(self, key):
        index = self._open_addressing(key)
        if self.table[index] is not None and self.table[index][0] == key:
            return self.table[index][1]
        return None

# Example usage
table = HashTable(5)
table.set(238, "hello")  # 238 % 5 = 3
table.set(5251, "world")  # 5251 % 5 = 1
table.set(123, "good")  # 123 % 5 = 3 (collision, resolved with probing)

# Retrieving values
print(table.get(238))   # Output: hello
print(table.get(5251))  # Output: world
print(table.get(123))   # Output: good
print(table.get(22))    # Output: None
