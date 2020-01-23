# 127. Word Ladder
# https://leetcode.com/problems/word-ladder/

from collections import defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        def generate_intermediate_words(words, n):
            intermediate_words = defaultdict(set)
            for x in words:
                for i in range(n):
                    k = x[:i] + '?' + x[i+1:]
                    intermediate_words[k].add(x)
            return intermediate_words        
                
        n = len(beginWord)
        d = generate_intermediate_words(wordList, n)
        
        queue = []
        queue.append((beginWord, 1,))
        explored = set()
        
        while queue:
            (current, length,) = queue.pop(0)
            explored.add(current[0])
            
            for i in range(n):
                k = current[:i] + '?' + current[i+1:]
                
                for x in d[k]:
                    if x not in explored:
                        explored.add(x)
                        if x == endWord:
                            return length + 1
                        else:
                            queue.append((x, length+1,))
                        
        return 0
