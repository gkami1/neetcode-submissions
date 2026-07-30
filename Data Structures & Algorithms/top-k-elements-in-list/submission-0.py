class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        
        freq_buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in counter.items():
            freq_buckets[freq].append(num)
        
        result = []
        for freq in range(len(freq_buckets)-1, 0, -1):
            for num in freq_buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result