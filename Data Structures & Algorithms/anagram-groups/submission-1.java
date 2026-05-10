class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        /**
        - outputColl = {}
        - str in strs:
            sortedStr = sort(str)
            if sortedStr in outputColl:
                outputColl[sortedStr] = [..., str]
            else:
                outputColl[sortedStr] = [str]
        - output = []
        - [sortedStr, anagramArr] in outputColl:
            output.add(anagramArr)
        */

        Map<String, List<String>> groups = new HashMap<>();
        for (String s : strs) {
            char[] chars = s.toCharArray();
            Arrays.sort(chars);
            String sortedStr = new String(chars);
            groups.putIfAbsent(sortedStr, new ArrayList<>());
            groups.get(sortedStr).add(s);
        }

        return new ArrayList<>(groups.values());
    }
}
