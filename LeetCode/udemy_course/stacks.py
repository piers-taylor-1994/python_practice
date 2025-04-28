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
        p1 = 0

        while p1 < len(s_list):
            if s_list[p1] in "()":
                if s_list[p1] == "(":
                    stack.append(p1)
                else:
                    if stack:
                        stack.pop()
                    else:
                        s_list.pop(p1)
                        continue
            p1 += 1
        
        if stack:
            for pos in stack[::-1]:
                s_list.pop(pos)
        return "".join(s_list)

    def minimum_brackets_to_remove_v2(self, s):
        s = list(s)
        stack = []

        for i in range(len(s)):
            if s[i] == ")":
                if stack:
                    stack.pop()
                else:
                    s[i] = ""
            elif s[i] == "(":
                stack.append(i)
        
        if stack:
            for i in stack:
                s[i] = ""
        
        return "".join(s)



solution = Solution()
print(solution.valid_parentheses("()"))
print(solution.minimum_brackets_to_remove("a)cbc(d)"))
print(solution.minimum_brackets_to_remove("(ab(c)d"))
print(solution.minimum_brackets_to_remove("))(("))
print(solution.minimum_brackets_to_remove("())()((("))
print(solution.minimum_brackets_to_remove_v2("a)cbc(d)"))
print(solution.minimum_brackets_to_remove_v2("(ab(c)d"))
print(solution.minimum_brackets_to_remove_v2("))(("))
print(solution.minimum_brackets_to_remove_v2("())()((("))