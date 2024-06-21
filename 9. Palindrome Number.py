class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x = str(x)
        front_pointer = len(x)-1
        back_pointer = 0
        while front_pointer > back_pointer:
            if x[back_pointer] != x[front_pointer]:
                return False
            front_pointer = front_pointer - 1
            back_pointer = back_pointer + 1
        return True 
