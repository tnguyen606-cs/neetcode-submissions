class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        O(m * n): m is len(strs), n is len(max(str))
        """
        output = []
        map = defaultdict(list)

        for str in strs:
            chars = [0] * 26
            for c in str:
                chars[ord(c) - ord('a')] += 1
            map[tuple(chars)].append(str)

        return list(map.values())

            

