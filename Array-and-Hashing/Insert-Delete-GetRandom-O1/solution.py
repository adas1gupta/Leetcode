import random
class RandomizedSet:

    def __init__(self):
        self.items = {}
        self.randomness = []

    def insert(self, val: int) -> bool:
        if val in self.items:
            return False
        else:
            self.randomness.append(val)
            self.items[val] = len(self.randomness) - 1
            return True

    def remove(self, val: int) -> bool:
        if val not in self.items:
            return False
        
        ind = self.items[val]
        last = self.randomness[-1]
        self.randomness[-1], self.randomness[ind] = self.randomness[ind], self.randomness[-1]
        self.items[last] = ind
        self.randomness.pop()
        del self.items[val]
        
        return True

    def getRandom(self) -> int:
        return self.randomness[random.randint(0, len(self.randomness) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()