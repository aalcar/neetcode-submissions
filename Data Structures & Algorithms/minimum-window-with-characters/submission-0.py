from collections import defaultdict, Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # There COULD not be a substring, t, inside of s
        # correct output is always unique
        # there could be multiple substrings, but
        # the shortest substring is unique
        # does that mean there's only one
        # OR that the characters that make up the substring
        # are unique
        #
        # OUZODXYXAZV
        # find XYZ
        # 
        # O->U->Z
        # we know that OU are NEVER going to be in the shortest substring
        # Z->O->D->X->Y ok that's a 5'er
        # go down to XY
        # we can either go down to XY or []
        # theres no benefit to going []
        # just shrink down to XY
        # XYX ok just shrink down to YX
        # YXAZ ok that's a 4'er
        # shrink down to Z
        # ZV -- nothing here
        # YXAZ is our shortest

        # saving the substring itself isnt that bad
        # if shortest = "", min_size is looking like inf

        freq_substring = Counter(t)
        freq_window = defaultdict(int)
        current_checks = 0
        total_checks = len(set(t)) 
        saved_left = -1
        saved_right = n = len(s)

        # O
        left = 0
        for right in range(n):
            freq_window[s[right]] += 1
            if freq_window[s[right]] == freq_substring[s[right]]:
                current_checks += 1

            while current_checks == total_checks:
                # only saved if bigger
                if saved_right - saved_left + 1 > right - left + 1:
                    saved_left = left
                    saved_right = right

                if freq_window[s[left]] == freq_substring[s[left]]:
                    current_checks -= 1
                freq_window[s[left]] -= 1
                left += 1
        
        return s[saved_left:saved_right + 1] if saved_left != -1 else ""


