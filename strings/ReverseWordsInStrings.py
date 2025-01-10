#151
# https://leetcode.com/problems/reverse-words-in-a-string/
import re


def reverseWords(s):
    arr = re.split(r"\s+",s)
    arr.reverse()
    ans =""
    for i in arr:
        ans += i + " "
    return ans.strip()

if __name__ == '__main__':
    print(reverseWords("The sky is blue "))
