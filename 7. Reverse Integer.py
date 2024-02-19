class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            reverse = (str(x)[::-1])
            reverse = int(reverse)
            if reverse < -(2**31) or reverse > (2**31)-1:
                return 0
            else:
                return reverse
        else:
            x = -x
            reverse = (str(x)[::-1])
            reverse = int(reverse)
            if reverse < -(2**31) or reverse > (2**31)-1:
                return 0
            else:
                return -reverse



        
