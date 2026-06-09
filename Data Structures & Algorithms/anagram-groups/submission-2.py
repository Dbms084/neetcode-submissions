class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict = {} # mapping charCount to the list of anagrams
        for word in strs:
            freq = [0]*26
            for c in word:
                index = ord(c) - ord('a')  # this maps a->0 , b-1...
                freq[index] += 1
            signature = tuple(freq)
            if signature not in mydict:
                mydict[signature] = []
            mydict[signature].append(word)
        ans = list(mydict.values())
        return ans

            



