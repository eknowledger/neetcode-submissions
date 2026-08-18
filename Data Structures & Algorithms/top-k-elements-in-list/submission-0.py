class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        freq = [[] for i in range(len(nums) + 1)] # buckets same size of the array length. at most max number of frequencies

        # count frequencies
        for n in nums:
            count[n] = 1 + count.get(n , 0)
        
        # create buckets of frequencies 
        for n,c in count.items():
            freq[c].append(n)

        # retrun results
        res = []
        for i in range(len(freq)-1, 0, -1): # reverse loop use -1, 0 to stop
            for c in freq[i]:
                res.append(c)
                if len(res) == k:
                    return res

