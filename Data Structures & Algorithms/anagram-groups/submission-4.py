class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagramGroup = {}

        for str in strs:
            arrStr = self.arrString(str)

            if arrStr in anagramGroup:
                anagramGroup.get(arrStr).append(str)
            else:
                anagramGroup[arrStr] = [str]

        return list(anagramGroup.values())


    def arrString(self, string: str) -> str:

        output = [0] * 26
        for s in string:
            output[ord(s) - ord('a')] += 1

        return tuple(output)


        