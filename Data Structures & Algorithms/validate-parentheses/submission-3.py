class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False

        br_dict = {')':'(', '}':'{', ']':'['}
        br_stack = []

        for br in s:
            if br in br_dict.values():
                br_stack.append(br)
            else:
                if not br_stack or br_stack.pop() != br_dict[br]:
                    return False
        if br_stack:
            return False
        return True
