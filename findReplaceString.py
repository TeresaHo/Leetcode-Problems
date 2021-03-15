class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        length = len(indexes)
        new_string = S
        diff = 0
        check = {}
        for i in range(length):
            diff = 0
            start = indexes[i]
            w_len = len(sources[i])
            
            if S[start:start+w_len] == sources[i]:
                
                for key in check:
                    if start>key:
                        diff+=check[key]
                    
                
                new_string = new_string[:start+diff]+targets[i]+new_string[start+w_len+diff:] 
                check[start] = len(targets[i]) - w_len
        return new_string