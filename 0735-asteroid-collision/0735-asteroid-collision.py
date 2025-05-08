class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # - means left dir
        # + means right dir
        stack = []

        for item in asteroids:
            if item >0:
                stack.append(item)
            else:
                while stack and item<0<stack[-1]:
                    if stack[-1] < -item:
                        stack.pop()
                        continue
                    elif stack[-1]==abs(item):
                        stack.pop()
                        break
                    else:
                        break
                else:
                    stack.append(item)
        return stack