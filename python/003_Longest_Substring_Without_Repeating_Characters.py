'''
Given a string s, find the length of the longest substring without repeating characters.
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substring = []

        current_char_dict = {}
        running_substring = []
        for char in s:
            if char not in current_char_dict:
                # This is not a repeating character
                running_substring += char
                current_char_dict[char] = 0
                if len(running_substring) > len(longest_substring):
                    longest_substring = running_substring.copy()
            else:
                # this is actually a repeating character.
                # Keep popping characters from our running list until we hit our character
                # also remove each popped char from our dict
                for char_to_pop in running_substring.copy():
                    popped_char = running_substring.pop(0)
                    current_char_dict.pop(popped_char)

                    if char == char_to_pop:
                        running_substring += char
                        current_char_dict[char] = 0
                        break

        return len(longest_substring)


print((Solution()).lengthOfLongestSubstring("ohvhjdml"))
