class Solution:
    def isValid(self, s: str) -> bool:
        mapper = {']':'[','}':'{',')':'('}
        stack = []
        for p in s:
            if p in mapper:
                if not stack or mapper[p] != stack[-1]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(p)

        return True if not stack else False