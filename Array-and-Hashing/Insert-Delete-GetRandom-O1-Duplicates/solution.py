import collections 
import random

class RandomizedCollection:
    def __init__(self):
        self.map = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        to_return = True
        if val in self.map:
            to_return = False
        else:
            self.map[val] = []
        self.arr.append(val)
        self.map[val].append(len(self.arr) - 1)
        return to_return

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        ind_to_remove = self.map[val].pop()
        n = len(self.arr) - 1
        if n != ind_to_remove:
            self.arr[n], self.arr[ind_to_remove] = self.arr[ind_to_remove], self.arr[n]
            to_change = self.arr[ind_to_remove]
            self.map[to_change].remove(n)
            self.map[to_change].append(ind_to_remove)
        self.arr.pop()
        if len(self.map[val]) == 0:
            del self.map[val]
        
        return True

    def getRandom(self) -> int:
        return self.arr[random.randint(0, len(self.arr) - 1)]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()