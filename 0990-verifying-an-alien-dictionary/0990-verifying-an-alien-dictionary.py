class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderMap = {char: i for i,char in enumerate(order)}

        def compare(word1, word2):
            for c1,c2 in zip(word1,word2):
                if c1!=c2:
                    return orderMap[c1]< orderMap[c2]
        
            return len(word1) <= len(word2)

        for i in range(len(words)-1):
            if not compare(words[i],words[i+1]):
                return False
        return True

        