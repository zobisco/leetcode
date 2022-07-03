# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        # Traversing the Expression
        for char in s:
            if char in ["(", "{", "["]:

                # Push the element in the stack
                stack.append(char)
            else:

                # IF current character is not opening
                # bracket, then it must be closing.
                # So stack cannot be empty at this point.
                if not stack:
                    return False
                current_char = stack.pop()
                if current_char == '(':
                    if char != ")":
                        return False
                if current_char == '{':
                    if char != "}":
                        return False
                if current_char == '[':
                    if char != "]":
                        return False

        # Check Empty Stack
        if stack:
            return False
        return True


parentheses = Solution()

class mySolution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        for char in s:
            if char in ["(", "[", "{"]:
                stack.append(char)
            else:
                if not stack:
                    return False
                current_char = stack.pop()  # last item in stack
                if current_char == "(":
                    if char != ")":
                        return False
                if current_char == "[":
                    if char != "]":
                        return False
                if current_char == "{":
                    if char != "}":
                        return False

        if stack:
            return False
        return True


myParentheses = mySolution()

if __name__ == "__main__":
    print(parentheses.isValid("()"))  # expected True
    print(myParentheses.isValid("()"))
