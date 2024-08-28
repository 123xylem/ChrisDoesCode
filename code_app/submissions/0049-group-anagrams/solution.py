class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = defaultdict(list)
        #Use hashmap. 
        # for each sorted word make a key
        # Append the unsorted anagram word to that key each time its found
        for word in strs:
            sorted_word = tuple(sorted(word))
            answer[sorted_word].append(word)
        return list(answer.values())
        
