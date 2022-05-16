'''
Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
'''

class Solution:
    class palindrom_str:
        pair_char = ""
        single_char = ""

        def add_pair_char(self, s: str):
            self.pair_char += s
        def add_single_char(self, s: str):
            self.single_char = s

        def get_len(self) -> int:
            return (len(self.pair_char) * 2) + len(self.single_char)

        def get_palindrom(self) -> str:
            no_of_pair_char = len(self.add_pair_char)

            if no_of_pair_char == 0:
                return ""

            return_str = ""
            for i in range(0, no_of_pair_char -1 ):
                return_str += self.pair_char[i]

            return_str += self.single_char if self.single_char != "" else ""

            for i in range(no_of_pair_char -1, 0):
                return_str += self.pair_char[i]

            return return_str


    def longestPalindrome(self, s: str) -> str:
        longest_pal_substr = ""

        left = 0
        right = len(s) - 1

        cur_palindrom_obj = self.palindrom_str()

        while left <= right:
            len_of_longest = len(longest_pal_substr)
            len_of_cur = cur_palindrom_obj.get_len()

            if left == right:
                # we are at the very end
                if len_of_cur != 0:
                    longest_pal_substr.add_single_char(s[left])
            elif s[left] == s[right]:
                # We have a matched pair
                cur_palindrom_obj.add_pair_char(s[left])
                if len_of_longest < cur_palindrom_obj.get_len():
                    longest_pal_substr = cur_palindrom_obj.get_palindrom()

