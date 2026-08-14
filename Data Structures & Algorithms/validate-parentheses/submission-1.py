class Solution:
    def isValid(self, s: str) -> bool:
        """
        Given: 
            1 <= s.length <= 1000
            Contains only ['(', ')', '{', '}', '[', ']']
            1. every open is closed by the same bracket
            2. open brackets are closed in an order
            3. every close has a corresponding open bracket
            Last open bracket has the first close bracket

        Return: true if s is a valid string

        Approach:
            - create a hashmap to store each pair of brackets
            - create a stack to store each open bracket
            - for c in s:
                if c in brackets.keys():
                    stack.append(c)
                else: # this is close bracket
                    if brackets.get(stack.peek()) == c:
                        stack.pop()
                    else:
                        return False
            return True

        Time: O(n)
        Space: O(n)
        """

        bks = {'(': ')', '{': '}', '[': ']'}
        open_bks = []

        for c in s:
            if c in bks:
                open_bks.append(c)
            else:
                if open_bks and c == bks.get(open_bks[-1]):
                    open_bks.pop()
                else:
                    return False

        return len(open_bks) == 0

