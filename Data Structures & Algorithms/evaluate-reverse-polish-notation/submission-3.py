class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Given: 
            integers + operators
            divisiion truncates to 0
            1 <= len(tokens) <= 10000
            operators = ['+', '-', '*', '/']
            never contains invalid tokens

        Return: the valid computation or -1 if tokens.length < 3

        Time: O(n)
        Space: O(n)

        Approach:

        """

        stack = []

        for token in tokens:
            if token == '+':
                stack.append(stack.pop() + stack.pop())
            elif token == '-':
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            elif token == '*':
                stack.append(stack.pop() * stack.pop())
            elif token == '/':
                a = stack.pop()
                b = stack.pop()
                stack.append(int(float(b) / a))
            else:
                stack.append(int(token))
        
        return stack[0]

        