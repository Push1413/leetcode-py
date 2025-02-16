class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        end= 0
        n = len(s)
        longestSubStr = 0
        set1 = set()
        for i in range(n):
            if s[i] in set1:
                while s[i] in set1:
                    set1.remove(s[end])
                    end+=1
                set1.add(s[i])
            else:
                set1.add(s[i])
                longestSubStr = max(i-end+1,longestSubStr)

        return longestSubStr



        