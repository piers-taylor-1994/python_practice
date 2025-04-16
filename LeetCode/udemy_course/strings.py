class Solution:
    def typed_out_strings_bf(self, s:str, t:str):
        list_s = []
        list_t = []
        for i in range(len(s)):
            if s[i] != "#":
                list_s.append(s[i])
            elif len(list_s) > 0:
                list_s.pop()
        for j in range(len(t)):
            if t[j] != "#":
                list_t.append(t[j])
            elif len(list_t) > 0:
                list_t.pop()
        return list_s == list_t
    def typed_out_strings(self, s:str, t:str):
        p1 = len(s) - 1
        p2 = len(t) - 1
        while p1 >= 0 or p2 >= 0:
            if s[p1] == "#":
                back_count = 2
                while back_count > 0:
                    p1 -= 1
                    back_count -= 1
                    if p1 >= 0 and s[p1] == "#":
                        back_count += 2
            if t[p2] == "#":
                back_count = 2
                while back_count > 0:
                    p2 -= 1
                    back_count -= 1
                    if p2 >= 0 and t[p2] == "#":
                        back_count += 2
            else:
                if p1 < 0 and p2 < 0:
                    break
                elif (p1 < 0 and p2 <= 0) or (p2 < 0 and p1 <= 0) or s[p1] != t[p2]:
                    return False
                p1 -= 1
                p2 -= 1
        return True
            

solution = Solution()
print(solution.typed_out_strings_bf("ab#z", "az#z"))
print(solution.typed_out_strings_bf("a##", "a##"))
print(solution.typed_out_strings("ab#c", "ad#c"))
print(solution.typed_out_strings("ab##", "c#d#"))
print(solution.typed_out_strings("xywrrmp", "xywrrmu#p"))
print(solution.typed_out_strings("a", "aa#a"))
print(solution.typed_out_strings("c#a#c", "c"))