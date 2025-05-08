class Solution:
    def simplifyPath(self, path: str) -> str:
        cleaned = re.sub(r'/+', '/', path)
        parts = [part for part in cleaned.split("/") if part]
        stack = []
        for str in parts:
            if str==".":
                continue
            if str=="..":
                if len(stack)!=0:
                    stack.pop()
            else:
                stack.append(str)

        ans = "/".join(stack)
        print(ans)
        return "/"+ans


        