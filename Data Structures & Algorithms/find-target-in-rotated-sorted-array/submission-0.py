class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1

        # find minimum
        while start < end:
            mid = (start + end) // 2

            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid

        min_idx = start

        if nums[min_idx] == target:
            return min_idx
        else:
            if min_idx == 0:
                start, end = 0, len(nums) - 1

            elif target >= nums[0] and target <= nums[min_idx - 1]:
                start, end = 0, min_idx - 1
            else:
                start, end = min_idx, len(nums) - 1

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1

        return -1
        