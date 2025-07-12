class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secretDict = {}

        for char in secret:
            secretDict[char] = secretDict.get(char, 0) + 1
        
        bulls, cows = 0, 0
        for i in range(len(guess)):
            guessChar = guess[i]
            secretChar = secret[i]

            if guessChar not in secretDict:
                continue
            elif guessChar == secretChar and secretDict[guessChar] > 0:
                bulls += 1
                secretDict[guessChar] -= 1
        
        for i in range(len(guess)):
            guessChar = guess[i]
            secretChar = secret[i]

            if guessChar not in secretDict:
                continue
            elif secretDict[guessChar] > 0 and guessChar != secretChar:
                cows += 1
                secretDict[guessChar] -= 1
        
        return f"{bulls}A{cows}B"
