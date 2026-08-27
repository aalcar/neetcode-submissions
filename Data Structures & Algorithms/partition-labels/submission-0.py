class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # the goal -> as many substrings as possible
        # abcabc only created one?
        # -- because we cant split it at all without another
        # -- substring having dupes
        # get counts
        # extend until you fill all counts for letters you've seen
        #
        # works for ordering, size, etc.
        #
        # add
        # decrement
        # remove if 0
        freq = Counter(s)
        res = []
        seen = set()

        l = r = 0
        

        while l < len(s):
            seen.add(s[r])
            while r < len(s) and seen:
                if s[r] not in seen and freq[s[r]] != 0:
                    seen.add(s[r])
                
                freq[s[r]] -= 1
                if freq[s[r]] == 0:
                    del freq[s[r]]
                    seen.remove(s[r])

                r += 1
            
            res.append(r - l)
            l = r
        
        return res

        # 

        # iterate over s
        # if x is new, start tracking that freq as well
        # we need to turn all the freqs down to 0 to stop iterating over
        # substr