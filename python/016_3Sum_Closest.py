'''
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0

Constraints:

3 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
-104 <= target <= 104
'''
from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closet_sum = 1000 # init to some high value

        nums.sort()
        no_of_intergers = len(nums)

        for i in range(no_of_intergers-2):
            i_data = nums[i]

            j = i + 1
            k = no_of_intergers - 1

            while j < k:
                current_sum = nums[i] + nums[j] + nums[k]

                current_diff = abs(current_sum - target)
                closest_diff = abs(closet_sum - target)

                if current_diff < closest_diff:
                    closet_sum = current_sum

                if current_diff > closest_diff:
                    k -= 1
                else:
                    j += 1
        return closet_sum

print((Solution()).threeSumClosest([1,1,-1,-1,3], -1,))