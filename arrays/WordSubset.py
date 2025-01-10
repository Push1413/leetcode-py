# 916
#https://leetcode.com/problems/word-subsets/description/
def wordSubsets(words1, words2):
    temp = [0] * 26
    maxsub = [0] * 26

    for word in words2:
        for ch in word:
            temp[ord(ch)-ord('a')] +=1
        for i in range(26):
            maxsub[i] = max(temp[i], maxsub[i])
        temp = [0] * 26

    ans =[]
    for word in words1:
        for ch in word:
            temp[ord(ch)-ord('a')] +=1
        isUniversal = True
        for i in range(26):
            if maxsub[i] > temp[i]:
                isUniversal = False
                break
        if isUniversal:
            ans.append(word)
        temp = [0] * 26

    return ans

if __name__ == '__main__':
    words1 = ["amazon","apple","facebook","google","leetcode"]
    words2 = ["e","o"]
    print(wordSubsets(words1, words2))


