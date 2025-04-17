class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        startCount =0
        result = []

        # we neglected the ')' to whom matching '(' is not found.
        for char in s:
            if char=='(':
                result.append(char)
                startCount+=1
            elif char==')':
                if startCount>0:
                    result.append(char)
                    startCount-=1
            else:
                result.append(char)
        
        startCount = 0
        finalResult = []

        # remove extra '(' from right to left for which ')' is not there.
        for char in reversed(result):
            if char=='(':
                if startCount >0:
                    finalResult.append(char)
                    startCount -=1
            elif char ==')':
                finalResult.append(char)
                startCount +=1
            else:
                finalResult.append(char)
        
        return ''.join(reversed(finalResult))



     