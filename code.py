class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = r = 0
        maxLen = 0 
        curK = 0 
        for num in nums:
            if num == 1:
                r += 1
            else: 
                if curK < k:
                    curK += 1
                    r += 1
                else:
                    while nums[l] != 0:
                        l += 1
                    l+=1
                    r+=1
            maxLen = max(maxLen, r-l)
        return maxLen