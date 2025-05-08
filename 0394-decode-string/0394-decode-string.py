class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char==']':
                temp =""
                while stack and stack[-1]!='[':
                    c = stack.pop()
                    temp = c+temp
                stack.pop()
                count=""
                while stack and stack[-1].isdigit():
                    c = stack.pop()
                    count = c+count
                repeatNo = int(count)
                repeatString = temp*repeatNo
                print(repeatString)
                for i in repeatString:
                    stack.append(i) 
            else:
                stack.append(char)

        return "".join(stack)