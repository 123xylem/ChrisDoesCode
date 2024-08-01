class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        answer = defaultdict(list)
        for i in nums:
            answer_key = (i)
            answer[answer_key].append(answer_key)
        
        removals_needed = len(answer) - k
        # now trim dict removals_needed times.
        # del the key with shortest list length
        if removals_needed > 0:
            for x in range(removals_needed):
                min_key = min(answer.keys(), key=lambda k: len(answer[k]))
                del answer[min_key]
        return list(answer)
        
