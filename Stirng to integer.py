class Solution:
    def myAtoi(self, s: str) -> int:
        
        res=0
        i=0
        sign=1
        
        str=s.strip()
        
        if len(str)<2:
            if str.isdigit():
                return str
            else:
                return res
        if str[0]=='-' or str[0]=='+':
            if str[0]=='-':
                sign=-1
            else:
                sign
            i+=1
            
        if not str[i].isdigit():
            return res
        
        for i in range(i,len(str)):
            if not str[i].isdigit():
                break
            res = res * 10 + (ord(str[i]) - ord('0'))
        res = -2147483648 if sign * res < -2147483648 else sign * res
        return 2147483647 if res > 2147483647 else res
