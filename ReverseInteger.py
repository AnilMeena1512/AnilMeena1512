class Solution:
    def reverse(self, x: int) -> int:
        if x<(-2147483648) or x>(2147483647):
            return 0
        y=str(abs(x))
        
        r=int(str(y)[::-1])
        
        if x<=0 and x> -2147483648 :
            return((-1)*r)
        
        elif x>0 and x<2147483647 :
            return(r)
