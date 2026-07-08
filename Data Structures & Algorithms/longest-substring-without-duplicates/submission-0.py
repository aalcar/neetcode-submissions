class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # do a sliding window and maintain a set of seen characters
        # "contiguous sequence"
        # sliding windows allow us to examine all useful
        # contiguous sequences in O(n)
        # -- they work by adding and removing data from a 
        # data structure as they move throughout a data source
        # 
        
        seen = set()
        maxLength = l = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            
            seen.add(s[r])

            maxLength = max(maxLength, r - l + 1)

        return maxLength
