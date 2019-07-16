class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)
        for i, m in enumerate(nums):
            j = i+1
            while j < size:
                if target == (m + nums[j]):
                    return [i, j]
                else:
                    j += 1

    def two_sum_with_dict(self, nums: List[int], target: int) -> List[int]:
        _dict = {}
        for i, m in enumerate(nums):
            _dict[m] = i

        for i, m in enumerate(nums):
            j = _dict.get(target-m)
            if j is not None and i != j:
                return [i, j]
