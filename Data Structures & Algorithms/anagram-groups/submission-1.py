class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicti = {}
        
        for stri in strs:
            compare = "".join(sorted(list(stri)))
            if compare not in dicti:
                dicti[compare] = [stri]
            else:
                dicti[compare].append(stri)
        return list(dicti.values())
