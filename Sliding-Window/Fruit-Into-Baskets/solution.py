class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left, right = 0, 0
        longest = 0
        curr, matches = 0, 2
        fruit_dict = {}

        while right < len(fruits):
            fruit = fruits[right]

            if fruit not in fruit_dict:
                curr += 1
            
            fruit_dict[fruit] = fruit_dict.get(fruit, 0) + 1

            while left <= right and curr > matches:
                fruit_dict[fruits[left]] -= 1

                if fruit_dict[fruits[left]] == 0:
                    del fruit_dict[fruits[left]]
                    curr -= 1
                
                left += 1
            
            if curr <= matches:
                longest = max(longest, right - left + 1)
            
            right += 1
        
        return longest
