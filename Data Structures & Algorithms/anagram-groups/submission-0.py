class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = defaultdict(list)
        for s in strs:
            index = [0] * 26 # a-z 
            for c in s:
                index[ord(c) - ord('a')] += 1 #increment ordinal of the char
            key = tuple(index) # create an index key of the string
            groups[key].append(s) # store in dict indexed on the key with original string
        return list(groups.values())

