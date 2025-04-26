class Solution:
    def valid_parentheses(self, s):
        mappings = {"{": "}", "[": "]", "(": ")"}
        stack = []

        for p in s:
            if p in mappings.keys():
                stack.append(p)
            else:
                if stack:
                    open_bracket = stack.pop()
                    mapped_bracket = mappings[open_bracket]
                    if mapped_bracket != p:
                        return False
                else:
                    return False
        return len(stack) == 0     

solution = Solution()
print(solution.valid_parentheses("()"))