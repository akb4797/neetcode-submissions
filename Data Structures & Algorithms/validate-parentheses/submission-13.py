class Solution:
    def isValid(self, s: str) -> bool:
        # Odd-length strings can never be matched
        if len(s) % 2 != 0:
            return False
            
        brackets = {'(': ')', '{': '}', '[': ']'}
        stack = []
        
        for char in s:
            if char in brackets: # Checks keys (opening brackets)
                stack.append(char)
            else:
                # If stack is empty or the top of stack doesn't match the closing bracket
                if not stack or brackets[stack.pop()] != char:
                    return False
                    
        return len(stack) == 0

