from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        def preprocess(wordList):
            worDict = defaultdict(list)
            for string in wordList:
                for i in range(len(string)):
                    tmp = string[:i]+"*"+string[i+1:]
                    worDict[tmp].append(string)
            return worDict
        
        def findNeighbor(mapping,string):
            neighbors = []
            for i in range(len(string)):
                tmp = string[:i]+"*"+string[i+1:]
                for item in mapping[tmp]:
                    if item != string:
                        neighbors.append(item)
            return neighbors
                
        
        mapping = preprocess(wordList)
        word_q = deque([[beginWord]])
        
        while(word_q):
            curr_path = word_q.popleft()
            last_node = curr_path[-1]
            neighbors = findNeighbor(mapping,last_node)
            
            for i in neighbors: 
                new_path = list(curr_path)                
                if i not in new_path:
                    new_path.append(i)
                if i == endWord:
                    return new_path
                word_q.append(new_path)
        
            
                
            
        
            
        