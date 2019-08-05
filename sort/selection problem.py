# 见https://leetcode.com/problems/kth-largest-element-in-an-array/
class Solution:
    def partition(self, arr, lo, hi):
        x = arr[hi]
        i = lo - 1
        for j in range(lo, hi):
            if arr[j] <= x:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[hi] = arr[hi], arr[i+1]
        return i+1
    
    # def qsort(self, arr, lo, hi):
    #     if lo < hi:
    #         pos = self.partition(arr, lo, hi)
    #         self.qsort(arr, lo, pos-1)
    #         self.qsort(arr, pos+1, hi)
    
    def findKth(self, arr, lo, hi, k):
        if (lo <= hi) and (0 < k <= hi - lo + 1): 
            pos = self.partition(arr, lo, hi)
            if pos == hi - k + 1: return arr[pos]
            elif pos > hi - k + 1: return self.findKth(arr, lo, pos-1, k - (hi-pos+1))
            else: return self.findKth(arr, pos+1, hi, k)
    
    def findKthLargest(self, nums: List[int], k: int) -> int:
        lo, hi = 0, len(nums) - 1
        #self.qsort(nums, lo, hi)
        #return nums[hi-k+1]
        return self.findKth(nums, lo, hi, k)
