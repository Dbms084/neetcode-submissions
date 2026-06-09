class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict = {}
        for word in strs:
            signature = "".join(sorted(word))
            if signature not in mydict:
                mydict[signature] = []
            mydict[signature].append(word)
        ans = list(mydict.values())
        return ans