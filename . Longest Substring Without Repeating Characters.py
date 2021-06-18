class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "": #base condition
            return 0
        res=0        #maxmullenght of the current substring
        start=0      # starting index of the window
        end=0        #ending index of the window
        seen=set()   # create a set to store the unique character
        
        #loop for each character in string
        while end<len(s):
            if s[end]  not in seen:
                seen.add(s[end])
                end+=1
                res=max(res,len(seen))
            else:
                seen.remove(s[start])
                start+=1
        return res
