class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}

        for i, num in enumerate(nums):
            other = target - num
            if other in store:
                return [store[other], i]
            else:
                store[num] = i
