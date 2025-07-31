class DetectSquares:

    def __init__(self):
        self.horizontals = {}
        self.verticals = {}
        self.points = {}

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] = self.points.get(tuple(point), 0) + 1
        x, y = point[0], point[1]

        if x not in self.horizontals:
            self.horizontals[x] = [point]
        else:
            self.horizontals[x].append(point)
        if y not in self.verticals:
            self.verticals[y] = [point]
        else:
            self.verticals[y].append(point)

    def count(self, point: List[int]) -> int:
        ways = 0
        xcoors = {}
        ycoors = {}
        x, y = point[0], point[1]
        if x not in self.horizontals or y not in self.verticals:
            return ways
        
        for key, val in self.horizontals[x]:
            if y == val: continue
            ycoors[val - y] = ycoors.get(val - y, 0) + 1
        for key, val in self.verticals[y]:
            if x == key: continue
            xcoors[key - x] = xcoors.get(key - x, 0) + 1
        
        for key in xcoors.keys():
            if key in ycoors and (x + key, y + key) in self.points:
                ways += ycoors[key] * xcoors[key] * self.points[tuple((x + key, y + key))]
            if -key in ycoors and (x + key, y - key) in self.points:
                ways += ycoors[-key] * xcoors[key] * self.points[tuple((x + key, y - key))]

        return ways
# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)