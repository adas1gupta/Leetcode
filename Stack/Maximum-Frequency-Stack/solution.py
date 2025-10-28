class FreqStack:

    def __init__(self):
        self.freq = {}
        self.freq_group = {}
        self.max_freq = 0

    def push(self, val: int) -> None:
        fr = self.freq.get(val, 0) + 1
        self.freq[val] = fr
        
        self.max_freq = max(self.max_freq, fr)

        if fr not in self.freq_group:
            self.freq_group[fr] = []
        self.freq_group[fr].append(val)

    def pop(self) -> int:
        val = self.freq_group[self.max_freq].pop()
        self.freq[val] -= 1

        if not self.freq_group[self.max_freq]:
            self.max_freq -= 1
        
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()