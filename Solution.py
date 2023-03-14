class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        left = 0
        r = len(nums) - 1

        while (left <= r):
            mid = (left + r) // 2

            if nums[mid] == target:
                return mid
            elif (target > nums[mid]):
                    left = mid + 1
            else:
                r = mid - 1
        return left
