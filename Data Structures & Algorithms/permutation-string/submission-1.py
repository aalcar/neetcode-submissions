from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # freq in substring?
        freqs1 = defaultdict(int)
        for c in s1:
            freqs1[c] += 1
        
        # sliding window

        # check if freqs2[s[left]] > freqs1[s[left]], iterate
        # abc
        # lecabee
        # c
        freqs2 = defaultdict(int)
        left = 0
        for right in range(len(s2)):
            freqs2[s2[right]] += 1

            while left < len(s2) and freqs2[s2[left]] > freqs1[s2[left]]:
                freqs2[s2[left]] -= 1
                left += 1

            if freqs1 == freqs2:
                return True
        
        return False

            