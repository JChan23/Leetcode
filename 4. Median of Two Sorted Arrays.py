class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        array = nums1 + nums2
        average = 0
        length = len(array)
        for i in range(length):
            for j in range(0, length - i - 1):
                if array[j] > array[j+1]:
                    temp = array[j]
                    array[j] = array[j+1]
                    array[j+1] = temp
        print(array)
        print(length)
        if length % 2 == 1:
            return float(array[(length//2)])
        else:
            average = float((array[length//2] + array[(length//2)-1])/2)
            return average

