class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        last_occurrence = {}
        for i, char in enumerate(s):
            last_occurrence[char] = i
        
        visited = set()
        
        stack = []
        
        for i, char in enumerate(s):
            if char in visited:
                continue
            
            while (stack and char < stack[-1] and 
                  i < last_occurrence[stack[-1]]):
                removed = stack.pop()
                visited.remove(removed)
            
            stack.append(char)
            visited.add(char)
        
        return ''.join(stack)