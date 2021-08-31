from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mDict = defaultdict(list)
        
        for name in strs:
            sortedName = ''.join(sorted([c for c in name]))
            mDict[sortedName] += name,
            
        return mDict.values()