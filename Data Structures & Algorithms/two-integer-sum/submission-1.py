class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen: dict[int,int] = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                # found the pair
                return [seen[complement], i]
            # record that num could pair with "complement" later
            seen[num] = i
        # impossible per problem constraints
        raise ValueError("No two sum solution")