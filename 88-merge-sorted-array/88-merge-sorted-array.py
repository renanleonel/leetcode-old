class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        right1, end = m-1, len(nums1)-1
        right2 = n-1

        while right1>=0 and right2>=0:
            if nums1[right1] > nums2[right2]:
                nums1[end], nums1[right1] = nums1[right1], nums1[end]
                end-=1
                right1-=1
            else:
                nums1[end], nums2[right2] = nums2[right2], nums1[end]
                end-=1
                right2-=1

        while right1>=0:
            nums1[end], nums1[right1] = nums1[right1], nums1[end]
            end-=1
            right1-=1

        while right2>=0:
            nums1[end], nums2[right2] = nums2[right2], nums1[end]
            end-=1
            right2-=1