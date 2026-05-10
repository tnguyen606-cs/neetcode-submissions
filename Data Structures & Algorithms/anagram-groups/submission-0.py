class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        - outputColl = {}
        - seen = []
        - str in strs:
            sortedStr = sort(str)
            if sortedStr in seen:
                outputColl[sortedStr] = [..., str]
            else:
                outputColl[sortedStr] = [str]
                seen.add(str)
        - output = []
        - [sortedStr, anagramArr] in outputColl:
            output.add(anagramArr)
        """

        groupColl = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            groupColl[sortedS].append(s)
        return list(groupColl.values())