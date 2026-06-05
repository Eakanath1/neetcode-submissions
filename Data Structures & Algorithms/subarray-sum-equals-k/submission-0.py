class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_count = defaultdict(int)
        prefix_count[0] = 1

        cur_prefix, res = 0, 0

        for num in nums:
            cur_prefix += num
            res += prefix_count[cur_prefix - k]
            prefix_count[cur_prefix] += 1

        return res 