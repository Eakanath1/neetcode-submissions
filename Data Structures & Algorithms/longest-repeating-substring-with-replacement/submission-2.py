class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        if n == 1:
            return 1
        freq = [0]*26
        res = 0
        max_freq = 0
        l = 0
        for r in range(n):
            c_idx = ord(s[r])-ord('A')
            freq[c_idx] += 1
            if freq[c_idx] > max_freq:
                max_freq = freq[c_idx]
            # shrink the start until acceptable replacements
            while (r-l+1)-max_freq > k:
                freq[ord(s[l])-ord('A')] -= 1
                l += 1
            if r-l+1 > res:
                res = r-l+1
        return res