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
        #
        # record last indices
        # if a char comes in with later last index, change
        indices = defaultdict(int)
        for i, v in enumerate(s):
            indices[v] = i

        res = []
        size = 0
        farthest = 0

        for i, c in enumerate(s):
            size += 1
            farthest = max(farthest, indices[c])
            if i == farthest:
                res.append(size)
                size = 0

        return res

        # 

        # iterate over s
        # if x is new, start tracking that freq as well
        # we need to turn all the freqs down to 0 to stop iterating over
        # substr