class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack =[]
        operators = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: int(x / y)  # Truncate toward zero
    }
        for i in tokens:
            if i in operators:
                second = stack.pop()
                first = stack.pop()
                ans = operators[i](first,second)
                stack.append(ans)
            else:
                stack.append(int(i))
        return stack.pop()




        