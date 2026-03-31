class Solution(object):
    def isValid(self, s):
        stack = []
        mapping = {")":"(", "]":"[", "}":"{"}

        for char in s:
            if char in mapping.values():  # যদি ওপেন ব্র্যাকেট
                stack.append(char)
            else:  # ক্লোজ ব্র্যাকেট
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()

        return len(stack) == 0