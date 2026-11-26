class Solution:
    def isValid(self, s: str) -> bool:
        stack, store = [], {'{':'}', '[': ']', '(': ')'}
  
        for br in s:
            if br in store.keys():
                stack.append(br)
            else:
                if stack and store[stack[-1]] == br:
                    stack.pop()
                else:
                    return False
                
        return not stack