class Solution(object):
    def merge(self, nums1, m, nums2, n):
        mx = m -1
        nx = n-1
        r = m+n-1

        while nx>=0:
            if mx >=0 and nums1[mx]>nums2[nx]:
                nums1[r] = nums1[mx]
                mx -=1
            else:
                nums1[r] = nums2[nx]
                nx -= 1

            r -=1
        