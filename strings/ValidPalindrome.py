import re

def isPalindrome(s):
    s = s.lower()
    s = re.sub(r'[^a-zA-Z0-9]', '', s)
    lenth = len(s)
    newString = ""
    for i in range(lenth-1,-1,-1):
        newString+=s[i]
    return newString == s


if __name__ == '__main__':
    print(isPalindrome("race a car"))