class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # pretty light
        # mainain a rolling hashmap w a sliding window
        # map { letter : frequency }
        # if map[newLetter] > map[currentMaxLetter]
        #   make new max letter
        # increment left ptr until right - left + 1 - freq[max] <= k
        freq = {}

        left = maxLength = maxFreq = 0
        for right in range(len(s)):
            if s[right] in freq:
                freq[s[right]] += 1
            else:
                freq[s[right]] = 1
            
            if freq[s[right]] >= maxFreq:
                maxFreq = freq[s[right]]

            while right - left + 1 - maxFreq > k:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]

                left += 1
        
            maxLength = max(maxLength, right - left + 1)
        return maxLength