class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        if not n:
            return []
        center = ['0','1','8']                      # center in case of odd length only
        ends = ['11','88','69','96']                # 0 cannot be first character
        middle = ['00','11','88','69','96']         # elsewhere in the string but middle and ends
        ans = []
        def recursive(center,index):
            nonlocal ans
            if index==0:
                ans.append(center)
                return
            
            expand = ends if index==1 else middle          
                            
            for item in expand:
                new_center = item[0] + center + item[1]
                recursive(new_center,index-1)
        
        centers = center if n%2!=0 else ['']       
        m = n//2       
        for c in centers:
            recursive(c,m)
        
        return ans


        