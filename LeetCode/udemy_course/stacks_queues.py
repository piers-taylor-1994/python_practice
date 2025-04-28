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
    
class MyQueue_v1(object):

    def __init__(self):
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        return self.stack.pop(0)
        

    def peek(self):
        """
        :rtype: int
        """
        return self.stack[0]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stack) == 0
    
class MyQueue_v2(object):

    def __init__(self):
        self.stack = []
        self.stack2 = []

    def consolidate(self):
        if len(self.stack2) == 0:
            for _ in range(len(self.stack)):
                self.stack2.append(self.stack.pop())

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        self.consolidate()
        return self.stack2.pop()
        

    def peek(self):
        """
        :rtype: int
        """
        self.consolidate()
        return self.stack2[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stack) == 0 and len(self.stack2) == 0

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

myQueue = MyQueue_v1()
myQueue.push(1)
myQueue.push(2)
print(myQueue.peek())
print(myQueue.pop())
print(myQueue.empty())

myQueue2 = MyQueue_v2()
myQueue2.push(1)
myQueue2.push(2)
print(myQueue2.peek())
print(myQueue2.pop())
print(myQueue2.empty())