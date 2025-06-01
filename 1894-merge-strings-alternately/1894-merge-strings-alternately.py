class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        mergedString = []
        len1 = len(word1)
        len2 = len(word2)
        i=0
        j=0

        if len1==0:
            return word2
        
        if len2==0:
            return word1

        while i<len1 and j<len2:
            mergedString.append(word1[i])
            mergedString.append(word2[j])
            i+=1
            j+=1
        
        while i<len1:
            mergedString.append(word1[i])
            i+=1
        
        while j<len2:
            mergedString.append(word2[j])
            j+=1
        
        return "".join(mergedString)