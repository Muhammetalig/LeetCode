class Solution:
    def merge(self, nums1, m, nums2, n):
        i = m - 1  # nums1'in son geçerli elemanının indexi
        j = n - 1  # nums2'nin son elemanının indexi
        k = m + n - 1  # nums1'in toplam uzunluğundaki son index

        while j >= 0:  # nums2 tamamen yerleştirilene kadar devam et
            if i >= 0 and nums1[i] > nums2[j]:  # nums1'in elemanı daha büyükse
                nums1[k] = nums1[i]  # nums1'in sonundaki boş yere yerleştir
                i -= 1  # nums1'in indexini azalt
            else:  # nums2'nin elemanı daha büyükse veya nums1 elemanları tükendiyse
                nums1[k] = nums2[j]  # nums2'nin elemanını yerleştir
                j -= 1  # nums2'nin indexini azalt
            k -= 1  # nums1'in yerleştirme indexini azalt
