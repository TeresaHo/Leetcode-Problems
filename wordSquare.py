class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        
        def recursive(valid_words):
            nonlocal s
            nonlocal ans
            level = len(valid_words)
            prefix =""
            return_list = []
            if len(valid_words)==len(valid_words[0]):
                ans.append(valid_words)
                return
            #set prefix
            for item in valid_words:
                prefix+=item[level]
            # search
            remaining = s - set(valid_words)
            
            for w in remaining:
                if prefix == w[:level]:
                    valid_words.append(w)
                    recursive(valid_words)
            return
        
        ans = []
        s = set(words)
        for w in words:
            if recursive([w]):
                
                ans.append(recursive([w]))
        return ans