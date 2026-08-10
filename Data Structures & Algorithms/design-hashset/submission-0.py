class MyHashSet:

    def __init__(self):
        
        self.capacity = 1000
        self.buckets = [[] for _ in range(self.capacity)]

    def _hash(self, key:int) -> int:
        return key % self.capacity

    def add(self, key: int) -> None:
        bucket_index = self._hash(key)
        bucket = self.buckets[bucket_index]

        for i, k in enumerate(bucket):
           if k == key:
                bucket[i] = key
                return    
        bucket.append(key)

    def remove(self, key: int) -> None:
        bucket_index = self._hash(key)
        bucket = self.buckets[bucket_index]
        
        for i,k in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                return

    def contains(self, key: int) -> bool:
        bucket_index = self._hash(key)
        bucket = self.buckets[bucket_index]
        
        for i, k in enumerate(bucket):
            if k == key:
                return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)