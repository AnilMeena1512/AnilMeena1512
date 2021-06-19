class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #combine nums1 and nums2 in one list
        num_total=nums1+nums2
        num_total.sort() #sorting the combined list
        
        int_1=int((len(num_total)-1)/2)
        int_2=int(len(num_total)/2)
        
        return((num_total[int_1]+num_total[int_2])/2)
