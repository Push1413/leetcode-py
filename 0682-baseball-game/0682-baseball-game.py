class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for char in operations:
            if char=='C':
                stack.pop()
            elif char=='D':
                newRecord = stack[-1] * 2
                stack.append(newRecord)
            elif char =='+':
                prev = stack.pop()
                prev2 = stack[-1]
                newRecord = prev + prev2
                stack.append(prev)
                stack.append(newRecord)
            else:
                stack.append(int(char))
        
        return sum(stack)