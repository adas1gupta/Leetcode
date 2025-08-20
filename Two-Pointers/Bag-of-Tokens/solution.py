class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score = 0
        tokens = sorted(tokens)
        start, end = 0, len(tokens) - 1

        while start <= end:
            while start <= end and tokens[start] <= power:
                score += 1
                power -= tokens[start]
                start += 1
            
            if end - start <= 1:
                break
            elif score > 0 and power + tokens[end] >= tokens[start]:
                score -= 1
                power += tokens[end]
                end -= 1
            else:
                break
        
        return score