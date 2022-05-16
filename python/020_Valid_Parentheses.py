'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''
class Solution:
    def isValid(self, s: str) -> bool:
        bracket_list = []

        if not s:
            return True

        for char in s:
            if char == "(":
                bracket_list.append(char)
            elif char == ")":
                if (len(bracket_list) == 0) or (bracket_list[-1] != "("):
                    return False
                else:
                    bracket_list.pop()

            elif char == "{":
                bracket_list.append(char)
            elif char == "}":
                if (len(bracket_list) == 0) or (bracket_list[-1] != "{"):
                    return False
                else:
                    bracket_list.pop()

            elif char == "[":
                bracket_list.append(char)
            elif char == "]":
                if (len(bracket_list) == 0) or (bracket_list[-1] != "["):
                    return False
                else:
                    bracket_list.pop()

        if len(bracket_list) != 0:
            return False

        return True

# print((Solution()).isValid("([)]"))
print((Solution()).isValid(")"))