'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
'''
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        LONGEST_STR = 200

        longestPrefix = ""

        for char_index in range(0, LONGEST_STR):

            current_char = ""

            exit_loop = False

            for inputStr in strs:

                if char_index >= len(inputStr):
                    exit_loop = True
                    break

                if current_char == "":
                    current_char = inputStr[char_index]

                elif current_char != inputStr[char_index]:
                    exit_loop = True
                    break

            if not exit_loop:
                # We got a valid match
                longestPrefix = longestPrefix + current_char
            else:
                break

        return longestPrefix