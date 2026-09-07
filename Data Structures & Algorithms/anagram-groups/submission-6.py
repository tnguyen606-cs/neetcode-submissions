class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        """
        Time: O(m * n)
        Space: O(n)
        """

        hmap = {} # pair: charArry=list of anagrams

        for s in strs:
            chars = [0] * 26
            for c in s:
                chars[ord(c) - ord('a')] += 1
            if tuple(chars) in hmap:
                hmap[tuple(chars)].append(s)
            else:
                hmap[tuple(chars)] = [s]

        return list(hmap.values())