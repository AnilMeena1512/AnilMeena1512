class Solution:
    def longestPalindrome(self, s: str) -> str:
        res="" #create an empty string
        long_substr=0
        
        #run a  for loop
        
        for i in range(len(s)):
            #initialize left and right pointers to the i
            #we would first check for odd string
            l_p,r_p=i,i
            
            while l_p>=0 and r_p<len(s) and s[r_p]==s[l_p]:
                if (r_p-l_p+1)>long_substr:
                    res=s[l_p:r_p+1]
                    long_substr=r_p-l_p+1
                
                l_p-=1
                r_p+=1
            
            #we would check for even string
            
            l_p,r_p=i,i+1
            while l_p>=0 and r_p<len(s) and s[r_p]==s[l_p]:
                if (r_p-l_p+1)>long_substr:
                    res=s[l_p:r_p+1]
                    long_substr=r_p-l_p+1
                
                l_p-=1
                r_p+=1
        return res
