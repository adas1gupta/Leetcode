from itertools import combinations
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        people_to_website = {}
        patterns = {}
        frequencies = {}

        for i in range(len(username)):
            user = username[i]
            time = timestamp[i]
            site = website[i]

            if user not in people_to_website:
                people_to_website[user] = [(time, site)]
            else:
                people_to_website[user].append((time, site))
        
        for key in people_to_website.keys():
            val = [y for x, y in sorted(people_to_website[key])]
            combos = itertools.combinations(val, 3)
            for item in set(combos):
                patterns[item] = patterns.get(item, 0) + 1
        
        for key, val in patterns.items():
            if val in frequencies:
                frequencies[val].append(key)
            else:
                frequencies[val] = [key]

        return sorted(frequencies[max(patterns.values())])[0]
