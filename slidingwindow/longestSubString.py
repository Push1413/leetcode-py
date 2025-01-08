def lengthOfLongestSubstring(s):
    maxSubString = 0
    set1 = set()
    left =0
    for i in range(len(s)):
        if s[i] not in set1:
            set1.add(s[i])
            maxSubString = max(i-left+1, maxSubString)
        else:
            while s[i] in set1:
                set1.remove(s[left])
                left+=1
            set1.add(s[i])
    return maxSubString

print(lengthOfLongestSubstring("abcabcbb"))