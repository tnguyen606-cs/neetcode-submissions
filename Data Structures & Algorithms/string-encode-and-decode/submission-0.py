class Solution:
    """
    1. Does the string contain special characters?
    2. Is there empty string or blank string?
    3. Does the string contain both lower + upper characters?
    4. Empty string <-> empty list
    5. Single string <-> single list
    """

    delimeter = "#"

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + self.delimeter + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != self.delimeter:
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res

