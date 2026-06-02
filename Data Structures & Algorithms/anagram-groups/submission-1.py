class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        occ: Dict[tuple, List[str]] = defaultdict(list)
        for s in strs:
            freq_list = [0]*26
            for c in s:
                freq_list[ord(c)-ord('a')] += 1
            occ[tuple(freq_list)].append(s)
        return list(occ.values())