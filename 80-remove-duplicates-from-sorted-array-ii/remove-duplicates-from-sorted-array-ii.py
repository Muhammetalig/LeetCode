class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)
        
        index = 2  # İlk iki eleman doğrudan kabul edilir
        
        for i in range(2, len(nums)):
            if nums[i] != nums[index - 2]:  # Son iki eklenenle aynı değilse ekle
                nums[index] = nums[i]
                index += 1
        
        return index

        