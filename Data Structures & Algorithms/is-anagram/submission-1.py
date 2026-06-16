from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # a string is an anagram if it contains the same character frequencies as
        # another string

        freqS = Counter(s)
        freqT = Counter(t)

        return freqS == freqT