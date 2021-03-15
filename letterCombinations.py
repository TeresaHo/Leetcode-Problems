class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        word_map = {
            "2":["a","b","c"],
            "3":["d","e","f"],
            "4":["g","h","i"],
            "5":["j","k","l"],
            "6":["m","n","o"],
            "7":["p","q","r","s"],
            "8":["t","u","v"],
            "9":["w","x","y","z"],
        }
        ans = []
        def backtracking(i,string):
            nonlocal ans
            nonlocal length
            if i ==length:
                ans.append(string)
                return
            num = digits[i]
            letters = word_map[num]
            for char in letters:
                newString = string+char
                backtracking(i+1,newString)
        
        i=0
        length = len(digits)
        backtracking(i,"")
        
        return ans