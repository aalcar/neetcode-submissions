class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # mega brute force:
        # get a prefix from first string
        # check every string
        # expand prefix
        # check every string
        prefix = ""
        matches = True
        while matches and len(prefix) < len(strs[0]):
            prefix = strs[0][:len(prefix) + 1]
            for string in strs:
                if string[:len(prefix)] != prefix:
                    prefix = prefix[:-1]
                    matches = False
                    break

        return prefix