class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0  # val olmayan elemanları takip eden index
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]  # val olmayan elemanı başa taşı
                k += 1  # Geçerli eleman sayısını artır
        return k
