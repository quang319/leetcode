'''
https://leetcode.com/problems/generate-parentheses/

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]


Constraints:

1 <= n <= 8
'''
from typing import List

class Solution:
    # def generateParenthesis(self, n):
    #     """
    #     :type n: int
    #     :rtype: List[str]
    #     """
    def generateParenthesis(self, n: int) -> List[str]:
        output_list = []
        self.backtracking(output_list, "", 0, 0, n)
        return output_list

    def backtracking(self, running_list: List[str], cur_str: str, open: int, close: int, max: int):
        # goal: the string reaches the max number of char and has both closing and opening brackets
        if len(cur_str) == (max * 2):
            running_list.append(cur_str)
            return

        # decisions: Keep appending opening bracket until you reach the max number
        if open < max:
            self.backtracking(running_list, cur_str+"(", open+1, close, max)

        # constrainst: We can not append a closing bracket until you have append a opening bracket
        if close < open:
            self.backtracking(running_list, cur_str+")", open, close+1, max)


print((Solution()).generateParenthesis(3))