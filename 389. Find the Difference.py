class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if s == "":
            return t
        sort_s = ''.join(sorted(s))
        sort_t = ''.join(sorted(t))

        s_pointer = 0
        t_pointer = 0

        while (sort_s[s_pointer] == sort_t[t_pointer]) and (t_pointer < len(sort_s)-1):
            s_pointer = s_pointer + 1
            t_pointer = t_pointer + 1
        
        if sort_s[s_pointer] == sort_t[t_pointer]:
            return sort_t[t_pointer+1]
        else:
            return sort_t[t_pointer]
