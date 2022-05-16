'''
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]

Constraints:

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
'''

from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result_set = set()
        nums.sort()

        for i in range(len(nums) - 3):
            for j in range(i+1, len(nums) - 2):
                self.two_pointer_sum(result_set, j+1, [nums[i], nums[j]], nums, target)
        return result_set

    def two_pointer_sum(self, result_set, left_index, running_list, nums: List[int], target: int):
        right_index = len(nums) - 1
        while left_index < right_index:
            cur_list = running_list + [nums[left_index], nums[right_index]]
            sum_result = sum(cur_list)

            if sum_result == target:
                result_set.add(tuple(cur_list))

            if sum_result < target:
                left_index += 1
            else:
                right_index -= 1


print((Solution()).fourSum([-3,-1,0,2,4,5], 2)) # -> [[-3,-1,2,4]]