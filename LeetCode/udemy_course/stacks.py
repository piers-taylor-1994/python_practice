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

    def minimum_brackets_to_remove(self, s):
        stack = []
        s_list = list(s)

        for pos in range(len(s_list)):
            if s_list[pos] in "()":
                if s_list[pos] == "(":
                    stack.append(pos)
                else:
                    if stack:
                        stack.pop()
                    else:
                        s_list[pos] = ""
        
        if stack:
            for pos in stack:
                s_list[pos] = ""
        return "".join(s_list)



solution = Solution()
print(solution.valid_parentheses("()"))
print(solution.minimum_brackets_to_remove("a)cbc(d)"))
print(solution.minimum_brackets_to_remove("(ab(c)d"))
print(solution.minimum_brackets_to_remove("))(("))
print(solution.minimum_brackets_to_remove("())()((("))

test = {0: "Hello", 1: "Test"}
print(test.popitem())