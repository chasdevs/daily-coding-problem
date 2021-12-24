class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        count = 0
        sums = 0
        d = {0: 1}
        
        for i, num in enumerate(nums):
            sums += num
            count += d.get(sums-k, 0)
            d[sums] = d.get(sums, 0) + 1
        
        return count