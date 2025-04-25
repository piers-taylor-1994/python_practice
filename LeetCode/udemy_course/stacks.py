class Solution:
    def valid_parentheses(self, s):
        mappings = {"}": "{", "]": "[", ")": "("}
        stack = []

        for i in range(len(s)):
            if s[i] in mappings.values():
                stack.append(s[i])
            else:
                if stack:
                    open_bracket = stack.pop()
                    if open_bracket != mappings[s[i]]:
                        return False
                else:
                    return False
        return len(stack) == 0

solution = Solution()
print(solution.valid_parentheses("()"))