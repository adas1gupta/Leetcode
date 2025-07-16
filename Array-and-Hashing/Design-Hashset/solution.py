class MyHashSet:

    def __init__(self):
        self.arr = [[]] * ((10 ** 4) + 1)

    def add(self, key: int) -> None:
        to_examine = self.arr[key % (10 ** 4)]
        for item in to_examine:
            if item == key:
                return
        self.arr[key % (10 ** 4)].append(key)

    def remove(self, key: int) -> None:
        to_examine = self.arr[key % (10 ** 4)]
        for i, val in enumerate(to_examine):
            if val == key:
                to_examine[len(to_examine) - 1], to_examine[i] = to_examine[i], to_examine[len(to_examine) - 1]
                to_examine.pop()
                break
        

    def contains(self, key: int) -> bool:
        for item in self.arr[key & (10 ** 4)]:
            if key == item:
                return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)