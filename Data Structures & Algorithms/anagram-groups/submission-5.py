class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """

        Time: O(n*m)
        Space: O(m)
        m = strs.length, n = max(string.length)

        """
        dic = defaultdict(list) # pair of key=char[], value=str[]

        for s in strs:
            char = [0] * 26
            for c in s:
                char[ord(c) - ord('a')] += 1
            
            dic[tuple(char)].append(s)

        return list(dic.values())